import os
from dotenv import load_dotenv
from discord.ext import commands
import random
from time import sleep
from Football_scraper import today_scraper, yesterday_scraper

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')
Guild = os.getenv('DISCORD_GUILD')
Channel = "80-as-evek"
bot = commands.Bot(command_prefix='!')



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='football_today')
async def games_today(ctx):
    lists = today_scraper()
    for text in lists:
        for result in text:
            await ctx.send(result)

@bot.command(name='heartbeat')
async def heartbeat(ctx):
    with open('test.txt') as f:
        lines = f.readlines()
    await ctx.send(lines)
@bot.command(name='football_yesterday')
async def games_yesterday(ctx):
    text = yesterday_scraper()
    for result in text:
        await ctx.send(result)


@bot.event
async def on_ready():
    for guild in bot.guilds: #in case your bot is connected to multiple servers
        if guild.name == Guild:
            break

    print(f'{bot.user.name} has connected to {guild.name} id {guild.id}')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == "Happy Birthday":
        response = "happy birthday indeed"
        await message.channel.send(response)
    elif 'asd' in message.content:
        print(message.channel)
        await message.channel.send('fgh')
    elif 'btc' in message.content:
        await message.channel.send(f'{message.content} to the moon')
    await bot.process_commands(message) #so commands work

bot.run(Token)