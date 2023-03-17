import discord
from discord.ext import commands
from datetime import datetime
from sys import exit 
import scan
from discord import utils, Client
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# client = commands.Bot(command_prefix = "!")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
guild = object()
#bot channel
bchan = 1077177180183863338
started = False
#userids 
santi = '<@635984188394307594>'
zarrar = '<@401837234170626048>'
will = '<@264081824815251456>'
jamal = '<@424447277197950977>'
neil = '<@449368126853873664>'

#counters for profit
long long santiBuy = 0
long long santiSell = 0
long long zarrarBuy = 0
long long zarrarSell = 0
long long willBuy = 0
long long willSell = 0
long long jamalBuy = 0
long long jamalSell = 0

dict userChannelIds
{



}



async def send_message(message, user_message, is_private):
    try:
        response = scan.get_message(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

    @bot.command()
    async def shutdown(ctx):
        """Logs the bot out and shuts it down"""
        shutdown_channel = bot.get_channel(1077177180183863338) # Replace with the ID of the channel you want to send the shutdown message to
        await shutdown_channel.send("Bot is shutting down...")
        await bot.logout()
    @bot.tree.command(name="hello")
    async def hello(interacton: discord.Interaction):
        await interacton.response.send_message('Hello!')

def run_discord_bot():
    TOKEN = 'MTA4MzExMDAxNzk3ODMzOTQ2OQ.GoZ27C.5TOHmw-rdO3j6oRrnzkN5sQRDCzQFEM4zOiVdw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        channel = client.get_channel(1077177180183863338) # Replace CHANNEL_ID with the actual ID of the channel you want to send a message to
        await channel.send("Huge Bot back online")
        await channel.send("Also, Fuck you Jamal")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        now = datetime.now() 
        current_time = now.strftime("%m/%d-%I:%M%p")

        #message information
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #add try catch block to throw exception on non emebedded message 
        try: 
            embeded = message.embeds[0] #convert embeded object to list        
            embed_dict = embeded.to_dict() #convers list to dict
            embeded_snipe_title = embed_dict["title"]
            sendback = discord.Embed.from_dict(embed_dict)        
            keywords = embeded_snipe_title.split()
            


            kw = []
            for word in keywords:
                if len(word):  # consider only words with length greater than 3
                    kw.append(word.lower())

            #prints selling info
            # print(f'The username is', {username})
            print(channel, end=' ')  
            for word in kw:
                print(word, end=' ')
            print("\n")
            ch = channel
            channel = client.get_channel(1077177180183863338) #channel id goes in brackets
            message_link = message.jump_url 

            for word in kw:
                if(word == 'huge'): # and username == 'Milk Up#0000'
                    with open("keywords.txt", "a") as file:
                        file.write(f"{current_time},{ch},{' '.join(keywords)}\n")
                    #await send_message(message, user_message, is_private=False)
                    # channel.send_message(message[:2])
                    if( ch == 'santi-sniping'):
                        await channel.send(santi)
                    if( ch == 'zarrar-sniping'):
                        await channel.send(zarrar)
                    if( ch == 'will-sniping'):
                        await channel.send(will)
                    if( ch == 'jamal-sniping'):
                        await channel.send(f'fuck you, {jamal}')
                    if( ch == 'neil-sniping'):
                        await channel.send(neil)
                    await channel.send(embed=message.embeds[0])
                    await channel.send(f'link: {message_link}')

        except Exception as e:
            print(f'ERROR - exception: {e}')


        # store keywords in a database or file
        # with open("keywords.txt", "a") as file:
        #     file.write(f"{message.author.id},{message.guild.id},{'|'.join(keywords)}\n")
    
    # @client.command(pass_context=True)
    # async def ping(ctx):
    #     channel = client.get_channel() #channel id goes in brackets 
    #     await channel.send('Pong!')
    @bot.event
    async def on_disconnect():
        channel = client.get_channel(1077177180183863338) # Replace CHANNEL_ID with the actual ID of the channel you want to send a message to
        await channel.send("Bot is now offline.")

        # await channel.send("Huge Bot back online")
        # await channel.send("Also, Fuck you Jamal")

    @client.event
    async def on_message(message):
        text = message.content
        author = message.author
        index = text.index("Sniped For:")
        sniped_index = string.index("Sniped For:") + len("Sniped For:")
        sniped_price = string[sniped_index:].strip()
        

    

    client.run(TOKEN)
