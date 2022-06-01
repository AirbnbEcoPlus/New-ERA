from database import databaseConnector
from panel import webServer
from bot import bot

if __name__ == "__main__":
    #Initialise la database
    databaseConnector.database_connect()
    #Lance le bot discord
    if databaseConnector.get_option("setup") == "true":
        bot.reload_client()






