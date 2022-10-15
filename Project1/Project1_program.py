# Project 1 - Crypto Wallet(Electronic Ledger)

# Success Criteria
# The electronic ledger is a text-based software (Runs in the Terminal).
# The electronic ledger display the basic description of the cyrptocurrency selected.
# The electronic ledger allows to deposit, withdraw and record transactions.
# The electronic ledger password protected to ensure privacy and safety.
# The electronic ledger shows the 10 most recent transactions.
# The electronic ledger shows the time that the transaction was made.



## Initial Setup ##

# Importing Modules #
import yfinance as yf
from my_library import validate_int_input

# Defining Variables #
crypto = "USDT-USD"
crypto_name = "Tether"
ChosenTicker = yf.Ticker(crypto)
colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m",
          "\033[0;37m", "\033[0;38m", "\033[0;39m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m",
          "\033[0;44m", "\033[0;45m", "\033[0;46m", "\033[0;47m", "\033[0;48m", "\033[0;49m", "\033[0;50m",
          "\033[0;51m", "\033[0;52m", "\033[0;53m", "\033[0;54m", "\033[0;55m", "\033[0;56m", "\033[0;57m",
          "\033[0;58m", "\033[0;59m", "\033[0;60m", "\033[0;61m", "\033[0;62m", "\033[0;63m", "\033[0;64m",
          "\033[0;65m", "\033[0;66m", "\033[0;67m", "\033[0;68m", "\033[0;69m", "\033[0;70m", "\033[0;71m",
          "\033[0;72m", "\033[0;73m", "\033[0;74m", "\033[0;75m", "\033[0;76m", "\033[0;77m", "\033[0;78m",
          "\033[0;79m", "\033[0;80m", "\033[0;81m", "\033[0;82m", "\033[0;83m", "\033[0;84m", "\033[0;85m",
          "\033[0;86m", "\033[0;87m", "\033[0;88m", "\033[0;89m", "\033[0;90m", "\033[0;91m", "\033[0;92m"]
end_code = "\033[00m"

## End of Initial Setup ##



## Landing Page ##

def Landing_Page():
    print(f"{colors[4]}Welcome to the Crypto Wallet{end_code}".center(90,"=") +
          "\n" + f"{colors[3]}(Electronic Ledger){end_code}".center(90,"=") +
          "\n" + f"{colors[4]}This is a simple electronic ledger that allows you to record transactions.{end_code}" +
          "\n" + f"{colors[4]}The electronic ledger is password protected to ensure your privacy and safety.{end_code}" +
          "\n" +
          "\n" + "◈".center(52, "◈") +
          "\n" + "◈".center(52, "◈") +
          "\n")
Landing_Page()

## End of Landing Page ##

## Login Page ##


print("|" + "".center(50, "▔") + "|" +
      "\n" + "|" + "LOGIN PAGE".center(50," ") + "|" +
      "\n" + "|" + "Enter your username and password to continue.".center(50," ") + "|" +
      "\n" + "|" + "".center(50,"▁") + "|")

pass_wrong_count = 0
username_input = input("Username:")
password_input = input("Password:")

login_status = False

while pass_wrong_count < 3:
    database = open("username.csv", "r")
    for line in database:
        line = line.split(",")
    while username_input != line[0] or password_input != line[1]:
        pass_wrong_count += 1
        if pass_wrong_count < 3:
            print(f"{colors[1]}ERROR: Incorrect Username or Password{end_code}" + "\n" + f"{colors[1]}Please try again.{end_code}" + "\n")
            username_input = input("Please input your Username:")
            password_input = input("Please input your Password:")
        elif pass_wrong_count == 3:
            print(f"{colors[1]}You have entered the wrong Username or Password 3 times.{end_code}")
            print(f"{colors[1]}Access Denied. Please try again later.{end_code}")
            exit()
    else:
        login_status = True
        print(f"\n{colors[6]}[ACCESS GRANTED.]{end_code}")
        print(f"{colors[6]}Welcome to your Crypto Wallet, {username_input}.{end_code}")
        break

database.close()


## End of Login Page ##




## |~Functions~| ##

def show_menu():
    print("\n" + "◈".center(52, "◈") +
          "\n" + "◈".center(52, "◈") +
          "\n" +
          "\n""|" + "".center(50, "▔") + "|" +
          "\n" + "|" + "MAIN MENU".center(50," ") + "|" +
          "\n" + "|" + "1. View Basic Description of Cryptocurrency".center(50, " ") + "|" +
          "\n" + "|" + "2. View Wallet Balance (USDT and USD)".center(50, " ") + "|" +
          "\n" + "|" + "3. Deposit & Withdraw (Record a Transaction)".center(50, " ") + "|" +
          "\n" + "|" + "4. View 10 Past Recent Transaction Records".center(50, " ") + "|" +
          "\n" + "|" + "5. Past record of the cryptocurrency".center(50, " ") + "|" +
          "\n" + "|" + "6. Exit".center(50, " ") + "|" +
          "\n" + "|" + "".center(50, "▁") + "|")

def basic_description():
    crypto_description = (f'''\n{colors[11]}[1]BASIC DESCRIPTION OF TETHER:{end_code}
{colors[5]}Tether(USDT) is an asset-backed cryptocurrency stablecoin created by iFinex Inc. in 2014 that is pegged to the US dollar. 
Tether's history goes back to a dollar-backed cryptocurrency "realcoin" which was used to transfer fiat currencies on the blockchain. 
It was then rebranded to Tether to what is known today, a coin that provides stable price point to that of USD at all times. 
Tether functions as the digital USD.{end_code}
(Source Cited:
 - CoinDesk. “Tether Price | USDT Price Index and Chart.” CoinDesk, https://www.coindesk.com/price/tether/. Accessed 23 September 2022.
 - Hicks, Coryanne. “What Is Tether? How Does It Work? – Forbes Advisor INDIA.” Edited by Farran Powell. Forbes, 5 September 2022, https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-tether-usdt/. Accessed 23 September 2022.
 - Kriptomat. “What is Tether? And how does USDT work? (2022 edition).” Kriptomat, https://kriptomat.io/cryptocurrencies/tether/what-is-tether/. Accessed 23 September 2022.
 - Sandor, Krisztian. “What Is Tether? How USDT Works and What Backs Its Value.” CoinDesk, 1 June 2022, https://www.coindesk.com/learn/2022/06/01/what-is-tether-how-usdt-works-and-what-backs-its-value/. Accessed 23 September 2022.
 - Tether Operations Limited. “About Tether.” Tether, https://tether.to/en/about-us. Accessed 23 September 2022.)''')
    print(crypto_description)

def main_menu():
    pass

def wallet_balance():
    print(f"\n{colors[11]}[2]WALLET BALANCE:{end_code}")
    with open("Transaction_record.csv", "r") as file:
        wallet = file.readlines()
        i = 0
        for line in wallet:
            if i > 0:
                data = line.split(" : ")
                data = line.split(",")
                # print(data)
                balance = float(data[3])
            i += 1
    print(f"{colors[6]}Loading...{end_code}")
    temp = f"You currently have {colors[1]}{balance} {crypto_name}{end_code} in your wallet, which is currently worth {colors[1]}{round(balance * float(ChosenTicker.info['regularMarketPrice']), 2)} USD{end_code}."
    print(temp)

def withdraw_deposit():
    print(f"\n{colors[11]}[3]DEPOSIT/WITHDRAW:{end_code}")
    print("""    1. Deposit
    2. Withdraw
    3. Return to Main Menu
    4. Exit
    """)
    option_input = validate_int_input("Please select an option: ")

    if option_input == 1:
        print("\n" + f"{colors[14]}Deposit USD Tether{end_code}".center(50, "="))
        deposit_input = int(input("Deposit Amount: "))
        date = input("Please enter the date of the transaction(MM/DD/YYYY): ")
        time = input("Please enter the time of the transaction(HH:MM): ")
        with open("Transaction_record.csv", "r") as file:
            record = file.readlines()
            i = 0
            for line in record:
                if i > 0:
                    line = line.split(" : ")
                    line = line[1].split(",")
                    temp = line[3]
                    temp = temp.replace("\n", "")
                    balance = float(temp) + deposit_input
                i += 1
        with open("Transaction_record.csv", "a") as file:
            file.write(f"\nDeposit : {date},{time},{deposit_input},{balance}")
            print(f"\n{colors[6]}[Deposit Successful]{end_code}")
            print(f"{colors[6]}Current Balance: {end_code}{colors[1]}{balance} Tether{end_code}")
            print(f"{colors[6]}Redirecting you back to Deposit/Withdraw Menu...{end_code}")
        withdraw_deposit()

    elif option_input == 2:
        print("\n" + f"{colors[14]}Withdraw USD Tether{end_code}".center(50, "="))
        withdraw_input = int(input("Withdraw Amount: "))
        date = input("Please enter the date of the transaction(MM/DD/YYYY): ")
        time = input("Please enter the time of the transaction(HH:MM): ")
        with open("Transaction_record.csv", "r") as file:
            record = file.readlines()
            i = 0
            for line in record:
                if i > 0:
                    line = line.split(" : ")
                    line = line[1].split(",")
                    temp = line[3]
                    temp = temp.replace("\n", "")
                    balance = float(temp)
                i += 1
        if withdraw_input <= balance:
            balance -= withdraw_input
            with open("Transaction_record.csv", "a") as file:
                file.write(f"\nWithdrawal : {date},{time},{withdraw_input},{balance}")
            print(f"\n{colors[6]}[Withdrawal Successful]{end_code}")
            print(f"{colors[6]}Current Balance: {end_code}{colors[1]}{balance} Tether{end_code}")
            print(f"{colors[6]}Redirecting you back to Deposit/Withdraw Menu...{end_code}")
            withdraw_deposit()
        else:
            print(f"\n{colors[1]}[Withdrawal Unsuccessful]{end_code}")
            print(f"{colors[1]}Error: Insufficient Funds.{end_code}")
            print(f"{colors[1]}Redirecting you back to Deposit/Withdraw Menu...{end_code}")
        withdraw_deposit()
        main_menu()

    elif option_input == 3:
        print(f"\n{colors[6]}Redirecting you back to Main Menu...{end_code}")
        main_menu()

    elif option_input == 4:
        print(f"{colors[1]}Exiting...{end_code}")
        exit()

def transaction_history():
    print(f"\n{colors[11]}[4]TRANSACTION HISTORY:{end_code}")
    with open("Transaction_record.csv", "r") as file:
        record = file.readlines()
        for line in record:
            print(line)

def past_records():
    # gets past month(based on current date) of data of the cryptocurrency from the plugin yfinannce and print it for the user
    Past_record = ChosenTicker.history(period="1mo")
    print(Past_record)

## |~End of Functions~| ##




## Main Page ##

while login_status == True:
    show_menu()
    choice = validate_int_input("Please enter your choice[1~6]: ")
    if choice == 1:
        basic_description()
    elif choice == 2:
        wallet_balance()
    elif choice == 3:
        withdraw_deposit()
    elif choice == 4:
        print("\n")
        transaction_history()
    elif choice == 5:
        print("\n")
        print(f"{colors[1]}View Past Records of the Cryptocurrency{end_code}")
        past_records()
    elif choice == 6:
        print("\n")
        print(f"{colors[1]}Exiting...{end_code}")
        exit()
    else:
        print(f"{colors[1]}Invalid Input. Please enter your choice[1~6]: {end_code}")
        main_menu()


## Main Page ##
