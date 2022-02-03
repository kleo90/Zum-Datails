import discord
from discord.ext import commands
import gspread
import numpy as np

gc = gspread.service_account(filename=r"C:\Users\Ксюша\Downloads\discort-zunami-c27a701ced9a.json")
sht1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1lDJmHinja4nMis2RUsX2QBWAzVqaW8u0TdMWUZdhuqU/edit#gid=1902601867') #1
worksheet = sht1.worksheet("Расчет_детальный")

sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/19uW05thc6wBRnwbS10hj0cHT_jWP1kQE42ezkKeyG-g/edit#gid=1902601867') #2
worksheet2 = sht2.worksheet("Расчет_детальный")

client = commands.Bot( command_prefix=" ! " )
token = 'OTE4MTE0MjQ4NjE2NDYwMzE4.YbCihg.TJ7zl2BWNUX4WJ0tJYAIzT5nvvo'

@client.event
async def on_message(message):
    global a
    global v

    cmdChannel = client.get_channel(938792251939762266)
    if message.content.lower().startswith('!check1'):
        if message.channel.id == cmdChannel.id:
            worksheet.update('A1', str(message.author))
            b=worksheet.get_values('A1:B24')
            a = np.array(b)
        await message.channel.send(a)

    else:
         if message.content.lower().startswith('!check2'):
                if message.channel.id == cmdChannel.id:
                    worksheet2.update('A1', str(message.author))
                    c = worksheet2.get_values('A1:B15')
                    v = np.array(c)
                await message.channel.send(v)


client.run(token)