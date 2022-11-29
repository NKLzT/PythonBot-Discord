import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e) 
@bot.tree.command(name='hello')
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!")


@bot.tree.command(name='coe')
async def coe(interaction: discord.Integration):
    await interaction.response.send_message(f"Fala fio bom?!")


bot.run('MTA0NjkyMDI2MzcxNzEwOTgzNQ.G0RM5v.W_C2JvkdlZ1l5aLViSoX8LWpNBfXd2jbZRkE0Y')