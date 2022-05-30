from database import databaseConnector
from panel import webServer
from bot import bot

if __name__ == "__main__":
    #Initialise la database
    databaseConnector.database_connect()
    #Check si le setup a été fait
    if databaseConnector.get_option("setup") == "false":
        webServer.setup()
    elif databaseConnector.get_option("setup") == "true":
        webServer.start()
    #Lance le bot discord
    if databaseConnector.get_option("setup") == "true":
        bot.run()





