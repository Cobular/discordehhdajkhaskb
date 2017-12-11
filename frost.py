import discord
import asyncio
import requests
import json
import logging

client = discord.Client()
user = 'Xa63Q0zbGyX6HJs9'
key = 'TcdlV8V85FotzAi6pdcmjOjCOrcBmAHM'

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')

@client.event
async def on_message(message):
    if not message.author.bot and (message.server == None or client.user in message.mentions):
        print(message.channel)
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )
    if not message.author.bot and message.channel.id == "301385917807984640":
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )
	
print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('Mzg5NTg2NzI5NzA0ODgyMTk3.DQ9vAg.LGlAvqzJpQaDEzEIrbx8FidBNuk')
