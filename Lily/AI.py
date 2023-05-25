print(" _     ___ _  __   __     _    ___ ")
print("| |   |_ _| | \\ \\ / /    / \\  |_ _|")
print("| |    | || |  \\ V /    / _ \\  | | ")
print("| |___ | || |___| |    / ___ \\ | | ")
print("|_____|___|_____|_|   /_/   \\_\\___|")

from Lily.libraries import *
from Lily.nltk_utils import *
from Lily.model import *
from Lily.functions import *
from ai_config import *

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# "As you wish.", "Sure thing.", "Absolutely!", "Of course.", "No problem.", "Certainly!", "That sounds good to me.", "Consider it #done.", "My pleasure.", "You got it!", "Happy to help.", "I'll make it happen.", "Without a doubt.", "Right away!", "It would be #my honor.", "I'm on it.", "Very well.", "Gladly!", "I'd be happy to.", "Okay, great.", "No trouble at all.", "You can count on #me.", "Affirmative.", "As you command.", "Certainly, sir/madam.", "It's a pleasure to serve you."

def DisplayName(UIName):
    ascii_art = text2art(f"{UIName}")
    print(ascii_art)

def LilyAI(sentence, intents):

    system_times = os.times()
    current_time = system_times[4]
    current_time_str = time.ctime(current_time)
    print("Current time: ", current_time_str)

    sentence = str(sentence)
    original = sentence

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    while True:

        if sentence == "quit":
            break

        type(sentence)

        if type(sentence) == str:
            sentence = tokenize(sentence)
        else:
            return

        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        ConfidenceRate = prob.item()

        if prob.item() > 0.85:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    AIFunctions(User, UIName, intent, sentence, original)
        else:
            pass

        f = open("Confidence.txt", "w+")
        f.write(f"Confidence: {ConfidenceRate}")
        f.close()

        try:

            with open("PersonalResponseOutput.txt") as f:
                ResponseOutput = f.read()
                f.close()

                print(f"{UIName}: {ResponseOutput} | Confidence Rate: {ConfidenceRate}")
        except:
            pass

def SentryNLG(sentence, User):

    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
        }, data=json.dumps({
        "text": f"{sentence}",
        "key": f"{CARTER_ULTRON_API}",
        "playerId": f"{User}"
        }))

    RawResponse = response.json()
    Response = RawResponse["output"]
    FullResponse = Response["text"]
    ResponseOutput = FullResponse
    User = str(User)

    ResponseOutput = ResponseOutput.replace("Unknown person", User)
    ResponseOutput = ResponseOutput.replace("Unknown Person", User)
    ResponseOutput = ResponseOutput.replace("unknown person", User)
    ResponseOutput = ResponseOutput.replace("Player", User)
    ResponseOutput = ResponseOutput.replace("player", User)
    f = open("ResponseOutput.txt", "w")
    f.write(f"{ResponseOutput}")
    f.close()

    ResponseType = "Generated"

    gail = open("ResponseType.txt", "w")
    gail.write(ResponseType)
    gail.close()

def PersonalNLG(original, User):

    response = requests.post("https://api.carterlabs.ai/chat", headers={
    "Content-Type": "application/json"
    }, data=json.dumps({
    "text": f"{original}",
    "key": f"{CARTER_GRIOT_API}",
    "playerId": f"{User}"
    }))

    RawResponse = response.json()
    Response = RawResponse["output"]
    FullResponse = Response["text"]
    ResponseOutput = FullResponse
    User = str(User)

    ResponseOutput = ResponseOutput.replace("Unknown person", User)
    ResponseOutput = ResponseOutput.replace("Unknown Person", User)
    ResponseOutput = ResponseOutput.replace("unknown person", User)
    ResponseOutput = ResponseOutput.replace("Player", User)
    ResponseOutput = ResponseOutput.replace("player", User)

    f = open("PersonalResponseOutput.txt", "w")
    f.write(f"{ResponseOutput}")
    f.close()

def AIFunctions(User, UIName, intent, sentence, original):
    system_times = os.times()
    current_time = system_times[4]
    current_time_str = time.ctime(current_time)
    AlreadyDone = 0
    ResponseOutput = "null"
    InstantResponses = ["sleep-monitor", "quit-reboot", "prom", "open-youtube", "open-gmail", "open-outlook", "open-twitter", "open-carter", "open-ebay", "open-github", "light-on", "light-off", "maps", "play-music", "pause-music", "skip-music", "open-disney+", "google", "open-iplayer", "open-google", "open-amazon", "volume", "mute"]
    ResponseType = "Fixed"

    if "sky-pause-play" == intent["tag"]:
        ResponseOutput = (f"{random.choice(intent['responses'])}")
        SkyPlay(SkyClient)

    elif "sky-power" == intent["tag"]:
        ResponseOutput = (f"{random.choice(intent['responses'])}")
        SkyPower(SkyClient)

    elif "time" == intent["tag"]:
        current_time = now.strftime("%H:%M")
        ResponseOutput = (f"{random.choice(intent['responses'])}{current_time_str}")
        ResponseType = "Partially fixed"

    elif "current-music" == intent["tag"]:
        ReadSpotify()
        with open("current_track.txt") as f:
            TrackOutput = f.read()
            TrackOutput = TrackOutput.replace("Track: ", "")
            TrackOutput = TrackOutput.replace("Artist: ", "by ")
            ResponseOutput = (f"{random.choice(intent['responses'])}{TrackOutput}")
        ResponseType = "Partially fixed"

    elif "morning-routine" == intent["tag"]:
        current_time = now.strftime("%H:%M")
        ResponseOutput = (f"{random.choice(intent['responses'])}{current_time_str}. I will now play your Spotify playlist and lights are turned on.")
        ResponseType = "Partially fixed"

    elif intent["tag"] in InstantResponses:
        ResponseOutput = (f"{random.choice(intent['responses'])}")

    else:
        PersonalNLG(original, User)
        AlreadyDone = 1
        ResponseType = "Generated"

    if AlreadyDone == 1:
        pass
    else:
        f = open("PersonalResponseOutput.txt", "w")
        f.write(f"{ResponseOutput}")
        f.close()

    PreFunction = intent["tag"]

    f = open("Function.txt", "w")
    f.write(f"{PreFunction}")
    f.close()

    et = open("Sentence.txt", "w")
    et.write(original)
    et.close()

    gail = open("ResponseType.txt", "w")
    gail.write(ResponseType)
    gail.close()

    if "quit-reboot" == intent["tag"]:
        sys.exit()

def DoFunction():
    with open("Function.txt") as f:
        Function = f.read()

    with open("PersonalResponseOutput.txt") as f:
        ResponseOutput = f.read()

    print(f"{UIName}: Predicted category is {Function}")

    with open("Sentence.txt") as f:
        sentence = f.read()

    if Function == "volume":
        sentence = str(sentence)
        setting = (sentence.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}))
        setvol(setting)

    elif Function == "open-amazon":
        Amazon()

    elif Function == "open-iplayer":
        iPlayer()

    elif Function == "open-disney+":
        DisneyPlus()

    elif Function == "google":
        Google()

    elif Function == "light-on":
        try:
            LightOn()
        except:
            ResponseOutput = "Light activation unsuccessful"
            f = open("PersonalResponseOutput.txt", "w")
            f.write(ResponseOutput)
            f.close()


    elif Function == "light-off":
        try:
            LightOff()
        except:
            ResponseOutput = "Light deactivation unsuccessful"
            f = open("PersonalResponseOutput.txt", "w")
            f.write(ResponseOutput)
            f.close()


    elif Function == "atom":
        NewCode()

    elif Function == "word-doc":
        NewDocument()

    elif Function == "morning-routine":
        MorningRoutine()

    elif Function == "play-music":
        PlayMusic()

    elif Function == "pause-music":
        PauseMusic()

    elif Function == "skip-music":
        SkipMusic()

    elif Function == "maps":
        GoogleMaps()

    elif Function == "open-youtube":
        YouTube()

    elif Function == "open-gmail":
        Gmail()

    elif Function == "open-outlook":
        Outlook()

    elif Function == "open-twitter":
        Twitter()

    elif Function == "open-carter":
        Carter()

    elif Function == "open-ebay":
        eBay()

    elif Function == "open-github":
        GitHub()

    elif Function == "quit-reboot":
        sys.exit()

    elif Function == "sleep-monitor":
        sleepPC()

    f = open("Function.txt", "w")
    f.write(f"Predicted category is '{Function[:1]}/{Function[1:]}'")
    f.close()

    f = open("Memory.txt", "a")
    f.write("\n\n ")
    f.write(f"\n{sentence}")
    f.write(f"\n{ResponseOutput}")
    f.close()


def VoiceCommand(UIName, User, VoiceChoice):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    seconds = 3.8
    filename = "audio.wav"
    threshold = 5000  # adjust as needed

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Listening')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Wait for the user to start speaking
    while True:
        data = stream.read(chunk)
        signal = np.frombuffer(data, dtype=np.int16)
        amplitude = np.max(signal)
        if amplitude > threshold:
            break

    print('Recording')

    f = open("VAD.txt", "w")
    f.write("Speech Detected.")
    f.close()

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print(f'{UIName}: I have finished recording.')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    f = open("VAD.txt", "w")
    f.write("Thinking...")
    f.close()

    speech(UIName, User, VoiceChoice)

def speech(UIName, User, VoiceChoice):

    rate, data = wavfile.read("audio.wav")
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write("cleaned_audio.wav", rate, reduced_noise)

    model = whisper.load_model("base.en")
    result = model.transcribe("cleaned_audio.wav")
    sentence = result["text"]

    print(f"{User}: {sentence}")

    sentence = str(sentence)

    message_data = {"message": sentence}

    message_json = json.dumps(message_data)

    headers = {"Content-type": "application/json"}

    response = requests.post(url, data=message_json, headers=headers)

    ResponseOutput = response.text

    f = open("PersonalResponseOutput.txt", "w")
    f.write(ResponseOutput)
    f.close()

    f = open("VAD.txt", "w")
    f.write(f"Listening...")
    f.close()
