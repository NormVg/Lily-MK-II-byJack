from Lily.AI import *

DisplayName(UIName)

WakeWord = UIName[2:]
print(f"Wake Word: {WakeWord}")

# This is the client connecting Sanware Framework with its discord bot.

discordintents = discord.Intents.all()
client = discord.Client(intents=discordintents)

# Program

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    User = str(message.author)

    if "Griot" in User:
        return
    if "Ultron" in User:
        return

    print(User)

    if WakeWord in message.content:
        await message.channel.trigger_typing()
        if User in AuthorisedUsers:
            if User == "Mechanic#4216":
                User = "Jack"
            ResponseOutput = " "
            print(message.content)
            sentence = message.content

            message_data = {"message": sentence}

            message_json = json.dumps(message_data)

            headers = {"Content-type": "application/json"}

            try:

                response = requests.post(url, data=message_json, headers=headers)

            except:

                print(f"{UIName}: Failure to connect to Lily server.")

            DoFunction()

            with open("PersonalResponseOutput.txt") as f:
                ResponseOutput = f.read()

            await message.channel.send(f"{ResponseOutput}")
        else:
            await message.channel.send(random.choice(UnauthorisedResponses))

        with open("PersonalResponseOutput.txt") as f:
            ResponseOutput = f.read()

        channel = message.author.voice.channel
        vc = discord.utils.get(client.voice_clients, guild=message.guild)

        if not vc:
            vc = await channel.connect()

            if vc.is_playing():
                vc.stop()

            os.system(f'say -v {VoiceChoice} "{ResponseOutput}" -o output.aiff')
            os.system(f"lame -m m output.aiff output.mp3")

            source = await discord.FFmpegOpusAudio.from_probe("output.mp3", method="fallback")
            vc.play(source)

    elif isinstance(message.channel, discord.channel.DMChannel):
        await message.channel.trigger_typing()
        if User in AuthorisedUsers:
            if User == "Mechanic#4216":
                User = "Jack"
            ResponseOutput = " "
            print(message.content)
            sentence = message.content

            message_data = {"message": sentence}

            message_json = json.dumps(message_data)

            headers = {"Content-type": "application/json"}

            try:

                response = requests.post(url, data=message_json, headers=headers)

            except:

                print(f"{UIName}: Failure to connect to Lily server.")

            DoFunction()

            with open("PersonalResponseOutput.txt") as f:
                ResponseOutput = f.read()

            await message.channel.send(f"{ResponseOutput}")
        else:
            await message.channel.send(random.choice(UnauthorisedResponses))

        channel = client.get_channel(int('723270333523558455'))
        vc = discord.utils.get(client.voice_clients, guild=channel.guild)

        if not vc:
            vc = await channel.connect()

            if vc.is_playing():
                    vc.stop()

        os.system(f'say -v {VoiceChoice} "{ResponseOutput}" -o output.aiff')
        os.system(f"lame -m m output.aiff output.mp3")

        source = await discord.FFmpegOpusAudio.from_probe("output.mp3", method="fallback")
        vc.play(source)

client.run(PERSONAL_DISCORD_API)
