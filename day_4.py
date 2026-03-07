# ROCK , PAPER AND SCISSORS
import random
choice=int(input("What do u choose? Type 0 for rock,1 for paper or 2 for scissors."))
rock=(
        """
        ROCK
        |  _______
       ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
paper=("""
       PAPER 
        _______
    ---'    ____)____
                ______)
                _______)
                _______)
       ---.__________)
    """)
scissor=("""
         SCISSOR
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
game=[rock,paper,scissor]
c_choice=random.choice(game)

if choice==0:
    print("Your choice")
    print(rock)
    if c_choice==game[0]:
        print("Computer chose")
        print(c_choice)
        print("Both chose same")
    elif c_choice==game[1]:
        print("Computer chose")
        print(c_choice)
        print("Computer won")
    elif c_choice==game[2]: 
        print("Computer chose")
        print(c_choice)
        print("you won")

   
elif choice==1:
    print("Your choice")
    print(paper)
    if c_choice==game[1]:
        print("Computer chose")
        print(c_choice)
        print("its a draw")
    elif c_choice==game[2]:
        print("Computer chose")
        print(c_choice)
        print("Computer won")
    elif c_choice==game[0]:
        print("Computer chose")
        print(c_choice)
        print("you won")
    
elif choice==2: 
    print("Your choice")
    print(scissor)
    if c_choice==game[2]:
        print("Computer chose")
        print(c_choice)
        print("its a draw")
    elif c_choice==game[0]:
        print("Its a draw")
        print(c_choice)
        print("Computer won")
    elif c_choice==game[1]:
        print("Computer chose")
        print(c_choice)
        print("you won")
else:
    print("Enter the correct choice")

    