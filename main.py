print("Welcome to the Math Game!")
print()

print("Enter any integer and let us see if you know the multiples of that number.")
print()

print("Everytime you key in your response press enter. Best score 10. Goodluck!!!")

def showWinMessage(count):
  print("You got",count,"out of 10.")  
  print() 
  


ansList = []

while True:
  print()
  try:
    num = int(input("Name your multiples by entering a number of your choice. "))
    print()
  except ValueError:
    print()
    print("I am expecting positive numbers.")
    print()
    continue

  if num < 0:
    print("I don't like zero and negative numbers. Goodbye.")
    break 
  else:
    # ansList.clear()
    for i in range(1,11):
      # print(i,"X",num,"=",i*num)
      ansList.append(i*num)
      print(i,"X",num,"= ")
      count = 0
      while count < 11:
        count+=1
        print()
        try:
          answer = int(input())
          print()
        except ValueError:
          print()
          print("I am expecting positive numbers.")
          print()
          continue
        print(i,"X",num,"= ")  
        if answer in ansList:
          print("Well done!")
        else:
          print("Nope. The answer was",i*num)
    print(ansList)    
     
      


def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run """)
    print()
    continue


if __name__=="__main__":
  endGame()