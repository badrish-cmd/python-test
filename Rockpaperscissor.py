import random
def show():
    player_choice = input("enter rock or paper or scissor : ")
    rps=["rock","paper","scissor"]
    computer_choice = random.choice(rps)
    choices = {"xp": player_choice, "yc": computer_choice}
    return choices
def do(xp,yc):
    if xp == yc:
        return "IT IS A TIE"
    elif  xp == "rock":
        if yc == "scissor":
            return "ROCK SMASHES SCISSORS AND YOU WON!"
        else:
            return "PAPER CRUSHES ROCK AND YOU LOST!"
    elif  xp == "scissor":
        if yc == "paper":
            return "SCISSORS CUTS THE PAPER AND YOU WON!"
        else:
            return "ROCK BREAKS THE SCISSORS AND YOU LOST!"
    elif  xp == "paper":
        if yc == "rock":
            return "PAPER CRUSHES ROCK AND YOU WIN!"
        else:
            return "SCISSOR CUTS THE PAPER AND YOU LOST!"
    else:
     return "ENTERED VALUE IS WRONG"
choices=show()
z=do(choices["xp"],choices["yc"])
print(z)