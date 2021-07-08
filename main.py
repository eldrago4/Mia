import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from gsheet import *

client = discord.Client()
sheet = gsheet()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

if "responding" not in db.keys():
	db["responding"] = True


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return (quote)


def update_encouragements(encouraging_message):
	if "encouragements" in db.keys():
		encouragements = db["encouragements"]
		encouragements.append(encouraging_message)
		db["encouragements"] = encouragements
	else:
		db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
	encouragements = db["encouragements"]
	if len(encouragements) > index:
		del encouragements[index]
		db["encouragements"] = encouragements


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	activity = discord.Game(name="Netflix", type=3)
	await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_message(message):
	if message.author == client.user:
	  return
	msg = message.content
	if msg.startswith('$inspire'):
		quote = get_quote()
		await message.channel.send(quote)

	if db["responding"]:
		options = starter_encouragements
		if "encouragements" in db.keys():
			options = options + db["encouragements"]

		if any(word in msg for word in sad_words):
			await message.channel.send(random.choice(options))

	if msg.startswith("$new"):
		encouraging_message = msg.split("$new ", 1)[1]
		update_encouragements(encouraging_message)
		await message.channel.send("New encouraging message added.")

	if msg.startswith("$del"):
		encouragements = []
		if "encouragements" in db.keys():
			index = int(msg.split("$del", 1)[1])
			delete_encouragment(index)
			encouragements = db["encouragements"]
		await message.channel.send(encouragements)

	if msg.startswith("$list"):
		encouragements = []
		if "encouragements" in db.keys():
			encouragements = db["encouragements"]
		await message.channel.send(encouragements)

	if msg.startswith("$responding"):
		value = msg.split("$responding ", 1)[1]

		if value.lower() == "true":
			db["responding"] = True
			await message.channel.send("Responding is on.")
		else:
			db["responding"] = False
			await message.channel.send("Responding is off.")

# Command to insert data to e

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.s '):
        
        # Code
        msg = message.content[3:]
        result = [x.strip() for x in msg.split(',')]
        if len(result) == FIELDS:
            # Add
            print(message.created_at)
            SPREADSHEET_ID = ['1wC2RdSb-kV4x-alolfpckXu6fZ3VO1Hrr8AcfNJ0wEU']
            RANGE_NAME = ['!attendanceA3:E34']
            DATA = [str(message.author.name)] + [str(message.author.id)] + [str(message.created_at)] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            await message.channel.send('Your data has been successfully submitted!')
        else:
            # Needs more/less fields
            await message.channel.send('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
            
    

keep_alive()
client.run(os.getenv('TOKEN'))