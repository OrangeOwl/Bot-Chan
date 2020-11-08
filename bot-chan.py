import os
import time
import discord
import requests
import random
from discord.ext import commands
#For Web-Scraping
from bs4 import BeautifulSoup
#A Google Search API
from googlesearch import search 

messages = [
"Yes it's lookin' good, I bet my Waifu on it!", "Outlook looks great! ", "As I see it, it's lookin' to be as good as Mob Psycho 100 II", "Your future almost looks as bright as Senku from Dr. Stone...almost", "Your future looks better than the dishes in Food Wars", "NANI! It looks great!", "Are you destined for an Isekai? Because your future will be out of this world!",
"I can’t make out a reply right now.", "The prediction is foggy, like the glasses of a sweaty weeb at an anime convention", "It’s about as uncertain as a third season of One Punch Man",
"The outlook ain't very Sugoi", "big oof bruh, that's all I can say", "The outcome looks more trash than your taste in Anime", "Your chances of success are about as slim as you dating your favourite Waifu."   
]

bot = commands.Bot(command_prefix = '!')
#EVENTS
#A terminal command that lets me know the bot is running in the terminal
@bot.event
async def on_ready():
	print('Bot-chan is ready')
	
#The on_message event lets the bot listen for certain key-words	
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if ('69') in message.content:
		await message.channel.send('Nice')
		
	#Getting it to listen to all the possible variants of Neko		
	if ('neko') in message.content.lower():
		path ='./cat'
		files = os.listdir(path)
		index = random.randrange(0, len(files))
		neko = files[index]
		print(neko)
		await message.channel.send(file=discord.File("./cat/" + neko))
	if ('cat-girl') in message.content.lower():
		path ='./cat'
		files = os.listdir(path)
		index = random.randrange(0, len(files))
		neko = files[index]
		print(neko)
		await message.channel.send(file=discord.File("./cat/" + neko))
	if ('catgirl') in message.content.lower():
		path ='./cat'
		files = os.listdir(path)
		index = random.randrange(0, len(files))
		neko = files[index]
		print(neko)
		await message.channel.send(file=discord.File("./cat/" + neko))
	#-----------------------------------------------------------------------
	#Rating Waifus
	if ('bot-chan rate my waifu') in message.content.lower():
		score = random.randint(0,10)
		await message.channel.send('I rate your waifu ' + str(score) + '/10')
		if score == 10:
			await message.channel.send("Wow, she's way too moe for you Senpai!")
		elif score == 9:
			await message.channel.send("You actually have good taste? Go figure")	
		elif score >= 6:
			await message.channel.send("You're Waifu is pretty kawaii, I guess. Not that I care of course")	
		elif score == 5:
			await message.channel.send("An average waifu for an average weeaboo")
		elif score == 4:
			await message.channel.send("Your taste in waifus could use some work")	
		elif score >= 1:
			await message.channel.send("Your waifu sucks, and you should feel bad")	
		elif score == 0:
			await message.channel.send("Baka! Only you could like someone like that!")
		else:
			await message.channel.send("An average waifu for an average weeaboo")		
	if ('botchan rate my waifu') in message.content.lower():
		score = random.randint(0,10)
		await message.channel.send('I rate your waifu ' + str(score) + '/10')
		if score == 10:
			await message.channel.send("Wow, she's way too moe for you Senpai!")
		elif score == 9:
			await message.channel.send("You actually have good taste? Go figure")	
		elif score >= 6:
			await message.channel.send("You're Waifu is pretty kawaii, I guess. Not that I care of course")	
		elif score == 5:
			await message.channel.send("An average waifu for an average weeaboo")
		elif score == 4:
			await message.channel.send("Your taste in waifus could use some work")	
		elif score >= 1:
			await message.channel.send("Your waifu sucks, and you should feel bad")	
		elif score == 0:
			await message.channel.send("Baka! Only you could like someone like that!")
		else:
			await message.channel.send("An average waifu for an average weeaboo")		
	#--------------------------------------------------------------------------		
	#fortune teller	
	if ('fortune') in message.content.lower():
		await message.channel.send("My prediction is...." + messages[random.randint(0, len(messages)-1)])
	
	#Hang in There
	if ('hang in there') in message.content.lower():
		print('HIT sent')
		await message.channel.send(file=discord.File("hit/1.jpg"))
		
	#This line is necessary, otherwise it will play this event only when receiving messages and ignore the commands		
	await bot.process_commands(message)
	
#COMMANDS: Asynchronous functions where the trigger word is the name of the function(ctx).
#Then the function sends message with the ctx.send()

#COMMANDS
@bot.command()	
async def hello(ctx):
#Simple message command
	await ctx.send("H-Hey " + str(ctx.author) + "-senpai! UwU")
	
@bot.command()	
async def ping(ctx):
#I use an f string to issue a ping command
	await ctx.send(f" Don't tell me what to do! Baka! [{round(bot.latency * 1000)}ms]")	
	
@bot.command()
async def news(ctx):
	#WEB SCRAPING FOR TITLES
	URL = 'https://www.crunchyroll.com/news'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find_all('h2')
	title1 = results[0]
	title2 = results[1]
	title3 = results[2]
	
	#WEB SCRAPING FOR LINKS FROM THE TITLES
	links1 = results[0].find('a')
	link1 = links1.get('href')
	links2 = results[1].find('a')
	link2 = links2.get('href')
	links3 = results[2].find('a')
	link3 = links3.get('href')
	
	#EMBED
	embed=discord.Embed(title="Click Here for More Details", url="https://www.crunchyroll.com/news", description="The Top 3 News Articles", color=0xff6100)
	embed.set_author(name="Crunchyroll News", url="https://www.crunchyroll.com/news",icon_url="http://assets.vg247.com/current/2014/03/crunchyroll-logo.jpg")
	embed.set_thumbnail(url="http://assets.vg247.com/current/2014/03/crunchyroll-logo.jpg")
	embed.add_field(name=title1.get_text(), value="https://www.crunchyroll.com" + link1, inline=False)
	embed.add_field(name=title2.get_text(), value="https://www.crunchyroll.com" + link2, inline=False)
	embed.add_field(name=title3.get_text(), value="https://www.crunchyroll.com" + link3, inline=False)
	embed.set_footer(text="https://www.crunchyroll.com/news")
	await ctx.send(embed=embed)
@bot.command()
async def anime(ctx, arg):
#Performs a google search for the anime chosen, adding "My Anime List" to the end to result in a bias towards results on MAL
	query = arg + "My Anime List"
	for anime in search(query, tld="co.in", num=1, stop=1, pause=0.5):
		await ctx.send(anime)
	
@bot.command()
async def CR(ctx, arg):
#This command generates crunchyroll links, presuming you use the exact title as Crunchyroll does
	info = [s.replace(' ','-') for s in arg]
	CR = ''.join(map(str, info))
	await ctx.send("https://crunchyroll.com/" + CR.casefold())	

@bot.command()
async def music(ctx):
#I use file and open commands to read my text file with Youtube Links
#Then I assign a variable (music) to the list created by splitting each line into an item
#I then close the file, and get the bot to message a random choice from the list
	file = open("text/op.txt")
	music = file.read().split('\n')
	file.close()
	music.remove("")
	await ctx.send(random.choice(music))
	
#Runs the bot and authorizes the bot with it's unique token
bot.run('PUT TOKEN HERE')
