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
        if user_name in self.df.index:
            print(f"\n{user_name} already exists!")
            return
        self.df.loc[user_name] = 0
        self.save()
        print(f"\n{user_name} added!")
    
    def add_user_by_number(self, user_num):
        if user_num <= 0 or user_num > len(self.df):
            print("\nInvalid user number!")
            return
        user_name = self.df.index[user_num-1]
        self.add_user(user_name)
    
    def remove_user(self, user_name):
        if user_name in self.df.index:
            self.df.drop(index=user_name, inplace=True)
            self.save()
            print(f"\n{user_name} removed!")
        else:
            closest_match = self.df.index[self.df.index.str.contains(user_name, case=False)]
            if len(closest_match) == 0:
                print(f"\n{user_name} not found!")
            elif len(closest_match) == 1:
                self.df.drop(index=closest_match[0], inplace=True)
                self.save()
                print(f"\n{closest_match[0]} removed!")
            else:
                print("\nMultiple matches found. Please enter a user number instead:")
                for i, name in enumerate(closest_match):
                    print(f"{i+1}. {name}")
                user_num = input()
                try:
                    user_num = int(user_num)
                    user_name = self.df.index[user_num-1]
                    self.df.drop(index=user_name, inplace=True)
                    self.save()
                    print(f"\n{user_name} removed!")
                except ValueError:
                    print("\nInvalid user number!")
    
    def remove_user_by_number(self, user_num):
        if user_num <= 0 or user_num > len(self.df):
            print("\nInvalid user number!")
            return
        user_name = self.df.index[user_num-1]
        self.remove_user(user_name)
    
    def add_tally(self, user_input):
        if isinstance(user_input, int):
            if not (0 < user_input <= len(self.df)):
                print("\nInvalid user number!")
                return
            user_name = self.df.index[user_input-1]
        else:
            closest_match = self.df.index[self.df.index.str.contains(user_input, case=False)]
            if not closest_match.size:
                print("\nUser not found!")
                return
            elif closest_match.size == 1:
                user_name = closest_match[0]
            else:
                print("\nMultiple matches found. Please enter a user number instead:")
                for i, name in enumerate(closest_match):
                    print(f"{i+1}. {name}")
                user_num = input()
                try:
                    user_num = int(user_num)
                    if not (0 < user_num <= closest_match.size):
                        print("\nInvalid user number!")
                        return
                    user_name = closest_match[user_num-1]
                except ValueError:
                    print("\nInvalid user number!")
                    return

            self.df.loc[user_name, self.COLUMN_NAME] += 1
            self.save()
            print(f"\n{user_name} now has {self.df.loc[user_name, self.COLUMN_NAME]} tallies.")


    def remove_tally(self, user_input):
        if isinstance(user_input, int):
            if not (0 < user_input <= len(self.df)):
                print("\nInvalid user number!")
                return
            user_name = self.df.index[user_input-1]
        else:
            closest_match = self.df.index[self.df.index.str.contains(user_input, case=False)]
            if not closest_match.size:
                print("\nUser not found!")
                return
            elif closest_match.size == 1:
                user_name = closest_match[0]
            else:
                print("\nMultiple matches found. Please enter a user number instead:")
                for i, name in enumerate(closest_match):
                    print(f"{i+1}. {name}")
                user_num = input()
                try:
                    user_num = int(user_num)
                    if not (0 < user_num <= closest_match.size):
                        print("\nInvalid user number!")
                        return
                    user_name = closest_match[user_num-1]
                except ValueError:
                    print("\nInvalid user number!")
                    return

        if self.df.loc[user_name, self.COLUMN_NAME] > 0:
            self.df.loc[user_name, self.COLUMN_NAME] -= 1
            self.save()
            print(f"\n{user_name} now has {self.df.loc[user_name, self.COLUMN_NAME]} tallies.")
        else:
            print(f"\n{user_name} not found or tally is already zero!")


    def print_data(self):
        print("_______________")
        print("Current data:")
        print("\n  #  User Name      Rage Quits\n")
        for i, (name, value) in enumerate(self.df[self.COLUMN_NAME].items()):
            print(f"{i+1:3}. {name:12} {value:3}")


def add_user(user_tallies):
    user_input = input("\nEnter a user name or 'n' to cancel: ")
    if user_input.lower() == 'n':
        return
    try:
        user_num = int(user_input)
        user_tallies.add_user_by_number(user_num)
    except ValueError:
        user_tallies.add_user(user_input)

def remove_user(user_tallies):
    user_input = input("\nEnter a user name or 'n' to cancel: ")
    if user_input.lower() == 'n':
        return
    try:
        user_num = int(user_input)
        user_tallies.remove_user_by_number(user_num)
    except ValueError:
        user_tallies.remove_user(user_input)

def add_tally(user_tallies):
    user_input = input("\nEnter a user name or number or 'n' to cancel: ")
    if user_input.lower() == 'n':
        return
    try:
        user_num = int(user_input)
        user_tallies.add_tally(user_num)
    except ValueError:
        user_tallies.add_tally(user_input)

def remove_tally(user_tallies):
    user_input = input("\nEnter a user name or number or 'n' to cancel: ")
    if user_input.lower() == 'n':
        return
    try:
        user_num = int(user_input)
        user_tallies.remove_tally(user_num)
    except ValueError:
        user_tallies.remove_tally(user_input)

def main():
    user_tallies = UserTallies()
    
    commands = {
        1: add_user,
        2: remove_user,
        3: add_tally,
        4: remove_tally,
        5: lambda _: print("\nGreat... now you're rage quitting too...\n") or exit(),
    }
    
    try:
        while True:
            user_tallies.print_data()
            print("_______________")
            print("\nCommands:")
            print("| 1. Add User")
            print("| 2. Remove User")
            print("| 3. Add Tally")
            print("| 4. Remove Tally")
            print("| 5. Quit")
            
            # Wait for user input and validate it
            command = input("Enter a command number: ")
            try:
                command = int(command)
            except ValueError:
                print("\nInvalid command number!")
                continue
            
            # Call the corresponding command function
            if command in commands:
                commands[command](user_tallies)
            else:
                print("\nInvalid command number!")
    except KeyboardInterrupt:
        print("Great... now you're rage quitting too...\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
