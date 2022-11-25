import random 
import time

def random_equation(num): 
    operatorList =  ["-","+","*"]
    equation = ""
    for i in range(num):
        number = random.randint(1, 10)
        equation = equation + str(number)+ ' '
        operator = random.choice(operatorList)
        equation = equation + operator + ' '
    number = random.randint(1, 10)
    equation += str(number)
    return equation 

def query_equation(returnedEquation):
    evaluation = eval(returnedEquation)
    print(returnedEquation)
    userAnswer = int(input("Answer: "))
    while userAnswer != evaluation: 
        if userAnswer - 2 <= evaluation <= userAnswer + 2: 
            print("Close, try again")
        else:
            print("Keep trying")
        userAnswer = int(input("Answer: "))
    print("Correct!\n")
        

def play_game(num, gameDuration):
    startTime = time.time() 
    currentTime = time.time() 
    elapsedTime = currentTime - startTime
    wordcount = 0 
    while elapsedTime < gameDuration:   
        query_equation(random_equation(num))
        wordcount += 1 
        currentTime = time.time()
        elapsedTime = currentTime - startTime 

    print("You got %d corrrect in" %(wordcount), str(int(elapsedTime))  + " seconds.")
                                                                                      
def main():
    gameStart = input("Do you want to play a game [yes/no]? ")
    if gameStart == "yes" or gameStart == "Yes":  
        num = random.randint(1, 10) 
        userTime = int(input("How long do you want to play for [seconds]? "))
        play_game(2, userTime)
    else:
        print("Bye") 

if __name__ == '__main__':
    main()