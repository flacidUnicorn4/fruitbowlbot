import discord
import datetime
import os
from discord.ext import commands

bot = commands.Bot(description="Hey! I'm Fruitbowl's personal bot! Use me at any time by using my !", command_prefix="!")

time = datetime.datetime.utcnow()


@bot.command()
async def clock(ctx):
    embed = discord.Embed(title="GMT Date and time", description=" ")
    embed.add_field(name="Date", value=f"{time.date()}")
    embed.add_field(name="time", value=f"{time.time().strftime('%H:%M:%S')}")
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator = True)
async def update(ctx, content):
    for i in ctx.guild.members:
        if not i.bot:
            await i.send(f'{content}')


@bot.command()
async def conan(ctx):
    await ctx.send("- Conan Exiles -\nJoin our world today and start your own adventure!\nIP:  185.44.78.61:7877")


@bot.command()
async def rok(ctx):
    await ctx.send("""- Reign of Kings -\nRp or PvP - Which will you choose?\nSimply search for "FruitBowl" on community servers and decide""")

bot.run(os.getenv('TOKEN'))
