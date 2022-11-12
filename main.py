print("Welcome to the Math Game!")
print()

print("Enter any integer and let us see if you know the multiples of that number.")
print()

print("Everytime you key in your response press enter. Best score 10. Goodluck!!!")

def showWinMessage(count):
  if count > 4 and count <= 6:
    print()
    print("Good effort!")
    print("You got",count,"out of 10.")  
    print() 
  elif count <=4:
    print()
    print("Keep practicing you will get better!")
    print("You got",count,"out of 10.")  
    print() 
  elif count >=7 and count <=9:
    print()
    print("Awesome!")
    print("You got",count,"out of 10.")  
    print() 
  elif count == 10:
    print()
    print("Phenomenal! 😁😁😁")
    print("You got",count,"out of 10.")  
    print() 
    
  

quitList = ["y","yes", 'quit', 'exit']
exit = ""
while exit.lower() not in quitList:
  print()
  try:
    num = int(input("Name your multiples by entering a number of your choice. "))
    print()
  except ValueError:
    print()
    print("I am expecting positive numbers.")
    print()
    continue

  if num <= 0:
    print("I don't like zero and negative numbers.")
    continue 
  else:
    count = 0
    for i in range(1,11):
      print(i,"X",num,"= ")
      try:
        answer = int(input())
        print()
      except ValueError:
        print()
        print("Nope. The answer was",i*num)
        print()
        print("I am expecting positive numbers.")
        print()
        continue 
      if answer == i*num:
        count+=1
        print("Correct!")
        print()
      else:
        print("Nope. The answer was",i*num)
    showWinMessage(count) 

    exit = input("Would like to exit the game? ")
     
  
def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run """)
    print()
    continue


if __name__=="__main__":
  endGame()