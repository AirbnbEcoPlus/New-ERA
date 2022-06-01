import discord

from database import databaseConnector


def reload_client():
    client = discord.Client()


    client.run(databaseConnector.get_option("token"))
