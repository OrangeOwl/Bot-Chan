# coding=utf-8
import os
import discord
import asyncio
#import requests
import random
from discord.ext import commands
#For Web-Scraping
from bs4 import BeautifulSoup
#A Google Search API
from googlesearch import search
#from Parser file
from News_Parser import *

#VARIABLES
messages = ["Yes it's lookin' good, I bet my Waifu on it!", "Outlook looks great! ", "As I see it, it's lookin' to be as good as Mob Psycho 100 II", "Your future almost looks as bright as Senku from Dr. Stone...almost", "Your future looks better than the dishes in Food Wars", "NANI! It looks great!", "Are you destined for an Isekai? Because your future will be out of this world!", "I can’t make out a reply right now.", "The prediction is foggy, like the glasses of a sweaty weeb at an anime convention", "It’s about as uncertain as a third season of One Punch Man", "The outlook ain't very Sugoi", "big oof bruh, that's all I can say", "The outcome looks more trash than your taste in Anime", "Your chances of success are about as slim as you dating your favourite Waifu."]
#COMMAND WORDS TO LISTEN FOR
neko_words = ['neko', 'nekos', 'cat-girl', 'catgirl']
waifu_rating = ['botchan rate my waifu', 'bot-chan rate my waifu', 'rate my waifu botchan', 'rate my waifu bot-chan']
find_anime = ['botchan find my anime', 'bot-chan find my anime', 'find my anime', 'search anime','botchan search anime', 'bot-chan search anime' ]
anime_shows = ['Gintama', 'JoJo', 'Some Harem Trash', 'Mob Psycho 100', 'Vtubers', 'Hentai', 'One Punch Man', 'Non Non Biyori', 'Yuru Camp' ]


bot = commands.Bot(command_prefix = '!')
	
#EVENTS
#A terminal command that lets me know the bot is running in the terminal
@bot.event
async def on_ready():
	print('Bot-chan is ready')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(anime_shows)))
	
#The on_message event lets the bot listen for certain key-words	
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
			
	#if ('69') in message.content.lower():
	#	await message.channel.send('Nice')
		
	if any(x in message.content.lower() for x in neko_words):
		path ='./cat'
		files = os.listdir(path)
		index = random.randrange(0, len(files))
		neko = files[index]
		print(neko)
		await message.channel.send(file=discord.File("./cat/" + neko))	
	if (' trap') in message.content.lower():
		path ='./trap'
		files = os.listdir(path)
		index = random.randrange(0, len(files))
		trap_pic = files[index]
		print(trap_pic)
		await message.channel.send('Did someone say trap? UwU *Nuzzles Closer*')
		await message.channel.send(file=discord.File("./trap/" + trap_pic))	
	#-----------------------------------------------------------------------	
	#fortune teller	
	if ('fortune') in message.content.lower():
		await message.channel.send("My prediction is...." + messages[random.randint(0, len(messages)-1)])
	
	#Hang in There
	if ('hang in there') in message.content.lower():
		print('HIT sent')
		await message.channel.send(file=discord.File("hit/1.jpg"))
	#-----------------------------------------------------------------------
	#Rating Waifus
	if any(x in message.content.lower() for x in waifu_rating):
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
			
	if ('recommend me anime') in message.content.lower():
		await message.channel.send('Name a show you like')
		def is_correct(m):
			return m.author == message.author
		try:
			entry = await bot.wait_for('message', check=is_correct, timeout=13.0)
		except asyncio.TimeoutError:
			return await message.channel.send("Sorry senpai, I can't wait that long")
		anime_title = str(entry.content)
		print(anime_title)
		query = anime_title + " MAL User Recommendations"
		for anime in search(query, tld="co.in", num=1, stop=1, pause=0.5):
			print(anime)
			page = requests.get(anime)
			soup = BeautifulSoup(page.content, 'html.parser')
		
			results = soup.find_all("div", {"style": "margin-bottom: 2px;"})
			print(results)
			#results = soup.find_all('div', 'class':'recsArea')
			title1 = results[0]
			title2 = results[1]
			title3 = results[2]
		
			T1 = title1.get_text().split()
			T2 = title2.get_text().split()
			T3 = title3.get_text().split()
	
			TITLE1 = " ".join(T1[:-1])
			TITLE2 = " ".join(T2[:-1]) 
			TITLE3 = " ".join(T3[:-1]) 
		
			#WEB SCRAPING FOR LINKS FROM THE TITLES
			links1 = results[0].find('a')
			link1 = links1.get('href')
			links2 = results[1].find('a')
			link2 = links2.get('href')
			links3 = results[2].find('a')
			link3 = links3.get('href')
		
			#EMBED
			embed=discord.Embed(title="MAL USER RECOMMENDATIONS", description="::Titles and URL's listed below::", color=0xff6100)
			embed.set_author(name="My Anime List", icon_url="https://media-exp1.licdn.com/dms/image/C4E0BAQHychSZh7ES0g/company-logo_200_200/0?e=2159024400&v=beta&t=Uyap65RCXG7VUyhO5bUS63ui3eyETYhZVpHl2tsHWcg")
			embed.set_thumbnail(url="https://media-exp1.licdn.com/dms/image/C4E0BAQHychSZh7ES0g/company-logo_200_200/0?e=2159024400&v=beta&t=Uyap65RCXG7VUyhO5bUS63ui3eyETYhZVpHl2tsHWcg")
			embed.add_field(name=TITLE1, value=link1, inline=False)
			embed.add_field(name=TITLE2, value=link2, inline=False)
			embed.add_field(name=TITLE3, value=link3, inline=False)
			embed.set_footer(text="https://myanimelist.net/")
			await message.channel.send(embed=embed)	
		
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
	#EMBED
	embed=discord.Embed(title="Click Here for More Details", url="https://www.crunchyroll.com/news", description="The Top 5 News Articles", color=0xff6100)
	embed.set_author(name="Crunchyroll News", url="https://www.crunchyroll.com/news",icon_url="http://assets.vg247.com/current/2014/03/crunchyroll-logo.jpg")
	embed.set_thumbnail(url="http://assets.vg247.com/current/2014/03/crunchyroll-logo.jpg")
	embed.add_field(name=news_title1.get_text(), value="https://www.crunchyroll.com" + news_link1, inline=False)
	embed.add_field(name=news_title2.get_text(), value="https://www.crunchyroll.com" + news_link2, inline=False)
	embed.add_field(name=news_title3.get_text(), value="https://www.crunchyroll.com" + news_link3, inline=False)
	embed.add_field(name=news_title4.get_text(), value="https://www.crunchyroll.com" + news_link4, inline=False)
	embed.add_field(name=news_title5.get_text(), value="https://www.crunchyroll.com" + news_link5, inline=False)
	embed.set_footer(text="https://www.crunchyroll.com/news")
	await ctx.send(embed=embed)
	
@bot.command()
async def CR(ctx, arg):
	info = [s.replace(' ','-') for s in arg]
	CR = ''.join(map(str, info))
	await ctx.send("https://crunchyroll.com/" + CR.lower())
	
@bot.command()
async def anime(ctx, *args):
	title = args
	query = str(title) + " My Anime List"
	for anime in search(query, tld="co.in", num=1, stop=1, pause=0.5):
		await ctx.send(anime)	

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
