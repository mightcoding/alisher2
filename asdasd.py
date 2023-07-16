import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx, randNumber: int):
    await ctx.send('Guess a number between 1 and 10.')

    answer = random.randint(1, 10)

    if randNumber == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')

@bot.command()
async def rps(ctx, ourMove):
    botMove = random.choice(["Камень", "Ножницы", "Бумага"])
    await ctx.send(botMove)
    if ourMove == botMove:
        await ctx.send('Ничья!')
    elif (ourMove == "Камень" and botMove == "Ножницы") or (ourMove == "Бумага" and botMove == "Камень") or (ourMove == "Ножницы" and botMove == "Бумага"):
        await ctx.send('Ты победил!')
    else:
        await ctx.send('Ты проиграл!')


bot.run("MTEyNzYwMzgyODE5NjM4ODk4Ng.GvQwtW.pYS3XO7jr00M8I4-r4ulgBVk_zgQrzr4_Kxu-c")








