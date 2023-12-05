# List with Mulitple Words and it will be chosen at random
# find the range of the random picked word 
# split string into char into seprate list
# asks for user input
# for every wrong input i will kill the character
# for every right input i reveal the correct one and not kill the character
import random
import hangman_words
import hangman_art


print(hangman_art.logo+"\n")

choosen_word = hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)].lower()


answer_list=[]
choosen_word_list=[]

for letter in choosen_word:
    choosen_word_list.append(letter)
    answer_list.append("_")
        
Total_chances = 6
stage=5

print(f"{answer_list}\n")

  
while Total_chances!=-1:
    lifestate_correct=False
    lifestate_wrong=False
       
    if Total_chances!=0:        
        if choosen_word_list!=answer_list:
            guess = input("Guess a letter : ").lower()
                      
            for j in range(0,len(choosen_word_list)):  
                if choosen_word_list[j]==guess:
                    answer_list[j]=guess
                    lifestate_correct=True                    
                else:
                    lifestate_wrong=True
                    
            print(answer_list) 
                 
        else:
            print("GameWon!")
            Total_chances=-1
        if lifestate_wrong==True and lifestate_correct == False:                
            Total_chances=Total_chances-1            
            print(hangman_art.stages[stage])
            stage=stage-1 
    else:
        print(f"Out of chance try again ! \nThe Word is : {choosen_word}")
        Total_chances=-1      
        








