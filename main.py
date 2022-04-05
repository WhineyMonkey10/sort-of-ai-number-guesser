import random
import time
import os

# Main
print("Notice: If you get an error about the 'random' module, please run 'pip install random' in the terminal. Also, if you get an error about cls only working in windows, change cls in line 11 to clear. ")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
           command = 'cls' 
    os.system(command)

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins),sec)

log = []

numberinput = int(input("How big do you want the range of the number to be: "))
number2guess = random.randint(1, numberinput)
show_guesses = input("Do you want it to log all the guesses (spam likely, it will also greatly reduce performance) y/n: ")
guesses = 0
while True:
    start_time = time.time()
    computer_guess = random.randint(1, numberinput)
    if show_guesses == 'y':
        log.append(computer_guess)
    if computer_guess == number2guess:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(f"The computer has guessed the number! \nIt took {guesses + 1} guesses and it took {time_convert(time_lapsed)} to find. The number was {number2guess}.")
        if show_guesses == 'y':
            printlog = input("Since you wanted to log the guesses, do you want to see the log? y/n: ")
            if printlog == "y":
             print(log)
        input("Press enter to exit")
        clearConsole()
        break
        
    guesses += 1