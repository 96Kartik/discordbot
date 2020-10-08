# bot.py
import os
import discord, requests, random

from dotenv import load_dotenv
from discord.ext import commands
from search import search_on_google, get_search_history_by_keywords, store_search_history

# to load .env file on shell env omm server
load_dotenv()

# to allow commands without prefix from local server/guild (in our case chatbot)
def command_prefix(bot, message):
    return ''

bot = commands.Bot(command_prefix=command_prefix)

# Kartbot Events
@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')
	return True


@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hello {member.name}, welcome to {member.dm_channel} / guild! We have a very intresting Bot here who can google anything for you. Check it out.'
	)
	return True

# Kartbot Commands
@bot.command(name='hi')
async def hi(ctx):
    await ctx.send("hey")


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("hey")


@bot.command(name='hey')
async def hey(ctx):
    await ctx.send("hey")


# Kartbot command to perform google search
@bot.command(name='!google', help='To perform Google search.')
async def google_search(ctx, *argv):
    search_text = ''
    for arg in argv:
    	search_text+=" "+str(arg)
    search_text = search_text.strip()
    search_result = search_on_google(search_text)
    if len(search_result) < 1:
    	await ctx.send('No item found')
    else:
    	response_list = [
    		discord.Embed(title = res.get('title'), url = res.get('link'), description = res.get('snippet')) for res in search_result[:5]]
    	await ctx.send('Top 5 Search Results are as follows:')
    	for resp in response_list:
    		await ctx.send(embed = resp)
    	store_search_history(search_text, ctx.author)
    return True


# Kartbot command to show recent Searches
@bot.command(name='!recent', help='To retrieve history of previous Google searches.')
async def get_recent_history(ctx, *argv):
	search_text = ''
	for arg in argv:
		search_text+=" "+str(arg)
	search_text = search_text.strip()
	recent_searches = get_search_history_by_keywords(search_text, ctx.author)
	if recent_searches:
		response = "Recent related searches :\n"
		await ctx.send('Search Results are :')
		for resp in recent_searches:
			response+= str(resp)+"\n"
		await ctx.send(response)
	else:
		await ctx.send(f'You never searched for : "{search_text}"')
	return True