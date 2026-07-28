import random
def menu():
  print("=======Rock Paper Scissors========")
  print("1.Rock")
  print("2.Scissors")
  print("3.Paper")
while True:
  menu()
  choice=int(input("Enter your choice: "))
  if choice<1 or choice>3:
    print('Invalid input. Please enter 1, 2, or 3.')
    continue
  answer=random.randint(1,3)
  if answer==1:
    print("Computer chose: Rock")
  elif answer==2:
    print("Computer chose: Scissors")
  elif answer==3:
    print("Computer chose: Paper")
  if choice==answer:
    print("Draw")
  elif choice==1 and answer==2:
    print("You win!")
  elif choice==2 and answer==3:
    print("You win!")
  elif choice==3 and answer==1:
    print("You win!")
  else:
     print("You lose!")
  again=input("Play again? (y/n): ")
  if again=="n":
      print("Game over!")
      break
