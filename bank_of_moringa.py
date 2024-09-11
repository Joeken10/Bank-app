import sqlite3


def create_database_table():
    db_connection = sqlite3.connect("bank_of_moringa.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "CREATE TABLE IF NOT EXISTS bank_users(id INTEGER PRIMARY KEY AUTOINCREMENT, owners_name TEXT NOT NULL, location TEXT NOT NULL, account_number INTEGER NOT NULL)")
    db_connection.commit()


class BankApplication:
    def __init__(self, owners_name, location, account_number):
        self.owners_name = owners_name
        self.location = location
        self.account_number = account_number

    def __str__(self) -> str:
        return f"Account for {self.owners_name} has been created succesfully, and account number is {self.account_number}"


def main():
    create_database_table()

    print("welcome to bank of moringa")

    while True:
        print("Menu Option")
        print("1. Create an account")
        print("2. Exit")

        menu_option = input("choose from menu option: ")
        if menu_option == "1":
            owner_name = input("Enter full name: ")
            location = input("Enter your location: ")
            account_number = input("Enter account number: ")

            db_connection = sqlite3.connect("bank_of_moringa.db")
            db_cursor = db_connection.cursor()
            db_cursor = db_cursor.execute("SELECT *FROM bank_users WHERE account_number = ?",(account_number,))
            results = db_cursor.fetchone()

            if results:
                print("Account already exist!!!!")
            
            else:
                 db_connection = sqlite3.connect("bank_of_moringa.db")
            db_cursor = db_connection.cursor()
            db_cursor = db_cursor.execute("INSERT INTO bank_users(owners_name, location, account_number) VALUES(?, ?, ?)", (owner_name, location, account_number) )
            db_connection.commit()
            db_connection.close()
            print(f"account for {owner_name} has been created successfully,account number is{account_number}")


        while True:
          print("Menu options")
          print("1. Create an account")
          print("2. Exit")

          menu_options = input("Choose from menu options: ")

          if menu_options == "1":
              create_database_table()
          elif menu_options == "2":
              break
          else:
              print("Invalid option, choose correct option again.")


if __name__ == "__main__":
    main()
