import discord
import os
class Bot():
    def __init__(self):
        self.TOKEN = 'Enter your discord token here.'
        self.client = discord.Client()

    async def send_file(self, file_path):
        try:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(id="Enter your discord channel ID here")
            await channel.send(file=discord.File(file_path))
            return 
        except Exception as e:
            print(f"{'-'*100}\n[ERROR]  {e}")
            return
        
    async def send_message(self, message):
        try:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(id="Enter your channel ID here")
            await channel.send(str(message))
            return 
        except Exception as e:
            print(f"{'-'*100}\n[ERROR] {e}")
            return

    def file_sender(self, file_path):
        try:
            if os.path.exists(file_path):
                self.client.loop.create_task(self.send_file(file_path))
            else:
                print(f"{'-'*100}\n[ERROR] File not found.")
            return
        except Exception as e:
            print(f"{'-'*100}\n[ERROR] {e}")
            return 

    def  message_sender(self, message):
        try:
            self.client.loop.create_task(self.send_message(message))
            print(f"{'-'*100}\n[SUCCESS] Message sent successfully.")
        except Exception as e:
            print(f"{'-'*100}\n[ERROR] {e}")
            return 



