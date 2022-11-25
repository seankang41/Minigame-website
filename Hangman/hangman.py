import random 

def play_wordgame(filename, num_incorrect_allowed):
    lives = '*'*num_incorrect_allowed
    print("Incorrect Guesses left:", lives)
    words = readWords(filename)
    sampleWord = random.choice(words)
    underscoredWord = '_'*len(sampleWord)
    letterSet = set() 


    while num_incorrect_allowed >= 0:
        userGuess = input("Guess a word:")
        
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        updatedWord = insert_letters(userGuess, sampleWord, underscoredWord)
        if userGuess.upper() not in alphabets:
            print("invalid variable")
        
        else:
            if userGuess.upper() in set_to_string(letterSet):
                print("already guessed")
        
            elif updatedWord != underscoredWord:
                underscoredWord = updatedWord 
                if updatedWord == sampleWord:
                    print("U win!")
                    break
                else: 
                    print("Incorrect Guesses left:", lives)
                    print("Word:", updatedWord)
                    
            elif updatedWord == underscoredWord:
                num_incorrect_allowed -= 1 
                lives = '*'*num_incorrect_allowed
                print("Incorrect Guesses left:", lives)
                print("Word:", updatedWord)
            

            letterSet.add(userGuess)
            userGuessSet = set_to_string(letterSet)
            print("Guessed words:", userGuessSet)
        
        if lives == "":
                print("Game over") 
                break
  


             
def readWords(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines() 
        return words
        
def set_to_string(letter_set): 
    newString = ""
    for i in letter_set:
        if newString=="":
            newString+=i
        else:
            newString = newString + " " + str(i)
    return newString.upper()
    

def insert_letters(letter, word, u_word):
    newstring = ""
    a = 0
    for l in word:
        if l == letter: 
            newstring = newstring + l 
        else:
            newstring = newstring + u_word[a]
        a += 1 
    return newstring
            
if __name__ == '__main__':
    play_wordgame("words.txt", 7)
    

    