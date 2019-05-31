# Create a heros inventory list and allow the user to select the weapons
# After the weapon selection place gold and rubies in the list by finding a "Chest"

# Welcome the user and define the list and the elements it will contain


print("\nWelcome to the hero's game","\n\nThe selection of weapons is below....\n\n")
Inventory = ['Shield','Sword','Potion','Magic','Spell']

# Access the elements from the Inventory using x and display the Inventory

for x in Inventory:
    print(x)


# Allow the user to select 2 weapons of choice for battle from the Inventory
# Assign the new Inventory for war

print('\n\nNow select 2 weapons of your choice')

Selection_1 = int(input('\n\nWeapon #1 : '))

War_Inventory = Inventory[Selection_1]
del Inventory[Selection_1]

#Display the rest of the elements in Inventory for the user to select from

print("\n\nHere is what's left choose wisely....")
for a in Inventory:
    print(a)

Selection_2 = int(input('\n\nWeapon #2 : '))
War_Inventory2 = [War_Inventory,Inventory[Selection_2]]
del Inventory[Selection_2]
  

# Notify the user of his weapons and to prepare for battle

print('\n\nWE ARE WAR READY!','\n\nHere is your War Inventory: ', War_Inventory2)
print(input('\n\nPress Enter to Advance'))


# Create a scene route option
# Assign the routes as variables

Route1 = 1
Route2 = 2

print('\n\nWe now must choose our path in the split road')
print('\n\nRoute 1 - Magic Mushrooms','\nRoute 2 - Foresty Ganja')
User_Route = int(input('\n\nChoose a route: '))

# If route 1 is chosen
# Add a treasure chest of gold and rubies to the user 
# Add the list of gold and rubies to the current war inventory list

if User_Route == Route1: 
    Gold = ['Gold','Rubies']
    War_Inventory2 += Gold

    print('\n\n\nCONGRATS YOU FOUND GOLD AND RUBIES!')
    print('\n\nHere is what you will go to battle with now: ','\n\n',War_Inventory2)

# If route 2 is chosen
# Add a bong and snack pack
# Add the new items to the current inventory list

elif User_Route == Route2:
    Ganja = ['Bong','Snack Pack']
    War_Inventory2 += Ganja
    print('\n\n\nCONGRATS YOU FOUND A BONG AND SNACK PACK!')
    print('\n\nHere is what you will go to battle with now: ','\n\n',War_Inventory2)
      

# Now ask if the user would like to purchase a crossbow for gold and rubies
# Assign the users variable
print('\n\nHere is a crossbow for your gold and rubies')

War_Inventory2[2:4] = ['Crossbow']


print('\n\nHere is the new weapon list for war: ', War_Inventory2)



    









    
    




