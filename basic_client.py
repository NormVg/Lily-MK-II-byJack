from Lily.AI import *

DisplayName(UIName)

Repeat = 1

while True:
    sentence = input(f"You: ")

    message_data = {"message": sentence}

    message_json = json.dumps(message_data)

    headers = {"Content-type": "application/json"}

    response = requests.post(url, data=message_json, headers=headers)

    DoFunction()

    with open("PersonalResponseOutput.txt") as f:
        ResponseOutput = f.read()

    print(f"{UIName}: {ResponseOutput}")
