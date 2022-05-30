import discord
from database import databaseConnector


def run():
    client = discord.Client()






    client.run(databaseConnector.get_option("token"))



