#Colours
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
#Winter Drinks List with Nested Dictionary
winter_drinks = [
        {"item_Id": "A1", "item_Name": "Hot Chocolate", "item_Price": 20, "Stock": 10},
        {"item_Id": "A2", "item_Name": "Pumpkin Spice Latte", "item_Price": 5, "Stock": 10},
        {"item_Id": "A3", "item_Name": "Tea", "item_Price": 10, "Stock": 10},
        {"item_Id": "A4", "item_Name": "Coffee", "item_Price": 15, "Stock": 10},
        {"item_Id": "A5", "item_Name": "Cappuccino", "item_Price": 5, "Stock": 10},
    ]

#Winter Snacks List with Nested Dictionary
winter_snacks = [
        {"item_Id": "B1", "item_Name": "Chocolate Bread", "item_Price": 20, "Stock": 10},
        {"item_Id": "B2", "item_Name": "Ginger Bread", "item_Price": 5, "Stock": 10},
        {"item_Id": "B3", "item_Name": "Cinnamon Roll", "item_Price": 10, "Stock": 10},
        {"item_Id": "B4", "item_Name": "Coffee Cookies", "item_Price": 15, "Stock": 10},
        {"item_Id": "B5", "item_Name": "Marshmallows", "item_Price": 5, "Stock": 10},
    ]

#Summer Drinks List with Nested Dictionary
summer_drinks = [
        {"item_Id": "C1", "item_Name": "Ice Cream", "item_Price": 12, "Stock": 10},
        {"item_Id": "C2", "item_Name": "Soda", "item_Price": 7, "Stock": 10},
        {"item_Id": "C3", "item_Name": "Lemonade", "item_Price": 23, "Stock": 10},
        {"item_Id": "C4", "item_Name": "Candy", "item_Price": 9, "Stock": 10},
        {"item_Id": "C5", "item_Name": "Strawberry Smoothie", "item_Price": 35, "Stock": 10},
    ]

#Summer Snacks List with Nested Dictionary
summer_snacks = [
        {"item_Id": "D1", "item_Name": "Popsicle", "item_Price": 10, "Stock": 10},
        {"item_Id": "D2", "item_Name": "Biscuits", "item_Price": 8, "Stock": 10},
        {"item_Id": "D3", "item_Name": "Chips", "item_Price": 12, "Stock": 10},
        {"item_Id": "D4", "item_Name": "Candy Bar", "item_Price": 9, "Stock": 10},
        {"item_Id": "D5", "item_Name": "Frozen Yogurt", "item_Price": 15, "Stock": 10},
    ]

#Dictionary for Recommendations
recommendations = {
    "A1": "B4",  # Hot Chocolate -> Coffee Cookies
    "A2": "B3",  # Pumpkin Spice Latte -> Cinnamon Roll
    "A3": "B1",  # Tea -> Chocolate Bread
    "A4": "B2",  # Coffee -> Ginger Bread
    "A5": "B5",  # Cappuccino -> Marshmallows
    "B1": "A3",  # Chocolate Bread -> Tea
    "B2": "A4",  # Ginger Bread -> Coffee
    "B3": "A2",  # Cinnamon Roll -> Pumpkin Spice Latte
    "B4": "A1",  # Coffee Cookies -> Hot Chocolate
    "B5": "A5",  # Marshmallows -> Cappuccino
    "C1": "D5",  # Ice Cream -> Frozen Yogurt
    "C2": "D3",  # Soda -> Chips
    "C3": "D1",  # Lemonade -> Popsicle
    "C4": "D4",  # Candy -> Candy Bar
    "C5": "D2",  # Strawberry Smoothie -> Biscuits
    "D1": "C3",  # Popsicle -> Lemonade
    "D2": "C5",  # Biscuits -> Strawberry Smoothie
    "D3": "C2",  # Chips -> Soda
    "D4": "C4",  # Candy Bar -> Candy
    "D5": "C1",  # Frozen Yogurt -> Ice Cream
}
#Def Function for Winter Drinks
def Winter_Drinks():
    return winter_drinks
#Def Function for Winter Snacks
def Winter_Snacks():
    return winter_snacks
#Def Function for Summer Drinks
def Summer_Drinks():
    return summer_drinks
#Def Function for Summer Snacks
def Summer_Snacks():
    return summer_snacks

#Def Function for Format 
def format_items(items):
# for loop
    for item in items:
# The format
        print(f"Item: {item['item_Name']}  |  Price: ${item['item_Price']}  |  Item ID: {item['item_Id']}  |  Stock: {item['Stock']}")
#Def Function Main
def main():
#While Loop
    while True:
        #Print function
        print(BLUE +"""██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    
              
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗""")
        #Print Function
        print(RED + """╔═╗┬ ┬┌─┐┌─┐┌─┐┌─┐  ┌┬┐┬ ┬┌─┐  ┌─┐┌─┐┌─┐┌─┐┌─┐┌┐┌
║  ├─┤│ ││ │└─┐├┤    │ ├─┤├┤   └─┐├┤ ├─┤└─┐│ ││││
╚═╝┴ ┴└─┘└─┘└─┘└─┘   ┴ ┴ ┴└─┘  └─┘└─┘┴ ┴└─┘└─┘┘└┘""")
#Input Keyword
        season = input( WHITE + "Is it Winter or Summer? ").capitalize()
#If Function
        if season == "Winter":
            choice = input(BLUE + """\n
            Do you want Drinks or Snacks?
            Choose 1 for Drinks
            Choose 2 for Snacks
             Your Choice:  \n""").capitalize() #Input Keyword
            if choice == "1":
                print("\nHere are the Winter Drinks:\n") #If Function
                items = Winter_Drinks() #Calling Winter_Drinks Function and returning to items
                #Elif Keyword
            elif choice == "2":
                print("\nHere are the Winter Snacks:\n") #Print Function
                items = Winter_Snacks() #Calling Winter_Snacks Function and returning to items
                #Else Keyword
            else:
                print("\nInvalid choice! Please enter 'Drinks' or 'Snacks'.") #Print Function
                continue # Skips rest of iteration / Allows user to attempt again

        elif season == "Summer": #Elif Keyword
            choice = input(RED + """\n
            Do you want Drinks or Snacks?
            Choose 3 for Drinks
            Choose 4 for Snacks
             Your Choice:  \n""").capitalize() #Input Keyword
            if choice == "3": #If function
                print("\nHere are the Summer Drinks:\n") #Print Function
                items = Summer_Drinks() #Calling Summer_Drinks Function and returning to items
            elif choice == "4": #Elif Keyword
                print("\nHere are the Summer Snacks:\n") #Print Function
                items = Summer_Snacks() #Calling Summer_Snacks Function and returning to items
            else: #Else Keyword
                print("\nInvalid choice! Please enter 'Drinks' or 'Snacks'.") #Print Function
                continue # Skips rest of iteration / Allows user to attempt again

        else:
            print("\nInvalid input! Please enter 'Winter' or 'Summer'.") #Else Keyword
            continue # Skips rest of iteration / Allows user to attempt again

        format_items(items) #Calls format_items
#While loop
        while True:
            choice_1 = input(WHITE + """\nPlease Select your Choice:
\033[32m1) Enter Balance
\033[31m2) Leave the Vending Machine
\033[34m3) Go back to the main menu
\033[37mEnter 1, 2, or 3: """).strip() #Input Keyword

            if choice_1 == "1": #If Function
                try: #Try Block
                    balance = float(input(GREEN + "\nEnter your balance: $").strip()) #Input Keyword
                except ValueError: # except block and ValueError
                    print(RED + "Please consider using a Number...")#Print Function
                    continue # Skips rest of iteration / Allows user to attempt again

                item_id = input("Enter the Item ID of the product you want to buy: ").upper() #Input Keyword

                selected_item = next((item for item in items if item['item_Id'] == item_id), None)#Next Function finding first matching Item/ for loop 

                if selected_item: #If Function
                    if balance >= selected_item['item_Price']: #If Function
                        print(f"\nYou bought a {selected_item['item_Name']} for ${selected_item['item_Price']}.")#Print Function
                        change = balance - selected_item['item_Price']# Change Variable
                        print(f"Your change is: ${change:.2f}") #Print Function
                        selected_item['Stock'] -= 1 #Stock functionality

                        recommended_id = recommendations.get(selected_item['item_Id'])#recommended_id variable
                        if recommended_id: #If Function
                            recommended_item = next((item for item in winter_drinks + winter_snacks + summer_drinks + summer_snacks if item['item_Id'] == recommended_id), None)#recommended_item Variable
                            if recommended_item and recommended_item['Stock'] > 0: #If Function/ and Logical Operator
                                reco = input(BLUE + f"\nWe recommend you also try: {recommended_item['item_Name']} for ${recommended_item['item_Price']} (Item ID: {recommended_item['item_Id']}).\n(y/n)\n") #Input Keyword
                                if reco == "y": #If Function
                                    if change >= recommended_item["item_Price"]: #If Function
                                        print(f"\nYou bought {recommended_item['item_Name']} in addition, for {recommended_item['item_Price']:.2f}.")#Print Function
                                        change = change - recommended_item["item_Price"] #Calculation
                                        print(f"Your change is: ${change:.2f}") #Print Function
                                        recommended_item["Stock"] -= 1 #Stock Functionality
                                        #Else Keyword
                                    else:
                                        print(RED + "\nInsufficient balance! Please add more money.") #Print Function
                                else: #Else Keyword
                                    print(GREEN+ """███████╗███╗   ██╗     ██╗ ██████╗ ██╗   ██╗██╗
██╔════╝████╗  ██║     ██║██╔═══██╗╚██╗ ██╔╝██║
█████╗  ██╔██╗ ██║     ██║██║   ██║ ╚████╔╝ ██║
██╔══╝  ██║╚██╗██║██   ██║██║   ██║  ╚██╔╝  ╚═╝
███████╗██║ ╚████║╚█████╔╝╚██████╔╝   ██║   ██╗
╚══════╝╚═╝  ╚═══╝ ╚════╝  ╚═════╝    ╚═╝   ╚═╝""") #Print Function

                            else: #Else Keyword
                                print("\nWe currently have no additional recommendations.")#Print Function

                    else: #Else Keyword
                        print("\nInsufficient balance! Please add more money.") #Print Function
                else: #Else Keyword
                    print("\nInvalid Item ID! Please try again.")#Print Function

            elif choice_1 == "2": #Elif Keyword
                print("\nThank you for using the vending machine. Goodbye!")#Print Function
                return #Return Statement

            elif choice_1 == "3": #Elif Keyword
                print("\nReturning to the main menu...\n") #Print Function
                break # Break Statement

            else: #Else Keyword
                print("\nInvalid choice! Please enter 1, 2, or 3.") #Print Function

main() #Calling main
