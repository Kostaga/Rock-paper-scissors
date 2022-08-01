#def
import random
def answers(answer1,answer2):
    global p1
    global p2
    if (answer1==1):
        if (answer2==2):
            print("Player 1 wins")
            p1+=1

        elif (answer2==1):
            print("It's a tie!")
        else:
            print("Player 2 Wins")
            p2+=1

    elif (answer1==2):
        if (answer2==1):
            print("Player 1 wins")
            p1 += 1
        elif (answer2==2):
            print("It's a tie!")
        else:
            print("Player 2 wins")
            p2 += 1
    elif (answer1==3):
        if (answer2 == 2):
            print("Player 1 wins")
            p1 += 1
        elif(answer2==3):
            print("It's a tie!")
        else:
            print("Player 2 wins")
            p2 += 1

    return answer1,answer2

#main
p1=0
p2=0
flag = True
numbers = [1,2,3]
names = ["Rock","Paper","Scissors"]
while flag:
    player1 = int(input("Player 1,choose Rock(1) Paper(2) or Scissors(3): "))
    while (player1>3 or player1<1):
        player1 = int(input("Wrong answer(1/2/3).Player 1,choose Rock(1) Paper(2) or Scissors(3): "))
    player2 = random.randint(1,3)
    answer = answers(player1, player2)
    for i in range(len(numbers)):
        if (numbers[i] == player1):
            player1=names[i]
        if (numbers[i] == player2):
            player2=names[i]
    print(f"Player 1 choice: {player1} \nPlayer 2 choice {player2}")

    replay = input("Would you like to play again?(Y/N) :")
    while (replay not in ["Y",'y','N','n']):
        replay = input("Would you like to play again?(Y/N) :")
    if (replay in ['n','N']):
        flag= False

print("Game over")
print("Player score: {} \nComputer score: {}".format(p1,p2))


