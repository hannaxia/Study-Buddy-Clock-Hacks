import discord
import asyncio 
import random
from discord.ext import commands
from asyncio import sleep as s

# from timer import Timer

TOKEN = 'MTAzODI0OTUyNzkwNTM2MjAxMA.GfjAVD.Xyr2IWS8UewQXj_5_fYGeszkH-GWm7eLLR_QrE'
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
          myEmbed = discord.Embed(title="Bot Commands", description="Here are the commands for this bot!", color=0x89CFF0)
          myEmbed.add_field(name="Motivation", value="Use these commands to motivate you to study: \n `!motivation, !quotes, !roast`", inline=False)
          myEmbed.add_field(name="Music", value="We'll give you study music/playlist reccomendations! \n `!lofi, !anime, !backgroundmusic`", inline=False)
          myEmbed.add_field(name="Ressources", value="Commands for helpful study ressources: \n `!studyhelp, !math, !sci, !art, !cs`", inline=False)
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


        # if message.content.startswith('!studylinks'):
        #   # await message.channel.send('Say hello!')

        #   def check(m):
        #     return m.content == 'hello' and m.channel == channel

        #   msg = await client.wait_for('message',check=check)
        #   await channel.send('Hello {.author}!'.format(msg))
      
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
      
 #{author.mention}
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
              
              
      # elif user_message.lower() == "!timerp":
    
        # async def timer(self, ctx, timeInput):
        #   try:
        #       try:
        #           time = int(timeInput)
        #       except:
        #           convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
        #           time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        #       if time > 86400:
        #           await ctx.send("I can't do timers over a day long")
        #           return
        #       elif time <= 0:
        #           await ctx.send("Timers don't go into negatives :/")
        #           return
        #       elif time >= 3600:
        #           message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
        #       elif time >= 60:
        #           message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
        #       elif time < 60:
        #           message = await ctx.send(f"Timer: {time} seconds")
        #       while True:
        #           try:
        #               await asyncio.sleep(5)
        #               time -= 5
        #               if time >= 3600:
        #                   await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
        #               elif time >= 60:
        #                   await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
        #               elif time < 60:
        #                   await message.edit(content=f"Timer: {time} seconds")
        #               if time <= 0:
        #                 await message.edit(content="Ended!")
        #                 await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
        #                 break
        #           except:
        #               break
        #   except:
        #       await ctx.send(f"Alright, first you gotta let me know how I'm gonna time {timeInput}....")





# attempted timer muahaha (will not work)
# @client.event
# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#         if user_message.lower() == '!start':
#             async def timer(self, ctx, timeInput):
#                 try:
#                     try:
#                         time = int(timeInput)
#                     except:
#                         convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
#                         time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
#                     if time > 86400:
#                         await ctx.send("I can\'t do timers over a day long")
#                         return
#                     if time <= 0:
#                         await ctx.send("Timers don\'t go into negatives :/")
#                         return
#                     if time >= 3600:
#                         message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
#                     elif time >= 60:
#                         message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
#                     elif time < 60:
#                         message = await ctx.send(f"Timer: {time} seconds")
#                     while True:
#                         try:
#                             await asyncio.sleep(5)
#                             time -= 5
#                             if time >= 3600:
#                                 await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
#                             elif time >= 60:
#                                 await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
#                             elif time < 60:
#                                 await message.edit(content=f"Timer: {time} seconds")
#                             if time <= 0:
#                                 await message.edit(content="Ended!")
#                                 await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
#                                 break
#                         except:
#                             break
#                 except:
#                     await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#         if user_message.lower() == '!start':
#             async def start_timer(ctx):
#                 start_work_em = discord.Embed(title="Time to start working!", color=0x89CFF0)
#                 await ctx.send(embed = start_work_em)

#                 timer.start()
#                 while timer.get_status():
#                     await asyncio.sleep(1)
#                     if timer.get_ticks() >= 10:
#                         timer.stop()

#                     start_play_em = discord.Embed(title='Time to start your break!', color=0x89CFF0)
#                     await ctx.send(embed = start_work_em)

# async def on_message(message):
#     user_message = str(message.content)
#     if user_message.lower() == '!stop':
#         general_channel = client.get_channel(1025831217511280782)
#         async def stop_timer(ctx):
#             stop_timer_em = discord.Embed(title='Timer has stopped!', color=0x89CFF0)
#             await ctx.send(embed = stop_timer_em)
#             timer.stop()


# @client.event
# if user_message.lower() == '!start':
  # async def timer(self, ctx, timeInput):
  #     try:
  #         try:
  #             time = int(timeInput)
  #         except:
  #             convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
  #             time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
  #         if time > 86400:
  #             await ctx.send("I can't do timers over a day long")
  #             return
  #         if time <= 0:
  #             await ctx.send("Timers don't go into negatives :/")
  #             return
  #         if time >= 3600:
  #             message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
  #         elif time >= 60:
  #             message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
  #         elif time < 60:
  #             message = await ctx.send(f"Timer: {time} seconds")
  #         while True:
  #             try:
  #                 await asyncio.sleep(5)
  #                 time -= 5
  #                 if time >= 3600:
  #                     await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
  #                 elif time >= 60:
  #                     await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
  #                 elif time < 60:
  #                     await message.edit(content=f"Timer: {time} seconds")
  #                 if time <= 0:
  #                     await message.edit(content="Ended!")
  #                     await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
  #                     break
  #             except:
  #                 break
  #     except:
  #         await ctx.send(f"Alright, first you gotta let me know how I'm gonna time {timeInput}....")

#timer command
# class TimerStatus(enum):
#     Initialized = 1
#     Running = 2
#     Stopped = 3
#     Expired = 4
# class Timer:
#     def init (self):
#         self.status = TimerStatus.Initialized
#         self.ticks = 0
        
#     def get_status(self):
#         return self.status
        
#     def start (self, max_ticks):
#         self.max_ticks = max_ticks
#         self.status = TimerStatus.Running
#         self.ticks = 0
    
#     def stop (self):
#         self.status = TimerStatus.Stopped

#     def get_ticks (self):
#         return self.ticks
    
#     def tick (self):
#         self.ticks == 1
#         if self.get_ticks() >= self.max_ticks:
#             self.status = TimerStatus.Expired





      # elif user_message.lower() == '!hi'
      # await message.channel.send
      #   return

# @client.event
# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#       if user_message.lower() == '!quotes':
#         general_channel = client.get_channel(1038234778262052885)
#         myEmbed = discord.Embed(title="They're not cringe I promise", description=(output), color=0x89CFF0)

#         await general_channel.send(embed=myEmbed)

# @client.event
# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#       if user_message.lower() == '!motivation':
#         words = ["studying = money = happiness","no bitches but if u ace that test, you will have money and thus get bitches - elaine","you want to beat that one really annoying classmate? get a higher mark than them >:)","studying is hard. but just do it, it's not as hard as jumping off a cliff.","if you studied right now ur mom would be proud of you"]
#         output = random.choice(words)
#         general_channel = client.get_channel(1038234778262052885)
#         myEmbed = discord.Embed(title="I'm rooting for you!!!", description=(output), color=0x89CFF0)

#         await general_channel.send(embed=myEmbed)

# @client.event
# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#       if user_message.lower() == '!quotes':
#         words2 = ["insert cringy quote here"]
#         output2 = random.choice(words2)
#         general_channel = client.get_channel(1038234778262052885)
#         myEmbed = discord.Embed(title="They're not cringe I promise", description=(output2), color=0x89CFF0)

#         await general_channel.send(embed=myEmbed)


# client.event
# async def on_message(message):
#     user_message = str(message.content)
#     if message.channel.name == 'general':
#       if user_message.lower() == '!roast':
#         words3 = ['stop being lazy and procrasting >:(','ur mom would not be proud of you rn','you no study, asian parents MAD D:','get your crap together and study for once','remember how awful you felt when you did bad on that one test','I am disappointed in you. Jk unless you study ;)']
#         output3 = random.choice(words3)
#         general_channel = client.get_channel(1038234778262052885)
#         myEmbed = discord.Embed(title="I'm sorry in advance", description=(output3), color=0x89CFF0)

#         await general_channel.send(embed=myEmbed)



# @client.event   
# async def on_message(message):
#   print("hi")

client.run(TOKEN)
