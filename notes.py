import datetime
from listen import *

def write_note(notes_name):
    try:
        
        note = listen()
        file = open('{}.txt'.format(notes_name), 'w')
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)    
        file.close()
        
    except Exception as e:
        print("An error occurred:", str(e))

def open_note(open_name):
    try:
        file = open('{}.txt'.format(open_name), 'r')
        while True:
            close = listen()
            if any(keyword in close for keyword in ["close", "exit", "bin"]):
                file.close()
                break
        
    except Exception as e:
        print("An error occurred:", str(e))

