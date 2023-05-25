from Lily.AI import *

from tkinter import *
import tkinter.font as tkFont

DisplayName(UIName)


def send_message():
    sentence = messageWindow.get("1.0", "end-1c")

    messageWindow.delete("1.0", "end")

    message_data = {"message": sentence}

    message_json = json.dumps(message_data)

    headers = {"Content-type": "application/json"}

    try:

        response = requests.post(url, data=message_json, headers=headers)

        ResponseOutput = response.text

        chatWindow.insert("end", f"\n{User}: {sentence}")
        chatWindow.insert("end", f"\n{UIName}: {ResponseOutput}")
        chatWindow.see("end")

    except:
        print(f"{UIName}: Connection to the Lily server failed.")

    with open("Confidence.txt") as f:
        Confidence = f.read()

    with open("Function.txt") as f:
        Function = f.read()

    ConfidenceBox.delete("1.0", "end")
    ConfidenceBox.insert("end", f"{Confidence}")

    FunctionBox.delete("1.0", "end")
    FunctionBox.insert("end", f"{Function}")

    DoFunction()

    with open("PersonalResponseOutput.txt") as f:
        ResponseOutput = f.read()

    time.sleep(0.1)
    os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')

def StartVC():
    VoiceCommand(UIName, User, VoiceChoice)
    DoFunction()

    with open("PersonalResponseOutput.txt") as f:
        ResponseOutput = f.read()

    os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')

    with open("Confidence.txt") as f:
        Confidence = f.read()

    with open("Function.txt") as f:
        Function = f.read()

    Function = Function.replace("/", "")
    Function = Function.replace("Predicted category is ", "")
    Function = Function.replace("'", "")

    ConfidenceBox.delete("1.0", "end")
    ConfidenceBox.insert("end", f"{Confidence}")

    FunctionBox.delete("1.0", "end")
    FunctionBox.insert("end", f"{Function}")

    with open("PersonalResponseOutput.txt") as f:
        ResponseOutput = f.read()

    with open("Sentence.txt") as f:
        sentence = f.read()

    chatWindow.insert("end", f"\n{User}: {sentence}")
    chatWindow.insert("end", f"\n{UIName}: {ResponseOutput}")
    chatWindow.see("end")

# Create tkinter window
root = Tk()

root.title(f"{UIName.upper()}")
#setting window size
width=407
height=183
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

root.attributes('-alpha',0.85)

main_menu = Menu(root)

file_menu = Menu(root)
file_menu.add_command(label="New...")
file_menu.add_command(label="Save as...")
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")

root.config(menu=main_menu)

chatWindow = Text(root, bd=1, bg="black", width=50, height=8, fg="yellow")
chatWindow.place(x=10,y=20,width=224,height=90)

messageWindow = Text(root, bg="lightblue", width=30, height=4, fg="black")
messageWindow.place(x=10,y=120,width=224,height=53)

FunctionBox = Text(root, bg="black", width=30, height=4, fg="cyan")
FunctionBox.place(x=250,y=70,width=142,height=30)

ConfidenceBox = Text(root, bg="black", width=30, height=4, fg="cyan")
ConfidenceBox.place(x=250,y=30,width=142,height=30)

SpeakButton=tk.Button(root)
SpeakButton["bg"] = "#a78d8d"
ft = tkFont.Font(family='Helvetica',size=14)
SpeakButton["font"] = ft
SpeakButton["fg"] = "#000000"
SpeakButton["justify"] = "center"
SpeakButton["text"] = "Speak"
SpeakButton.place(x=320,y=120,width=74,height=52)
SpeakButton["command"] = StartVC

SendButton=tk.Button(root)
SendButton["bg"] = "#a99b9b"
ft = tkFont.Font(family='Helvetica',size=14)
SendButton["font"] = ft
SendButton["fg"] = "#000000"
SendButton["justify"] = "center"
SendButton["text"] = "Send"
SendButton.place(x=240,y=120,width=74,height=52)
SendButton["command"] = send_message

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

messageWindow.bind("<Return>", lambda event: send_message())

root.mainloop()
