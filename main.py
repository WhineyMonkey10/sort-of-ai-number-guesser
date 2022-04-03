import random
import time

# Main

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins),sec)

number2guess = random.randint(1, 1000000)
show_guesses = input("Do you want it to log all the guesses (spam likely) y/n: ")

guesses = 0
while True:
    start_time = time.time()
    computer_guess = random.randint(1, 1000000)
    if show_guesses == 'y':
        print(computer_guess)
    if computer_guess == number2guess:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(f"The computer has guessed the number! \nIt took {guesses + 1} guesses and it took {time_convert(time_lapsed)} to find. The number was {number2guess}.")
        input("Press enter to exit")
        break
    guesses += 1