import discord
import asyncio 
import random
from discord.ext import commands
from asyncio import sleep as s

# from timer import Timer

TOKEN = 'MTAzODI0OTUyNzkwNTM2MjAxMA.GsY1WQ.udHQYv9admCIXWj-Heyhqs65fMp5lTfq9ARHIM'
# client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# timer = timer()

@client.event
async def on_ready():
    # await client.change_presece(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="!help and being productive"))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
      return

    # put all command code here
    if message.channel.name == 'general':
      if user_message.lower() == '!help':
          myEmbed = discord.Embed(title="Bot Commands", description="Here are the commands for this bot! Prefix: !", color=0x89CFF0)
          myEmbed.add_field(name="Motivation", value="Use these commands to motivate you to study: \n `!motivation, !quotes, !roast`", inline=False)
          myEmbed.add_field(name="Music", value="We'll give you study music/playlist reccomendations! \n `!lofi, !anime, !backgroundmusic`", inline=False)
          myEmbed.add_field(name="Resources", value="Commands for helpful study ressources: \n `!studyhelp, !math, !sci, !art, !cs`", inline=False)
          myEmbed.add_field(name="Productivity", value="Use me for productivity! I have timers, reminders, and fun productivity commands. \n `!timer {insert minutes}` \n `!reminder {insert minutes} {reminder message}`", inline=False)
          myEmbed.add_field(name="Other", value=" Other fun commands! \n `!cat, !hug`", inline=False)
          myEmbed.set_image(url="https://media.discordapp.net/attachments/1038234778262052885/1038527311135395971/studybuddy.png")
          await message.channel.send(embed=myEmbed)
          return
      
      elif user_message.lower() == "!studyhelp":
        myEmbed = discord.Embed(title="Study Commands", description="!math ~ math links\n!sci ~ science links\n!art ~ art links \n!cs ~ cs links", color=0x89CFF0)
        myEmbed.set_image(url="https://media.discordapp.net/attachments/1038234778262052885/1038527311135395971/studybuddy.png")
        await message.channel.send(embed=myEmbed)
        return
      
      elif user_message.lower() == "!math":
        myEmbed = discord.Embed(title= "Trig links:", description= "\nhttps://www.mathsisfun.com/algebra/trigonometry.html\nhttps://www.khanacademy.org/math/trigonometry", color = 0x89CFF0)
        myEmbed.add_field(name="Functions", value = "https://www.mathsisfun.com/sets/function.html\nhttps://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions",  inline=False)
        await message.channel.send(embed=myEmbed)
        return
      
      elif user_message.lower() == '!sci':
        myEmbed = discord.Embed(title='Science Links:', description= 'https://instil.ca/#gsc.tab=0', color = 0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return
        
      elif user_message.lower() == "!art":
        myEmbed = discord.Embed(title= "Art links:", description= "https://www.youtube.com/watch?v=kNQCP3CtHvI\nhttps://rapidfireart.com/2017/04/06/lesson-1-how-to-sketch/\nhttps://drawpaintacademy.com/painting-for-beginners/", color = 0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return
      
      elif user_message.lower() == '!cs':
        myEmbed = discord.Embed(title= "CS Links:", description= "https://replit.com/~\n https://stackoverflow.com/ \nhttps://www.programiz.com/python-programming/modules", color = 0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return

      elif user_message.lower() == '!motivation':
        words = ["studying = money = happiness", "no bitches but if u ace that test, you will have money and thus get bitches - Elaine","you want to beat that one really annoying classmate? get a higher mark than them >:)","studying is hard. but just do it, it's not as hard as jumping off a cliff.","if you studied right now ur mom would be proud of you"]
        wordoutput = random.choice(words)
        myEmbed = discord.Embed(title="I'm rooting for you!!!", description=(wordoutput), color=0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return

      elif user_message.lower() == '!quotes':
        quotes = [' "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do." - Pelé, Brazillian pro footballer ',' "People always say that I didn’t give up my seat because I was tired, but that isn’t true. I was not tired physically… No, the only tired I was, was tired of giving in." - Rosa Parks',' "However difficult life may seem, there is always something you can do and succeed at." - Steven Hawkings',' “Success is the sum of small efforts, repeated day in and day out.” - Robert Collier, self-help author']
        quotesoutput = random.choice(quotes)
        myEmbed = discord.Embed(title="Motivational quotes", description=(quotesoutput), color=0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return

      elif user_message.lower() == "!roast":
        roasts = ['stop being lazy and procrastinating >:(', 'ur mom would not be proud of you rn', 'you no study, asian parents MAD D:', 'get your crap together and study for once ', 'remember how awful you felt when you did bad on that one test', 'I am disappointed in you. Jk unless you study ;)', 'If you do not work now. You will be crying on the toilet later.']
        roastsoutputs = random.choice(roasts)
        myEmbed = discord.Embed(title="I'm sorry in advance", description = (roastsoutputs), color = 0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return


      elif user_message.lower() == "!cat": # /ᐠ｡ꞈ｡ᐟ\ 
        cats = ['/ᐠ｡ꞈ｡ᐟ\ ', '⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⡀⠀⢀⣴⣇⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀\n⠀⠀⠀⣴⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀\n⠀⠀⣾⣿⣿⣿⣿⣿⣶⣿⣯⣭⣬⣉⣽⣿⣿⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀\n⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n⢸⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠁\n ⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀',' ✧/ᐠ-ꞈ-ᐟ\ ', '/ᐠ –ꞈ –ᐟ\ ', '/ᐠ ̷  ̷𝅒 ̷‸ ̷𝅒 ̷ ᐟ\ﾉ' , '/ᐠ≗ᆽ≗ᐟ \ ', ' —ฅ/ᐠ. ̫ .ᐟ\ฅ —']
        catsoutput = random.choice(cats)
        myEmbed = discord.Embed(title= "Cat.", description =(catsoutput), color=0x89CFF0)
        await message.channel.send(embed=myEmbed)
        return

      elif user_message.lower() == "!hug":
        myEmbed = discord.Embed(title= "Hug", description =('Awww heres a hug :('), color=0x89CFF0)
        myEmbed.set_image(url="https://images-ext-1.discordapp.net/external/h4jJmHrow6Ir9uSQZ-2JMJ8srdnVj3HTE-hzyuHJK98/https/media.tenor.com/g8QItjXUFnwAAAPo/divz-divii.mp4")   
        await message.channel.send(embed=myEmbed)
        
      elif user_message.lower() == "!lofi":
        await message.channel.send(f'**Lofi:** https://open.spotify.com/playlist/4Zljhza4dQw7tkbPu7OrLW?si=54e8b7514e0f4458')
        return

      elif user_message.lower() == "!backgroundmusic":
        await message.channel.send(f'**Background:** https://open.spotify.com/playlist/39TMfjXqkYguKpXYWQdOqi?si=8813344b42cc43e7')
        return

      elif user_message.lower() == "!animemusic":
        await message.channel.send(f'**Anime Lofi**: https://open.spotify.com/playlist/4WtqLI6gaRFaWB4g6mDnAX?si=a636e8768a9d4e2d')
        return
      
      elif user_message.lower().find("!timer") != -1:
        stripTimeOnly = user_message.lower().replace("!timer","")
        timerstart = "Your timer has started..."
        await message.channel.send(timerstart)

        delay = int(stripTimeOnly) * 60
        messageTimer = "Hi, "+ message.author.mention + " your timer of " +  stripTimeOnly + " minute(s) has finished ฅ^•ﻌ•^ฅ"
        memes = ["https://media.discordapp.net/attachments/1038234778262052885/1038634417918333008/IMG_8351.png?width=678&height=688","https://media.discordapp.net/attachments/1038234778262052885/1038634425992355930/IMG_8353.png?width=719&height=688","https://media.discordapp.net/attachments/1038234778262052885/1038634426231435344/IMG_8354.png?width=714&height=688","https://bgr.com/wp-content/uploads/2015/06/funny-cat.jpg?quality=82&strip=all","https://64.media.tumblr.com/02bbb4aa0251620d47807551d93fc88d/tumblr_p6o1l4pB7c1u3abkpo1_1280.jpg"]
        randommemes = random.choice(memes)

        await asyncio.sleep(delay)
        await message.channel.send(messageTimer)
        await message.channel.send(randommemes)
        return

      #Reminder
      elif user_message.lower().find("!reminder") != -1:
        commandStripped = user_message.lower().replace("!reminder","")

        timerstart = "Your reminder has started..."
        await message.channel.send(timerstart)

        #time = (commandStripped[1])
        time = ""
        position = 1
        while commandStripped[position].isnumeric() == True:
          time = time + commandStripped[position]
          position += 1
    
        delay = int(time) * 60
        
        stripReminder = commandStripped.replace(time,"")

        messageReminder = "Hi, "+ message.author.mention + " your reminder of " + str(delay) + " second(s) has finished!! " + "\nThe reminder: " + stripReminder
        
        await asyncio.sleep(delay)
        await message.channel.send(messageReminder)
        return

client.run(TOKEN)
