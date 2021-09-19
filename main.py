import asyncio
import os
import random
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from requests import get
import youtube_dl

import main
import utilities

load_dotenv()
token = os.getenv('discordToken')
server = os.getenv('discordServer')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/')
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

sessions = []


def check_session(ctx):
    if len(sessions) > 0:
        for i in sessions:
            if i.guild == ctx.guild and i.channel == ctx.author.voice.channel:
                return i
        session = utilities.Session(ctx.guild, ctx.author.voice.channel, id=len(sessions))
        sessions.append(session)
        return session
    else:
        session = utilities.Session(ctx.guild, ctx.author.voice.channel, id=0)
        sessions.append(session)
        return session


def continue_queue(ctx):
    fut = asyncio.run_coroutine_threadsafe(skip(ctx, internal=True), bot.loop)
    try:
        fut.result()
    except Exception as e:
        print(e)


@bot.command(name='play')
async def play(ctx, *, arg):
    try:
        voice_channel = ctx.author.voice.channel
    except AttributeError as e:
        print(e)
        await ctx.send("Tu não tá conectado num canal de voz, burro")
        return

    if not voice_channel:
        await ctx.send("Tu não tá conectado a nenhum canal de voz!")
        return

    session = check_session(ctx)

    with youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        try:
            requests.get(arg)
        except Exception as e:
            print(e)
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else:
            info = ydl.extract_info(arg, download=False)

    url = info['formats'][0]['url']
    thumb = info['thumbnails'][0]['url']
    title = info['title']

    session.q.enqueue(title, url, thumb)
    for i in session.q.queue:
        print(i[0])

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice:
        await voice_channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        await ctx.send(thumb)
        await ctx.send(f"Adicionado à queue: {title}")
        return
    else:
        await ctx.send(thumb)
        await ctx.send(f"Tocando agora: {title}")

        source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
        voice.play(source, after=lambda e: continue_queue(ctx))


@bot.command(name='next', aliases=['skip'])
async def skip(ctx, internal=False):
    session = check_session(ctx)
    session.q.next()

    voice = discord.utils.get(bot.voice_clients, guild=session.guild)
    source = await discord.FFmpegOpusAudio.from_probe(session.q.current_music_url, **FFMPEG_OPTIONS)
    print(source)

    if voice.is_playing():
        voice.stop()
        voice.play(source, after=lambda e: continue_queue(ctx))
        return

    # if voice.is_playing():
    #     if internal:
    #         voice.stop()
    #         voice.play(source, after=lambda e: next(ctx))
    #         return
    #     else:
    #         voice.stop()
    #         voice.play(source)
    #         return

    voice.play(source, after=lambda i: main.continue_queue(ctx) if not internal else i)


@bot.command(name='print')
async def print_info(ctx):
    session = check_session(ctx)
    await ctx.send(f"Session ID: {session.id}")
    queue = [q[0] for q in session.q.queue]
    await ctx.send(f"Queue: {queue}")


@bot.command(name='leave')
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected:
        await voice.disconnect()
    else:
        await ctx.send("Bot not connect, so it can't leave.")


@bot.command(name='pause')
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Não ta tocando porra nenhuma mlk va ser burro no inferno")


@bot.command(name='resume')
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused:
        voice.resume()
    else:
        await ctx.send("Música já ta pausada, mangolao")


@bot.command(name='stop')
async def stop(ctx):
    session = check_session(ctx)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing:
        voice.stop()
        session.q.clear_queue()
    else:
        await ctx.send("Não tem nada tocando ô abobado.")


bot.run(token)
