# Discord-MusicBot
### A simple discord.py music bot.

This bot was built upon insomnia by me. It receives a command from your discord guild and does the magic.
It can run on multiple discord guilds at the same time, managing each session with it's correct queue and all. The only thing it doesn't do is play simultaneously in two voice channels in the same guild. I know Rythm can do it, but I didn't look into it yet to learn how it is done to implement in this simple bot. :)


## Commands:

Currently the commands prefix is the forward-slash character (/). 

To change it go to line 18 `bot = commands.Bot(command_prefix='/')` in [main.py](Discord-MusicBot/main.py) and change the forward-slash.

- /play : Searchs for the author's current voice channel, joins it and plays the requested song, which can be a url to a video on YouTube or a simple search.
- /pause : Pauses the current song.
- /resume : Resumes the current song.
- /stop : Stops playing the current song and clears the queue.
- /leave : Leaves the voice channel.
- /print : Only for debugging, returns the session ID, what is currently playing and what is on the queue.


## How to run it:
***This bot has dependencies on FFmpeg, youtube_dl, dotenv, PyNaCl and (obviously) discord.py.***

This repo has the raw code to run a (almost) perfectly fine discord music bot. To run it, a few steps are necessary:

1. Download [FFmpeg](https://ffmpeg.org/download.html) and __install__.
   - Depending on your OS, it will have a different way to do it. 
     - On [Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)
     - On [Linux](https://www.tecmint.com/install-ffmpeg-in-linux/)
     - On [Mac OS X](http://jollejolles.com/install-ffmpeg-on-mac-os-x/)
 
2. Open your favorite IDE for writing in Python, start a new project and paste the [main](Discord-MusicBot/main.py) and [utilities](Discord-MusicBot/utilities.py) on the same folder.

3. Start your venv (virtual enviroment) and pip install the following libraries:
   - [youtube_dl](https://pypi.org/project/youtube_dl/)
   - [python-dotenv](https://pypi.org/project/python-dotenv/)
   - [PyNaCl](https://pypi.org/project/PyNaCl/)
   - [discord.py](https://pypi.org/project/discord.py/)

4. Create a file called .env and paste `discordToken = 'YOUR_DISCORD_TOKEN_HERE'`.
   - To get a discord token you need to:
     1. Enter the [Discord Developer Portal](https://discord.com/developers/applications)
     2. Create an application.
     3. Add a bot on "Bot" tab.
     4. Make sure the "Server members intent" option is checked on.
     5. Still on the "Bot" tab, on the right of the bot's icon, click "Copy" to copy the token to your clipboard.
     
   - To add the bot to a server:
     1. In the your recently created application, open the "OAuth2" tab and scroll down to "Scopes".
     2. Check the "bot" option and copy the link created underneath the scopes table.
     3. Paste the link on your browser and then choose the server you want to add the bot to. You will need to be an adm in the guild to perform this action, I think.

5. If you want to, feel free to read and change anything you want in the code. It was made in about 3 or 4 days upon insanity and insomnia. I recommend to translate the messages the bot sends back to the chat, currently it is on PT-BR.

6. Run the code on your IDE or compile to a .exe or similar, the bot is ready!




### **Please, if you spot any mistakes/errors in this tutorial and on the code itself, send in an issue so I can fix it.**
