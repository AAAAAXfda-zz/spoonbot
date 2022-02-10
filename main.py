import discord


from discord.ext import commands

intents = discord.Intents.all()

try :
    with open("token.txt") as text_file:
        token = text_file.read()
except FileNotFoundError:
    print("Error : a file named 'token.txt' containing your bot token has not been found. Please create one for the bot to run correctly.")
    exit()

bot = commands.Bot(command_prefix="f!", description="a very simple yet necessary bot for any server", intents = intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("------------")
    print(f"logged in successfully as {bot.user.name} (id : {bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="coiffeur ahah"))
    print("LOADING COMPLETE")
    print("------------")

@bot.event
async def on_message(message):

    stripped_message = message.content.lower().strip(" .:?!*\)")

    if stripped_message.endswith("quoi"):
        await message.channel.send("feur")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("oui"):
        await message.channel.send("stiti")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("non") or stripped_message.endswith("nom"):
        await message.channel.send("bril")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("ouais"):
        await message.channel.send("stern")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("ça") or message.content.lower().endswith("sa"):
        await message.channel.send("pristi")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("allo"):
        await message.channel.send("à l'huile")
        print(f"ahah on vient d'avoir {message.author}")
    elif stripped_message.endswith("ok") or stripped_message.endswith("okay") :
        await message.channel.send("sur glace")
        print(f"ahah on vient d'avoir {message.author}")


    if message.content == "f!servers":
        await message.channel.send(f"Je suis actuellement sur {len(bot.guilds)} serveurs. Tapez `f!serverlist` pour en afficher la liste.")
    
    elif message.content == "f!serverlist":
        serverlist = '\n'.join([guild.name + ' - (' + str(len(guild.members)) + ' membres)' for guild in bot.guilds])
        await message.channel.send("Liste des serveurs : \n" + serverlist)

bot.run(token, bot=True, reconnect=True)
print("CONNEXION TERMINATED")


