from discord.ext import commands
import os

# token = os.environ['TOKEN']
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')
bot.load_extension('music')
bot.run(token)
