import random
#  Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer choose r
    elif comp == 'r':
        if you=='p':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer choose p
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer choose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Comp Turn: rock(r) paper(p) secissor(s)")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: rock(r) paper(p) secissor(s)")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a Tie!\n")
    
elif a:
    print("You Win!\n")
    
else:
    print("You Lose!\n")
   