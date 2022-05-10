def main():
    #created dictionary linking rooms and items
    rooms = {
            'Slumbering Abode' : { 'East' : 'Expanse'},
            'Castle' : {'South' : 'Capitol'},
            'Expanse' : { 'North' : 'Swamps', 'East' : 'Capitol', 'South' : 'Desert', 'West' : 'Slumbering Abode', 'Item' : 'Armor' },
            'Capitol' : {'North' : 'Castle', 'West' : 'Expanse', 'Item' : 'Potion H' },
            'Desert': {'North' : 'Expanse', 'East' : 'Southern Peak', 'Item' : 'Fire Gauntlets' },
            'Southern Peak' : {'West' : 'Desert', 'Item' : 'Ice Rod' },
            'Swamps' : { 'South' : 'Expanse', 'East' : 'Wildlands', 'Item' : 'Potion S' },
            'Wildlands' : {'West' : 'Swamps', 'Item' : 'Speed Boots'}
    }

    def show_status(): #Show Status
        print('You are at the ', location)
        print('Inventory:', inventory)



    def show_instructions():
        # print a main menu and the commands
        print("Restoring the Lost Kingdom.\n")
        print("Collect the 6 unique items from the spellbound rooms or get YEETED by The Evil Lord Uub!\n")
        print("Move commands, Enter: South, North, East, West, or Exit\n")
        print("To add an item to Inventory, Enter: Get 'item name'\n")   

    def get_new_location(location, direction): #function to move rooms
        new_location = location
        for key in rooms: #loop
            if key == location:
                if direction in rooms[key]:
                    new_location = rooms[key][direction]
        return new_location #moving between rooms

    def get_item(location): #dictionary for items
        items = {
            'Expanse': 'Armor',
            'Capitol': 'Potion H',
            'Desert': 'Fire Gauntlets',
            'Southern Peak': 'Ice Rod',
            'Swamps': 'Potion S',
            'Wildlands': 'Speed Boots',

        }

        return items[location] # return items in location

    show_instructions() #call function
    inventory = [] #set empty inventory

    location = 'Slumbering Abode' #start location

    while True:  # main gameplay loop
        show_status() #call function
        if location == 'Slumbering Abode': #start room
            direction = input('Enter your move: \n -->') #recieve input form player
            title = direction.title() #capitilizing first letter of each input
            if title == 'Exit': #choice to quit
                print('You have quit the game.  Thanks for playing!')
                break
            if title == 'East' or title == 'West' or title == 'North' or title == 'South': #if 
                new_location = get_new_location(location, title) # call function
                if new_location == location: #if
                    print('Invalid Entry, Pick another direction!') #input validation
                else:
                    location = new_location 
                    print('\n')
            else:
                print('Invalid direction!!\n') #input validation
            continue

        item = get_item(location) # call function
        if not item in inventory: #if to display items
            print('You see',item)
            print('--------------------------------')
        if len(inventory) == 6:
            print('Congratulations! You have aquired all the items, you are now the GOAT!')
            break #player wins

        direction = input('Enter your move: \n -->') #input following start room
        title = direction.title()
    

        if title == 'East' or title == 'West' or title == 'North' or title == 'South':
            new_location = get_new_location(location, title) #call function
            if new_location == 'Castle': #if
                print('YEET! GAME OVER! You have reached Lord Uub without all the items!')
                break #player loses
            if new_location == location: #if, input validation
                print('Invalid Entry, Pick another direction!\n') 
            else:
                location = new_location
        elif title == 'Get ' + item: #elif room has item, get item
            if item in inventory:
                print('You have already retrieved this item!') #input validation
            else:
                print(item + ' retrieved!\n')
                inventory.append(item)
        elif title == 'Exit':
            print('You have quit the game.  Thanks for playing!')
            break #exit option once out of main room
        else:
            print('Invalid input!!')

main() #calling main function

