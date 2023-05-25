from Lily.AI import *

DisplayName(UIName)

while True:
    try:
        VoiceCommand(UIName, User, VoiceChoice)
        DoFunction()
        
        with open('PersonalResponseOutput.txt') as f:
            ResponseOutput = f.read()

        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
        os.remove("PersonalResponseOutput.txt")
    except:
        pass
