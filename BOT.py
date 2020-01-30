import discord
from discord.ext import commands
import oC

prefix = '!'

Bot = commands.Bot(command_prefix= [prefix])

ban_msg = ["qwe", "rrt", "lala"]

Bot.remove_command('help')

@Bot.event
async def on_ready():
	print("Bot is online")

@Bot.event
async def on_message(msg):
    for i in ban_msg:
        if i in msg.content:
    	    await Bot.delete_message(msg)

    await Bot.process_commands(msg)

@Bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="подпищик")
    await Bot.add_roles(member, role)

@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(title= "Info about commands", colour= 0x39d0d6)
    emb.add_field(name= "{}help".format(prefix), value= "это подсказки")
    emb.add_field(name= "{}ban".format(prefix), value= "Это бан игроков")
    await Bot.say(embed= emb)

@Bot.command(pass_context= True)
async def reaction(ctx):
    await Bot.add_reaction(ctx.message, "👍") 

@Bot.command(pass_context= True)
async def add_role(ctx, user: discord.Member, role: discord.Role):
    await Bot.add_roles(user, role)

@Bot.command(pass_context= True)
async def ban(ctx, user: discord.Member):
    await Bot.ban(user)

@Bot.command(pass_context= True)
async def привет(ctx):
    await Bot.say("Привет мой брат{}".format(ctx.message.author.mention))
    
@Bot.command(pass_context= True)
async def info(ctx, user: discord.User):
    emb = discord.Embed(title= "info about {}".format(user.name), colour= 0x39d0d6)
    emb.add_field(name= "Name", value= user.name)
    emb.add_field(name= "joined at", value= str(user.joined_at)[:16])
    if user.game is not None:
        emb.add_field(name= "Game", value= user.game)
    emb.set_thumbnail(url= user.avatar_url)
    emb.set_author(name= Bot.user.name, url= "https://discordapp.com/api/oauth2/authorize?client_id=669818088111210506&permissions=8&scope=bot")
    emb.set_footer(text= "Вызов: {}".format(user.name), icon_url= user.avatar_url)
    await Bot.say(embed= emb)
    await Bot.delete_message(ctx.message)

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
