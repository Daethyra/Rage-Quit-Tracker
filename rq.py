import pandas as pd

class UserTallies:
    COLUMN_NAME = "Rage Quits"
    FILE_NAME = "ragequits.csv"
    
    def __init__(self):
        try:
            self.df = pd.read_csv(self.FILE_NAME, index_col=0)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=[self.COLUMN_NAME])
    
    def save(self):
        self.df.to_csv(self.FILE_NAME)
    
    def add_user(self, user_name):
        self.df.loc[user_name] = 0
        self.save()
        print(f"{user_name} added!")
    
    def remove_user(self, user_name):
        if user_name in self.df.index:
            self.df.drop(index=user_name, inplace=True)
            self.save()
            print(f"{user_name} removed!")
        else:
            print(f"{user_name} not found!")
    
    def add_tally(self, user_name):
        if user_name in self.df.index:
            self.df.loc[user_name, self.COLUMN_NAME] += 1
            self.save()
            print(f"{user_name} now has {self.df.loc[user_name, self.COLUMN_NAME]} tallies.")
        else:
            print(f"{user_name} not found!")
    
    def remove_tally(self, user_name):
        if user_name in self.df.index and self.df.loc[user_name, self.COLUMN_NAME] > 0:
            self.df.loc[user_name, self.COLUMN_NAME] -= 1
            self.save()
            print(f"{user_name} now has {self.df.loc[user_name, self.COLUMN_NAME]} tallies.")
        else:
            print(f"{user_name} not found or tally is already zero!")
    
    def print_data(self):
        print("\nCurrent data:")
        print(self.df.to_string(justify='center', col_space=13, header=True))

def add_user(user_tallies):
    user_name = input("Enter a user name: ")
    user_tallies.add_user(user_name)

def remove_user(user_tallies):
    user_name = input("Enter a user name: ")
    user_tallies.remove_user(user_name)

def add_tally(user_tallies):
    user_name = input("Enter a user name: ")
    user_tallies.add_tally(user_name)

def remove_tally(user_tallies):
    user_name = input("Enter a user name: ")
    user_tallies.remove_tally(user_name)

def main():
    user_tallies = UserTallies()
    
    commands = {
        1: add_user,
        2: remove_user,
        3: add_tally,
        4: remove_tally,
        5: exit,
    }
    
    while True:
        user_tallies.print_data()
        print("\nCommands:")
        print("1. Add User")
        print("2. Remove User")
        print("3. Add Tally")
        print("4. Remove Tally")
        print("5. Quit")
        
        # Wait for user input and validate it
        command = input("Enter a command number: ")
        try:
            command = int(command)
        except ValueError:
            print("Invalid command number!")
            continue
        
        # Call the corresponding command function
        if command in commands:
            commands[command](user_tallies)
        else:
            print("Invalid command number!")


if __name__ == '__main__':
    main()
