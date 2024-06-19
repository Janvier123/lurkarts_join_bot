import os
import asyncio
import ctypes
from random import randint
import time
from twitchio.ext import commands

#---------------------------------------------------------
# Give the windows window a nice name
#---------------------------------------------------------
ctypes.windll.kernel32.SetConsoleTitleW("Lurkarts Bot")


#---------------------------------------------------------
# Start the main script
#---------------------------------------------------------
class Bot(commands.Bot):

    # Main setup
    def __init__(self):
        super().__init__(token='oauth:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', client_id='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', prefix='!', heartbeat=30, initial_channels=["abulic"])

    # Does it work? If yes say logged in as
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    # Listen for events
    async def event_message(self, message):
        
        # Dont listen to our own bot
        if message.echo:
            return

        # Listen for !lurkarts in chat
        if message.content == "Card raffle incoming, !lurkarts time" and message.author.name.lower() == "lurkarts":
            print(time.strftime("%d/%m %H:%M:%S") + "|  Lurkarts raffle found, joining")
            
            # Set a random time to reply in the chat
            # Lurkarts bot expects a reply withing 120sec!
            time.sleep(randint(3,30))
            await message.channel.send("!lurkarts")

        await self.handle_commands(message)


    # Block any ! commands we dont need in chat
    async def event_command_error(self, ctx, error: Exception):
        return

bot = Bot()
bot.run()