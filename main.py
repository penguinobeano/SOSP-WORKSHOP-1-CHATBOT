from discord.ext import commands
import os 
import random
bot = commands.Bot(command_prefix = "!")
bot.videos = ['https://www.youtube.com/watch?v=XmoKM4RunZQ', 'https://www.youtube.com/watch?v=qTmjKpl2Jk0', 'https://www.youtube.com/watch?v=hY7m5jjJ9mM']
bot.happyList = []
bot.rps = ['Rock', 'Paper', 'Scissors']
bot.coin = ['Heads', 'Tails']
@bot.command()
async def hello(ctx): 
   await ctx.send("Hello " + ctx.author.display_name + "!")
@bot.command()
async def cat(ctx):
  await ctx.send(random.choice(bot.videos))
@bot.command() 
async def happy(ctx, *, item):
  await ctx.send("Awesome!")
  bot.happyList.append(item)
  print(bot.happyList)
@bot.command() 
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happyList))
@bot.command()
async def calc(ctx, x: float, fn: str, y: float):
  if fn == "+":
    await ctx.send(x + y)
  elif fn == "-":
    await ctx.send(x - y)
  elif fn == "*":
    await ctx.send(x * y)
  elif fn == "/":
    await ctx.send(x / y)
  else:
    await ctx.send("We only support four function operations.")
@bot.command()
async def coinflip(ctx):
  await ctx.send(random.choice(bot.coin))

@bot.command()
async def rps(ctx, string: str):
  choice = random.choice(bot.rps)
  if choice == "Rock" and string == "Scissors":
   await ctx.send("Rock, you lose!")
  elif choice == "Rock" and string == "Paper":
   await ctx.send("Rock, you win!")
  elif choice == "Rock" and string == "Rock":
   await ctx.send("Rock, it's a tie!")
  elif choice == "Paper" and string == "Paper":
   await ctx.send("Paper, it's a tie!")
  elif choice == "Paper" and string == "Rock":
   await ctx.send("Paper, you lose!")
  elif choice == "Paper" and string == "Scissors":
   await ctx.send("Paper, you win!")
  elif choice == "Scissors" and string == "Paper":
   await ctx.send("Scissors, you lose!")
  elif choice == "Scissors" and string == "Scissors":
   await ctx.send("Scissors, it's a tie!")
  elif choice == "Scissors" and string == "Rock":
   await ctx.send("Scissors, you win!")
  else:
   await ctx.send("Please put your choice as a proper noun. For example: Rock, Paper, Scissors.")

password = os.environ["password"]
bot.run(password)