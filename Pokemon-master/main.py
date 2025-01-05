import discord
from discord.ext import commands
from config import token
from logic import *
import random

intents = discord.Intents.default()  
intents.messages = True              
intents.message_content = True       
intents.guilds = True                


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  


@bot.command()
async def go(ctx):
    author = ctx.author.name  
    if author not in Pokemon.pokemons.keys():
        sinif = random.randint(1,3)
        if sinif == 1:
            pokemon = Pokemon(author)  
        elif sinif == 2:
            pokemon = Warrior(author)
        elif sinif == 3:
            pokemon = Mage(author)
        else:
            pokemon = Pokemon(author)
        await ctx.send(await pokemon.info())  
        image_url = await pokemon.show_img() 
        if image_url:
            embed = discord.Embed()  
            embed.set_image(url=image_url)  
            await ctx.send(embed=embed)  
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  

@bot.command()
async def saldır(ctx,target):
    if target in Pokemon.pokemons.values() and ctx.author.name in Pokemon.pokemons.keys():
        attacker=Pokemon.pokemons[ctx.author.name]
        await ctx.send(await attacker.saldir(target))
    else:
        await ctx.send("Kendinize bir Pokemon seçiniz")

@bot.command()
async def bilgi(ctx):
    if ctx.author.name in Pokemon.pokemons.keys():
        pokemon=Pokemon.pokemons[ctx.author.name]
        await ctx.send(await pokemon.info())
    else:
        await ctx.send("Kendinize bir Pokemon seçiniz")



@bot.command()
async def besle(ctx):
    if ctx.author.name in Pokemon.pokemons.keys():
        fed=Pokemon.pokemons[ctx.author.name]
        await ctx.send(await fed.feed())
    else:
        await ctx.send("Kendinize bir Pokemon seçiniz")

    

        
        






bot.run(token)
