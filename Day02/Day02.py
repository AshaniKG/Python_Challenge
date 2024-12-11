num = 7
i = 1 

print ("HI THERE..! \nWELCOME TO GUESSING GAME..\n")

name = input ("ENTER YOUR NAME: ")

print("\nHI "+name+ "!! \n\nHERE IS YOUR HINT: The number is less than 10. \nNOW START GUESSING..!\n")

guess = int (input ("THE NUMBER IS: "))

while guess != num:
    guess = int (input ("ANSWER IS WRONG! TRY AGAIN: "))
    i += 1 

    if guess == num:
        print ("CONGRADULATIONS..!!!  YOU WON AFTER",i,"TRIES")
        break
    
