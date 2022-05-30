import discord
from database import databaseConnector


def run():
    bot = discord.Client()




    @bot.command()
    async def rename(ctx, name):
        await bot.user.edit(username=databaseConnector.get_option("username"))
    async def rename(ctx, name):
        await bot.user.edit(avatar="/panel/static/images/icon.png")
    bot.run(databaseConnector.get_option("token"))



