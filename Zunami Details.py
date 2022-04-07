from discord.ext import commands
import gspread
import numpy as np

gc = gspread.service_account(filename='discort-zunami-c27a701ced9a.json')
sht1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1lDJmHinja4nMis2RUsX2QBWAzVqaW8u0TdMWUZdhuqU/edit#gid=1902601867') #1
worksheet = sht1.worksheet("Расчет_детальный")
worksheet3 = sht1.worksheet("Ответы на google-форму")
values_list1= worksheet3.col_values(6) #id Ответы на google-форму

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
            for i in values_list1:
                if i == str(message.author):
                    worksheet.update('A1', str(message.author))
                    b = worksheet.get_values('A1:B24')
                    a = np.array(b)
                    await message.channel.send(a)
                    break
            else:
                await message.channel.send("We couldn't find your username probably for 2 reasons:\n1.When filling out a Google form, you entered your nickname with an error (for example, an extra space).\n2. You didn't fill out a Google form. Unfortunately, without completing this step, we will not be able to add you to the Leaderboard.\nYou can fill out the form here: "
                    'https://docs.google.com/forms/d/e/1FAIpQLSfqv9PZi7UgGbWKdcN4cfBVPv8s2HOn_SQWq_Ii8d-afVVPQg/viewform\nIf you definitely filled out the form accurately, but still have not find yourself on the Leaderboard, please contact Oksana#9601 on Discord.')
    else:
         if message.content.lower().startswith('!check2'):
                if message.channel.id == cmdChannel.id:
                    for i in values_list1:
                        if i == str(message.author):
                           worksheet2.update('A1', str(message.author))
                           c = worksheet2.get_values('A1:B15')
                           v = np.array(c)
                           await message.channel.send(v)
                           break
                    else:
                      await message.channel.send("We couldn't find your username probably for 2 reasons:\n1.When filling out a Google form, you entered your nickname with an error (for example, an extra space).\n2. You didn't fill out a Google form. Unfortunately, without completing this step, we will not be able to add you to the Leaderboard.\nYou can fill out the form here: "
                    'https://docs.google.com/forms/d/e/1FAIpQLSfqv9PZi7UgGbWKdcN4cfBVPv8s2HOn_SQWq_Ii8d-afVVPQg/viewform\nIf you definitely filled out the form accurately, but still have not find yourself on the Leaderboard, please contact Oksana#9601 on Discord.')


client.run(token)
