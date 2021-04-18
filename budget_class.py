database = {"food": 0, "clothing": 0, "entertainment":0}

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    @staticmethod
    def availableCategory():
        for key, value in database.items():
            print(f"-  {key}")


    @staticmethod
    def deposit():
        
        print("-"*50)
        print('==== See available budget categories ====')
        for key, value in database.items():
            print(f"-  {key}")
        print("")


        cat_name = input("Please enter the category name you would like make deposit too \n").lower()
        if cat_name in database:
            amt = int(input("Enter amount to deposit \nNGN "))
            balance = int(database[cat_name])
            new_balance = balance + amt #Budget.deposit(amt, balance)
            database[cat_name] = new_balance
            print(f'\n{cat_name} category as been credited with NGN {amt}\nTotal {cat_name} category budget amount is now NGN {new_balance}')
            menu()

        else:
            print('')
            pick = input(f'{cat_name} category does not exist!\nEnter [cb] To create a new budget category\nEnter [rb] To re-enter budget category name\nEnter [mm] To go back to main menu\n')
            if (pick == "cb"):
                Budget.new_budget_category()
            elif (pick == "rb"):
                Budget.deposit()
            elif (pick == "mm"):
                menu()
            else:
                print('Invalid option\n')
                Budget.deposit()
        

       

    def withdraw():
        cat_name = input("Please enter the category name you would like to withdraw from \n").lower()
        if cat_name in database:
            withdraw_amt = int(input("Please enter amount to withdraw: "))
            if withdraw_amt > database[cat_name]:
                print(f"\nYou do not have enough fund in {cat_name} category. Please choose an option below.")
                response = input("\n\nEnter [md] To make a deposit. \nEnter [mm] To go back to main menu.\n\n>").lower()
                if response == "md":
                    Budget.deposit()

                elif response == "mm":
                    menu()
                
                else:
                    print("Invalid input")

                

            else:
                balance = int(database[cat_name])
                new_balance = balance - withdraw_amt 
                database[cat_name] = new_balance
                print(f'\n{cat_name} category as been debited with NGN {withdraw_amt}\nTotal {cat_name} category budget amount is now NGN {new_balance}')
                menu()
        
        else:
            print("Invalid cat name")

    

    def transfer():
        cat_name = input("From what category would you like to transfer: ")
        if cat_name in database:
            transfer_amt = int(input("Please enter amount you would like to transfer: "))
            balance = int(database[cat_name])
            if transfer_amt < balance:
                receiving_cat = input("What category are you sending too: ").lower()
                receiving_balance = int(database[receiving_cat])
                new_balance = receiving_balance + transfer_amt
                database[receiving_cat] = new_balance

                print(f"\n{receiving_cat} as been credited NGN{transfer_amt}. {receiving_cat} now have total balance of NGN{receiving_balance}")
                menu()
            else:
                print(f"You do not have enough fund in {cat_name}")
        
        else:
            print("Invalid input")
            
        

    def balance():
        print("-"*50)
        print('==== See available budget categories ====')
        for key, value in database.items():
            print(f"-  {key}")
        print("")

        cat_name = input("Please enter budget category name: ").lower()

        balance = int(database[cat_name])
        print(cat_name + " NGN" + str(balance))

        

        """for cat, bal in database.items():
            print(categ, bal)"""
    
    @staticmethod
    def new_budget_category():
        print("\n=== ***Creating a New Budget**** ===\n")

        budget_title = input("Enter budget name \n")
        try:
            amount = int(input("Enter your budget amount \n$"))
        except:
            print('\nInvalid input')
            new_budget()
        #budget = Budget(budget_title, amount)
        database[budget_title] = amount
        print('')
        print(f'Budget {budget_title} was setup with ${amount}')
        menu()



def init():
    print('=== Welcome to the Budget App===\n')
    menu()

def menu():
    try:

        user = input('\n=== ****What would you like to do?**** ===\nEnter [ac] See available categories\nEnter [md] Make deposit to budget\nEnter [mw] Make withdrawer from budget\nEnter [cb] Check budget balance\nEnter [tb] Transfer from budget to another budget\n').lower()
    except:
        print('Invalid input')
        menu()

    if (user == "ac"):
        Budget.availableCategory()
    elif (user == "md"):
        Budget.deposit()
    elif (user == "mw"):
        Budget.withdraw()
    elif (user == "cb"):
        Budget.balance()
    elif (user == "tb"):
        Budget.transfer()
    
        
    else:
        print('Invalid input\n')
        menu()

init()