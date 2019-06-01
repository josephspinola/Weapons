#High Score game 2.0 Display the names and only the top 3 scores

# Welcome the user to the game

print('\n\nWelcome User to High Score 2.0','\U0001f600'*3)

# Assign the Users Choice and Scores List

highScores = [('Joe',5000),('Shmo',6000),('Tod',3000),('Doe',10,000),('Low',2000)]
choice = None

# Display the menu options

print('\n\nMenu Options','\nQuit-0','\nList Scores-1','\nAdd Score-2')

# Ask the user for his choice and then list the sequences for the menu options

while choice != 0:
    choice = int(input('\n\nSelect a menu option: '))
    

    if choice == 1:
        print('\n\nHere are the top 3 HIGH SCORES\n')
        for x in highScores:
            name, score = x
            print(name,score)
        

    elif choice == 2:
        addedName = input('Enter Name : ')
        addedScore = int(input('Add score: '))
        entry = (addedName,addedScore)
        highScores.append(entry)
        print('\n\nHere is the updated scores : ',highScores)





    









    
    




