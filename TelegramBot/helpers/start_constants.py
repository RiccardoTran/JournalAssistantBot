from TelegramBot.version import (__python_version__, __version__, __pyro_version__, __license__)

USER_TEXT = """
🗒️ Documentation for commands available to user's

• /start: To Get this message

• /help: Alias command for start

• /alive: Check if bot is alive or not.

• /ping: Alias command for alive.

• /paste: paste text to katb.in website.
"""

SUDO_TEXT = """
🗒️ Documentation for Sudo Users commands.

• /speedtest: Check the internet speed of bot server.

• /serverstats: Get the stats of server.

• /dbstats: Get the stats of database 

• /stats: Alias command for serverstats

• /log: To get the log file of the bot.
"""

DEV_TEXT = """
🗒️ Documentation for Developers Commands.

• /update: Update the bot to latest commit from repository. 

• /restart: Restart the bot.

• /shell: Run the terminal commands via bot.

• /py: Run the python commands via bot

• /broadcast: Broadcast the message to bot users and chats.
"""

ABOUT_CAPTION = f"""• Python version : {__python_version__}
• Bot version : {__version__}
• pyrogram  version : {__pyro_version__}
• License : {__license__}

**Github Repo**: https://github.com/sanjit-sinha/TelegramBot-Boilerplate"""

START_ANIMATION = "https://telegra.ph/file/c0857672b427bec8542f6.mp4"

START_CAPTION = """Hey There! I will hep you log your day through my questions. \n\n When you're ready, press Log My Day."""

COMMAND_CAPTION = """**Here are the list of commands which you can use in bot.\n**"""
