import discord
import math
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
async def birthday():
    if 'happy birthday' in ctx.content.lower():
        await ctx.channel.send('Happy Birthday! 🎈🎉')
@bot.command()
async def Import(ctx, a: str):
    if(a.lower() == "swapnil"):
        await ctx.send("ah shit, dont do ert")
    if(a.lower() == "kavin"):
        await ctx.send("budda why")
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
@bot.command()
async def mod(ctx, a: int, b: int):
    await ctx.send(a%b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command
async def power(ctx, a: int, b: int):
    await ctx.send(math.pow(a, b))

@bot.command()
async def root(ctx, a: int, b: int):
    await ctx.send(math.pow(a, (1/b)))
def integral(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = eval(f(x))
    area = eval(np.sum(fx)*(b-a)/N)
    return area    
@bot.command()
async def integrate(ctx, f, a: float, b: float, N: int):
    #prob doesn't work rihjt
    await ctx.send(integral(f, a, b, N)) 
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    emced.add_field(name = "$mod X Y", value="Gives the value of **X** mod **Y**")
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)
bot.run("NTQ1MTIyMDEwMzY4NTczNDQw.XbN7RA.rR8wgUquzsjwvUeF8rgYmh6IzVE")
































import discord as d
import numpy as np
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
client = d.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.guilds)
    print('------')
    
    guilds = bot.guilds
    k = 1
    while(k < 3):
        for i in guilds:
            for j in i.text_channels:
                await j.send("All rihjt listen up niglets. Don't try to be cool guy or I will make you do the kukkar.")
                k = k+1

    #print(bot.text_channels())

    #await fetch_channels()
def integral(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = eval(f(x))
    area = eval(np.sum(fx)*(b-a)/N)
    return area
   
#async def birthday():
#    if 'happy birthday' in ctx.content.lower():
#        await ctx.channel.send('Happy Birthday! 🎈🎉')
#@bot.command()
#async def Import(ctx, a: str):
#    if(a.lower() == "swapnil"):
#        await ctx.send("ah shit, dont do ert")
#    if(a.lower() == "kavin"):
#        await ctx.send("budda why")
#@bot.command()
#async def nigger(ctx):
#    await ctx.send("Ya you too!")
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
@bot.command()
async def mod(ctx, a: int, b: int):
    await ctx.send(a%b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def integrate(ctx, f, a: float, b: float, N: int):
    #eval(f(a, b, N))
    #try:
    #    await ctx.send(dispatcher[f](f, a, b, N))
    #except KeyError:
    #    raise ValueError('invalid input')
    #    await ctx.send("Fix parameters")
    await ctx.send(integral(f, a, b, N)) 
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    emced.add_field(name = "$mod X Y", value="Gives the value of **X** mod **Y**")
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$integrate F(x) a b N(rectangles)", value="evalues definite integral of **F(x)** from **A** to **B**. Larger **N** gives more precision, but requires more computational power.", inline = False)
    await ctx.send(embed=embed)
bot.run("NTQ1MTIyMDEwMzY4NTczNDQw.XbPZPQ.s1KfzC7UWDtmpNdT0HOSlyGPtAs")

