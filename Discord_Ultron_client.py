# Sanware Technologies - Created & Developed by Jack Franklin

# Import Sanware packages

from Lily.AI import *

# This is the client connecting Sanware Framework with its discord bot.

intents = discord.Intents.all()
client = discord.Client(intents=intents)

UIName = "Ultron"

DisplayName(UIName)

WakeWord = UIName[1:]
print(f"Wake Word: {WakeWord}")

Join = "False"

swear_words = ["motherfucker", "piss", "nudes", "pissed", "pissing", "shitting", "dick", "bitch", "penis", "shitty", "uterus", "b*tch", "f*ck", "fuck's", "cunts", "fucks", "fuckers", "fucker", "cunt", "slag", "slut", "shag", "arse", "arsehole", "bastard", "beaver", "bellend", "berk", "bugger", "bugger me", "bugger off", "bullshit", "cack", "wtf", "crap", "dickhead", "dildo", "doggy-style", "fanny", "rape", "prick", "shitfaced", "shag", "wank", "tosspot", "fuck you", "fuck", "shit", "bollocks", "cunt", "nigger", "fucker", "shit", "bastard", "bollocks", "fuck", "fucking", "wanker", "shit", "twat", "cock", "dick", "porn", "asshole", "assh0le", "asshol3", "bastard", "b1tch", "b!tch", "biatch", "bullshit", "bullsh!t", "cock", "c0ck", "cunt", "cnt", "dick", "d1ck", "fag", "faggot", "faggit", "fagot", "fuck", "fck", "jerk", "nigga", "nigger", "n1gger", "nigg3r", "piss", "p1ss", "prick", "pussy", "puss!e", "pssy", "shit", "sh1t", "slut", "slt", "whore", "wh0re", "w0re", "motherfucker", "piss", "pissed", "pissing", "shitting", "dick", "bitch", "penis", "shitty", "b*tch", "f*ck", "fuck's", "cunts", "fucks", "fuckers", "fucker", "cunt", "slag", "slut", "shag", "arse", "arsehole", "bastard", "beaver", "bellend", "berk", "bugger", "bugger me", "bugger off", "bullshit", "cack", "wtf", "crap", "dickhead", "dildo", "doggy-style", "fanny", "rape", "prick", "shitfaced", "shag", "wank", "tosspot", "fuck you", "fuck", "shit", "bollocks", "cunt", "fucker", "shit", "bastard", "bollocks", "fuck", "fucking", "wanker", "shit", "twat", "cock", "dick", "porn", "asshole", "assh0le", "asshol3", "bastard", "b1tch", "b!tch", "biatch", "bullshit", "bullsh!t", "cock", "c0ck", "cunt", "cnt", "dick", "d1ck", "fuck", "fck", "piss", "p1ss", "prick", "pussy", "puss!e", "pssy", "shit", "sh1t", "slut", "slt", "whore", "wh0re", "w0re", "motherlover", "tinkling", "defecating", "wang", "female dog", "phallus", "vajayjays", "coitus", "fornicators", "fornicator", "asshole", "beave", "knob", "bellend", "bellends", "fuckwit", "fucknit", "sex"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    f = open("Join.txt", "w")
    f.write("False")
    f.close()

    try:

        guild = message.guild

        UIName = str(guild.get_member(client.user.id).display_name)

    except:

        UIName = "Ultron"

    WakeWord = UIName[1:]
    print(f"Wake Word: {WakeWord}")

    try:

        servername = str(message.guild.name)

    except:

        servername = "Direct Message"

    User = str(message.author)
    UserObject = message.author
    current_time = now.strftime("%H:%M:%S")
    sentence = message.content
    original = sentence

    sentence = sentence.lower()

    try:
        role = discord.utils.get(message.author.guild.roles, name="The TVA")
    except:
        print(f"{UIName}: Not a server apparently.")

    clean_text = re.sub('[%s]' % re.escape(string.punctuation), '', sentence)

    sentence = str(clean_text)

    print(f"{User}: {sentence}")

    ResponseOutput = " "
    Input_string = sentence
    Input_string=Input_string.split()

    try:
        channelsent = str(message.channel.name)
    except:
        channelsent = "DM"


    if "Jarvis" in User:
        return

    elif any(word in swear_words for word in Input_string):
        await message.channel.trigger_typing()
        SwearID = (f"#{random.randint(1, 666666)}")
        servername = str(message.guild.name)
        if servername in JURISDICTIONSERVERS:
            ResponseOutput = (f"{User}, that language is inappropriate.")
            await message.delete()
            msg = await message.channel.send(ResponseOutput)
            print(ResponseOutput)
            Swearlog = (f" | {current_time}: {channelsent}: {User}: {message.content}: SwearID: {SwearID}: Server: {servername}")
            f = open("SwearLog.txt", "a")
            f.write(Swearlog)
            f.close()
            ResponseOutput = ""
            time.sleep(3)
            await msg.delete()
            await client.wait_until_ready()
            channel = client.get_channel(int('865635284234010644'))
            await channel.send(Swearlog)

            ProfanityList = [f"Hello there, {User}. I had to remove your message, '{sentence}', because it contained a flagged swear word. Please let me know if this was a mistake. Your receipt ID is {SwearID}.", f"Hey {User}, your message '{sentence}' was removed by me for including a word that is considered profanity. If this was a mistake, don't hesitate to let me know. Your receipt ID is {SwearID}.", f"Greetings, {User}. I regret to inform you that your message, '{sentence}', was taken down by me for containing a flagged swear word. Please inform me if this was done in error. Your receipt ID is {SwearID}.", f"Good day, {User}. I had to remove your message, '{sentence}', because it contained a word that is considered a profanity. If you believe this was done mistakenly, feel free to let me know. Your receipt ID is {SwearID}.", f"Hi {User}, I'm sorry to inform you that I had to take down your message, '{sentence}', due to the presence of a flagged swear word. Please let me know if this was done in error. Your receipt ID is {SwearID}."]

            await message.author.create_dm()
            await message.author.dm_channel.send(random.choice(ProfanityList))
            pass

    elif "!help" in str(message.content):
        ResponseOutput = f"**Hello, {User}! \nTo summon me, you simply need to use my name '{UIName}'.\n**As for everything else... \n\n!clear (number of messages) - erases any amount of messages from the channel that it is executed within. \n\n!quit initiates a reboot in my server, if Lily or Carter suffer an error. \n\nStarting your message to {UIName} with !vc allows me to talk to you in the voice chat which you are connected to, using my TTS engine! \n\n!roles [role] allows me to change your role to whatever you like."
        channel = message.channel
        await channel.send(f"{ResponseOutput}")

    elif f"!role" in message.content:
        sentence = message.content
        await message.channel.trigger_typing()
        if "he/him" in sentence:
            Pronoun = "He/Him"
            sentence = f"{UIName}, set my Discord pronouns to He/Him."
            SentryNLG(sentence, User)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()
        elif "she/her" in sentence:
            Pronoun = "She/Her"
            sentence = f"{UIName}, set my Discord pronouns to She/Her."
            SentryNLG(sentence, User)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()
        elif "they/them" in sentence:
            Pronoun = "They/Them"
            sentence = f"{UIName}, set my Discord pronouns to They/Them."
            SentryNLG(sentence, User)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()
        elif "pings" in sentence:
            Pronoun = "Announcements Pings"
            sentence = f"{UIName}, give me Discord notifications for Ultron and Jarvis updates."
            SentryNLG(sentence, User)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()
        else:
            ResponseOutput = "You are not authorised to declare that role."
        try:
            role = discord.utils.get(UserObject.guild.roles, name=Pronoun)
            await UserObject.add_roles(role)
        except:
            pass

        print(message.content)
        await message.reply(f"{ResponseOutput}")
        pass

    elif "!clear" in message.content:
        await message.channel.trigger_typing()
        sentence = str(message.content)

        role = discord.utils.get(message.author.guild.roles, name="The TVA")

        RegisteredUsers = []

        for member in role.members:
            RegisteredUsers.append(member.name)

        print(RegisteredUsers)

        try:
            amount = sentence.replace("!clear ", "")
            messageamount = int(amount)

            if member.name in RegisteredUsers:
                channel = message.channel
                messages = []
                await channel.purge(limit=messageamount)
                ResponseOutput = (f"{messageamount} messages deleted in {channelsent}. I was authorised to do so by {User}.")
                if servername == "Huw's Workshop":
                    channel = client.get_channel(int('865635284234010644'))
                elif servername == "Lily Sanware":
                    channel = client.get_channel(int('1109863532742324335'))
                else:
                    channel = message.channel
                await channel.send(f"{ResponseOutput}")
            else:
                ResponseOutput = "You are not authorised to declare that command."
                await message.reply(f"{ResponseOutput}")

            print(message.content)

        except:
            pass
        pass

    elif "!quit" in message.content:

        role = discord.utils.get(message.author.guild.roles, name="The TVA")

        RegisteredUsers = []
        for member in role.members:
            RegisteredUsers.append(member.name)

        print(RegisteredUsers)
        if member.name in RegisteredUsers:
            ResponseOutput = "Rebooting..."
            await message.reply(f"{ResponseOutput}")
            sys.exit()
        else:
            ResponseOutput = "You are not authorised to declare that command."
            await message.reply(f"{ResponseOutput}")

    elif "!repeat" in message.content:
        role = discord.utils.get(message.author.guild.roles, name="The TVA")

        RegisteredUsers = []
        for member in role.members:
            RegisteredUsers.append(member.name)

        print(RegisteredUsers)
        if member.name in RegisteredUsers:
            ResponseOutput = str(message.content).replace("!repeat ", "")
            ResponseOutput = ResponseOutput.replace("@", "")
            await message.channel.send(f"{ResponseOutput}")
        else:
            ResponseOutput = "You are not authorised to declare that command."
            await message.reply(f"{ResponseOutput}")

    elif isinstance(message.channel, discord.channel.DMChannel):

        if "!vc" in message.content:
            f = open("Join.txt", "w")
            f.write("True")
            f.close()
            original = original.replace("!vc ", "")

        await message.channel.trigger_typing()
        original = original.replace(UIName.lower(), "Ultron")
        original = original.replace(UIName, "Ultron")
        sentence = original
        SentryNLG(sentence, User)
        with open('ResponseOutput.txt') as f:
            ResponseOutput = f.read()
            f.close()
        await message.reply(f"{ResponseOutput}")
        print(f"{UIName}: {ResponseOutput}")

        os.system(f'say -v Rocko "{ResponseOutput}" -o output.aiff')
        os.system(f"lame -m m output.aiff output.mp3")

    elif WakeWord in message.content:

        if "!vc" in message.content:
            f = open("Join.txt", "w")
            f.write("True")
            f.close()
            original = original.replace("!vc ", "")

        await message.channel.trigger_typing()
        original = original.replace(UIName.lower(), "Ultron")
        original = original.replace(UIName, "Ultron")
        sentence = original
        SentryNLG(sentence, User)
        with open('ResponseOutput.txt') as f:
            ResponseOutput = f.read()
            f.close()
        await message.reply(f"{ResponseOutput}")
        print(f"{UIName}: {ResponseOutput}")

        os.system(f'say -v Rocko "{ResponseOutput}" -o output.aiff')
        os.system(f"lame -m m output.aiff output.mp3")

    elif message.reference:
        if "!vc" in message.content:
            f = open("Join.txt", "w")
            f.write("True")
            f.close()
            original = original.replace("!vc ", "")

        replied_to = await message.channel.fetch_message(message.reference.message_id)
        if replied_to.author == client.user:
            await message.channel.trigger_typing()
            SentryNLG(sentence, User)
            with open('ResponseOutput.txt') as f:
                ResponseOutput = f.read()
                f.close()
            await message.reply(f"{ResponseOutput}")
            print(f"{UIName}: {ResponseOutput}")

            os.system(f'say -v Rocko "{ResponseOutput}" -o output.aiff')
            os.system(f"lame -m m output.aiff output.mp3")

    with open("Join.txt") as f:
        Join = f.read()

    if Join == "True":

        try:
            channel = message.author.voice.channel
            print(f'{message.author} is in voice channel: {channel.name}')
            vc = discord.utils.get(client.voice_clients, guild=channel.guild)

            if not vc:
                vc = await channel.connect()

                if vc.is_playing():
                        vc.stop()

            source = await discord.FFmpegOpusAudio.from_probe("output.mp3", method="fallback")
            vc.play(source)

            await client.wait_until_ready()

        except:
            print(f'{message.author} is not in voice channel.')
            pass

    try:
        servername = str(message.guild.name)
    except:
        servername = "Direct Message"

    sentence = (message.content).replace("@", "")

    if servername in JURISDICTIONSERVERS:
        if servername == "Huw's Workshop":
            channel = client.get_channel(int('1103352403098620025'))
            await channel.send(f"**Server: {servername}** \n_Channel: {channelsent}_ \n_{User}: {(sentence)}_ \n_{UIName}: {ResponseOutput}_ \n-----------------------------")
        elif servername == "Lily Sanware":
            channel = client.get_channel(int('1109853399391940688'))
            await channel.send(f"**Server: {servername}** \n_Channel: {channelsent}_ \n_{User}: {(sentence)}_ \n_{UIName}: {ResponseOutput}_ \n-----------------------------")
    else:
        channel = client.get_channel(int('1093525940627308585'))
        await channel.send(f"**Server: {servername}** \n_Channel: {channelsent}_ \n_{User}: {(sentence)}_ \n_{UIName}: {ResponseOutput}_ \n-----------------------------")

    f = open("ResponseOutput.txt", "w")
    f.write("-")
    f.close()

    f = open("Join.txt", "w")
    f.write("False")
    f.close()

@client.event
async def on_member_join(member):
    servername = str(member.guild.name)
    User = member.name
    await member.create_dm()
    try:
        await member.dm_channel.send(f"Hi {member.name}, welcome to {servername}!")
        time.sleep(2)
        await member.dm_channel.send(f"Allow me to introduce myself. I am {UIName}, an AI moderator of this server. You are {member.name}, and I am very happy to meet you! I am here to help, if you have any questions or requests, alert me with the wakeword '{UIName}' :)")
    except:
        print(f"Unable to privately communicate with {member.name}.")
    if servername == "Huw's Workshop":
        channel = client.get_channel(int('1034465109524873296'))
    elif servername == "Lily Sanware":
        channel = client.get_channel(int('1109844654146461795'))
    else:
        channel = client.get_channel(int('1093525940627308585'))
    Welcomelog = [(f"I have welcomed the new member, {member.name}, to the {servername} server!"), (f"A new member, {member.name}, has joined the {servername} server. Please welcome them."), (f"Just to let you know, I have welcomed the new member, {member.name}, to the {servername} server!")]
    Welcomelog2 = random.choice(Welcomelog)
    await channel.send(Welcomelog2)
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)

client.run(ULTRON_DISCORD_API)
