import random
import guessing_game_project.art3 as art3
print(art3.logo)
guess=random.randint(1,100)
level=str(input('''enter "easy" or "hard" '''))
if level=="hard":
    level=5
else:
    level=10
again=0
while again<level:
    number=int(input("Make a guess : "))
    if number>guess:
        print("Too High")
        print("Guess again")
        again+=1
    elif number<guess:
        print("Too Low")
        print("Guess again")
        again += 1
    else:
        print(f"U got it! The answer was {number}")
        break

if level==again:
    print("U lost")
    print("The answer was",guess)
    print("wanna play again")
