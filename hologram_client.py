import tkinter as tk
import tkinter.font as tkFont
from ai_config import *
from Lily.AI import *

root = tk.Tk()

root.title(f"{UIName}")
root.configure(background="black")
root.attributes('-alpha',0.75)
root.resizable(width=True, height=True)

# --- Text output & time

textbox=tk.Text(root, font=("Helvetica", 36), background="lightblue", fg="black")
textbox.place(x=540,y=270,width=840,height=784)

TimeBox=tk.Text(root, font=("Helvetica", 104), background="darkblue")
TimeBox.place(x=540,y=60,width=1295,height=150)
TimeBox.tag_configure("center", justify="center")

# --- Four blocks

GLabel_795=tk.Label(root)
GLabel_795["bg"] = "black"
ft = tkFont.Font(family='Franklin Gothic Medium',size=66)
GLabel_795["font"] = ft
GLabel_795["fg"] = "#ffffff"
GLabel_795["justify"] = "center"
GLabel_795["text"] = f"{UIName.upper()}"
GLabel_795["relief"] = "sunken"
GLabel_795.place(x=70,y=60,width=438,height=150)

ResponseBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
ResponseBox.place(x=70,y=270,width=438,height=150)

ConfidenceBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
ConfidenceBox.place(x=70,y=480,width=438,height=150)

FunctionBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
FunctionBox.place(x=70,y=690,width=438,height=150)

VadBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
VadBox.place(x=70,y=900,width=438,height=150)

RamBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
RamBox.place(x=1412, y=270, width=438, height=150)

SpotifyBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
SpotifyBox.place(x=1412, y=480, width=438, height=150)

Empty1=tk.Text(root, font=("Helvetica", 30), background="darkblue")
Empty1.place(x=1412, y=690, width=438, height=150)

NoteBox=tk.Text(root, font=("Helvetica", 30), background="darkblue")
NoteBox.place(x=1412, y=900, width=438, height=150)

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except:
        return ''

while True:
    memory_contents = read_file('Memory.txt').upper()
    ConfidenceLevel = read_file('Confidence.txt').upper()
    Function = read_file('Function.txt').upper()
    VADStatus = read_file('VAD.txt').upper()
    ResponseType = read_file('ResponseType.txt').upper()
    Usage = read_file('usage.txt').upper()
    Music = read_file('current_track.txt').upper()

    Function = Function.replace("/", "")

    paragraphs = memory_contents.split('\n\n')[-4:]
    Music = Music.split('\n\n')[-2:]


    current_time = time.ctime()
    current_time_struct = time.strptime(current_time)
    minutes = current_time_struct.tm_min
    hours = current_time_struct.tm_hour
    day = current_time_struct.tm_wday
    month = current_time_struct.tm_mon
    day_of_month = current_time_struct.tm_mday

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months_of_year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    current_time_str = (f"{days_of_week[day]} {day_of_month} {months_of_year[month-1]} {hours}:{minutes}")

    if "Saturday" not in current_time_str and "Sunday" not in current_time_str and "06:25:" in current_time_str:
        ResponseOutput = f"Good morning. It is currently {current_time_str}. I will now play your Spotify music and run the morning routine."
        textbox.delete('1.0', tk.END)
        textbox.insert(tk.END, str(ResponseOutput))

        try:
            maxvol()
            PlayMusic()
            LightOn()

        except:
            pass

        print("e")

        textbox.delete('1.0', tk.END)
        textbox.insert(tk.END, "ALARM!")

        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
        print("")
        print("")
        print(ResponseOutput)
        print("Current time: ", current_time_str)
        time.sleep(60)

    else:
        textbox.delete('1.0', tk.END)
        textbox.insert('1.0', '\n\n'.join(paragraphs))
        textbox.yview_moveto(1.0)

        TimeBox.delete('1.0', tk.END)
        TimeBox.insert(tk.END, str(f" {current_time_str}").upper())

        ConfidenceBox.delete('1.0', tk.END)
        ConfidenceBox.insert(tk.END, str(ConfidenceLevel))

        FunctionBox.delete('1.0', tk.END)
        FunctionBox.insert(tk.END, str(Function))

        ResponseBox.delete('1.0', tk.END)
        ResponseBox.insert(tk.END, str(ResponseType))

        VadBox.delete('1.0', tk.END)
        VadBox.insert(tk.END, str(VADStatus))

        RamBox.delete('1.0', tk.END)
        RamBox.insert(tk.END, str(Usage))

        SpotifyBox.delete('1.0', tk.END)
        SpotifyBox.insert(tk.END, '\n\n'.join(Music))

        root.update()
        root.after(1000)

root.mainloop()
