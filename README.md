# Discord-MusicBot
##A simple discord.py music bot.

***This bot has dependencies on FFmpeg, youtube_dl, dotenv, PyNaCl, requests and (obviously) discord.py.***

This repo have the raw code to run a (almost) perfectly fine discord music bot. To run it, a few steps are necessary:

1. Download [FFmpeg](https://ffmpeg.org/download.html) and __install__ it.
   - Depending on your OS, it will have a different way to do it. 
     - On (Windows)[https://www.wikihow.com/Install-FFmpeg-on-Windows]
     - On (Linux)[https://www.tecmint.com/install-ffmpeg-in-linux/]
     - On (Mac OS X)[http://jollejolles.com/install-ffmpeg-on-mac-os-x/]
2. Open your favorite IDE for writing in Python, start a new project and paste the [main](Discord-MusicBot/main.py) and [utilities](Discord-MusicBot/utilities.py) on the same folder.
3. Start your venv (virtual enviroment) and pip install the following libraries:
   - [youtube_dl](https://pypi.org/project/youtube_dl/)
   - [python-dotenv](https://pypi.org/project/python-dotenv/)
   - [PyNaCl](https://pypi.org/project/PyNaCl/)
   - [discord.py](https://pypi.org/project/discord.py/)
4. Create a file called .env and paste in it `discordToken = 'YOUR_DISCORD_TOKEN_HERE'`.
   - To get a discord token you need to:
     1. Enter the (Discord Developer Portal)[https://discord.com/developers/applications]
     2. Create an application.
     3. Add a bot to it on "Bot" tab.
     4. Make sure the "Server members intent" option is checked on.
     5. Still on the "Bot" tab, on the right of the bot's icon, click "Copy" to copy the token to your clipboard.
5. If you want to feel free to read and change anything you want in the code. It was made in about 3 or 4 days upon insanity and insomnia. I recommend to translate the messages the bot sends back to the chat, currently it is on PT-BR.
6. Run it on your IDE or compile it to a .exe or similar, the bot is ready!
