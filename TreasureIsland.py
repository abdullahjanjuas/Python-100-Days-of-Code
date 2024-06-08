print("============================TREASURE ISLAND GAME START==========================")
print("Your mission is to find the treasure, Good Luck!")
dir_1 = input("You are at a cross road.Where do you want to go,left or right?")
l_dir_1 = dir_1.lower()

if l_dir_1 == "right":
    print("Game Over.")

elif l_dir_1 == "left":
    dir_2 = input("You com to a lake.There is an island in the middle of lake.Type 'wait' to wait for a boat.Type 'swim' to swim across. ")
    l_dir_2 = dir_2.lower()
    
    if l_dir_2 == "swim":
        print("Game Over.")
    elif l_dir_2 == "wait":
        color = input("You arrive at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which color do you choose?")
        l_color = color.lower()
        
        if l_color == "blue" or l_color == "red":
            print("Game Over!")
        elif l_color == "yellow":
            print("YOU WIN!")