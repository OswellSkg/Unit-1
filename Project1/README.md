# Crypto Wallet

<img src="https://cdn.dribbble.com/users/517178/screenshots/2985223/media/c5522f99c193c84dec23be8bfa102f86.gif"></img>

<a href="https://dribbble.com/shots/2985223-Wallet" target="_blank"><sub>Figure 1: Wallet by ilias chalkiopoulos on Dribbble</sub></a>

# Criteria A: Planning
## Problem definition
Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics.

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution
Design statement: I will to design and make an **Electric Ledger/Crypto Wallet** for a client who is **a local trader(Ms. Sato)**. The **project** will be about **helping her track the amoutn of the cryptocurrency, the transactions, along with useful statistics** and is constructed using the software **Python 3.10.8**. It will take **about 3 weeks** to make and will be evaluated according to the criteria **shown below**.

The digital coin used will be USD Tether.
Tether(USDT) is an asset-backed cryptocurrency stablecoin created by iFinex Inc. in 2014.
Tether's history goes back to a dollar-backed cryptocurrency "realcoin" which was used to transfer fiat currencies on the blockchain. 
It was then rebranded to Tether to what is known today, a coin that provides stable price point to that of USD at all times. 
Tether functions as the digital USD. 

## Justification to proposed solution

USDT is a stable cryptocurrency that is correlated to that of the United States Dollar. Since Ms. Sato is not an experienced trader in cryptocurrency, this stability can bring her a chance to gain experience without a big loss. The USDT can also provide Ms. Sato with an opportunity to further explore and experiment with cryptocurrency of how it works and how it converts to real-life currencies, without any worries that other cryptocurrencies may bring to her. 

I will use the software Python3 to program my digital ledger. Firstly, this is due to the code-readability emphasized syntax of Python that brings efficiency and flexibility to the developer, myself. By using Python3, it allows me and the program to be very sustainable as the software gives me access to easy-maintanance of the program for long-term uses. Secondly, Python3 encourages developers a Test Driven Development style, also known as TDD. This means that Python3 allows me to swiftly create a prototype of the digital ledger, and shape it to become more solid in favor of my client. For that reason, with Python3, I can be more client-friendly and reflect their wills on my program. Thirdly and lastly, Python3 is very commonly used for data analytics. The language will help me and my client to easily work with datas, and easily organize the finances of my client. 


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger password protected to ensure privacy and safety. 
5. The electronic ledger shows the 10 most recent transactions. 
6. The electronic ledger time that the transaction was made.

[Approved]


# Criteria B: Design
## System Diagram
![CS Hardware system diagram](https://user-images.githubusercontent.com/112055140/196055740-de804461-dd54-4e25-a9ca-4afc1fea3ac8.jpeg)

**Figure 2:** The above seen is the system diagram for my digital ledger. The input is from a keyboard. This program is made on a 13-inch MacBook Air(1.1 GHz Dual-Core Intel Core i3) with a macOS Monterey Version 12.2.1. The program is coded on Pycharm2020 with the software Python 3.8. 3 external csv files as well as 1 external library is used. The Transaction_record.csv file securely records the user's transactions in two categories: Deposit and Withdrawal. The Username.csv file holds the recorded Username and Password of the user's account in a different file from the main program to ensure privacy and security. The my_library.csv provides me with access to the validate_int_input function for use in the main program. Lastly, the external library yfinance gives meaccess to conversion rates from USDT to USD, as well as past records of the cryptocurrency that I am working on. The program outputs from the laptop display. 

## Flow Diagrams
### Chart 1: Login System
![ComputerScience-Unit1_Project_1](https://user-images.githubusercontent.com/112055140/196067676-3872323f-28cf-4059-b0bd-12817faed28c.jpg)

**Figure 3:** The chart above is the flowchart for the Login system of my digital ledger.  To verify the user's input, the login system refers to a different csv file, and check it against the username and the password recorded in the file. When the user misinputs either the username or the password, the login system will automatically exit the program. On the other hand, if the user properly inputs both the correct username and password within the given 3 chances, the login system will allow the user to move on to the main menu.


### Chart 2: Wallet Balance system
![ComputerScience-Unit1_Project_2](https://user-images.githubusercontent.com/112055140/196067681-91b25655-ba46-4fb0-a179-7209b5e9afb6.jpg)

**Figure 4:** The chart above is the flowchart for the Wallet Balance system for my digital ledger. This part of the program will be seen when the user chooses 2 from the Main Menu. This wallet balance system allows the user to see their balance in both cryptocurrency and United States Dollar. The wallet balance system achieves this by asking the yfinance plugin the conversion rate from USDT to USD and multiplying USDT by the given conversion rate. 

### Chart 3: Transaction History
![ComputerScience-Unit1_Project_3](https://user-images.githubusercontent.com/112055140/196067697-8bb5f7c8-6fe6-4ac3-a924-8055983f7746.jpg)

**Figure 5:** The chart above is the flowchart for the Transaction History system for my digital ledger. This part of the program will be seen when the user chooses 4 from the Main Menu. This Tranaction History system allows the user to see their transaction history, that is recorded on a different csv file. The system will access the csv record and list down the transactions made for the user to see. This system will skip the first line as the transaction record only starts from the second line.


## Record of Tasks
| **Task No.** | **Planned Action**                                                                                                                            | **Planned Outcome**                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Time estimate** | **Target completion date** | **Criterion** |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------|---------------|
| 1            | Create system diagram                                                                                                                         | To have a clear idea of the <br>hardware and software requirements for the proposed solution                                                                                                                                                                                                                                                                                                                                                                       | 10 min            | Sep 24                     | B             |
| 2            | Identifying the client's need<br>(Problem definition) and defining<br>their specifications(Success Criteria)                                  | Clear vision of client's will, functions <br>to implement in the digital ledger                                                                                                                                                                                                                                                                                                                                                                                    | 30 min            | Sep 24                     | A             |
| 3            | Discuss with the client proposed solution<br>as well as approval for success criteria                                                         | Solidified image of what I aim the digital ledger to be<br> in regards to the client's wills and intentions                                                                                                                                                                                                                                                                                                                                                        | 30 min            | Sep 25                     | A             |
| 4            | Review system diagram and make adjustments                                                                                                    | Solidified structure of the digital ledger<br>(Login system, Main menu, Functions, External csv files, libraries, etc.)                                                                                                                                                                                                                                                                                                                                            | 1 hour            | Sep 27th                   | B             |
| 5            | Program the Login System                                                                                                                      | Coded login system based on an external csv file                                                                                                                                                                                                                                                                                                                                                                                                                   | 1 hour            | Oct 1st                    | C             |
| 6            | Program Menu, <br>Connect it with Login System and Functions                                                                                  | Menu, Login system and skeleton functions(not coded yet) interconnected. <br>Solidified structure of the digital ledger.                                                                                                                                                                                                                                                                                                                                           | 1 hour            | Oct 1st                    | C             |
| 7            | Fix any bugs and learn library yfinance                                                                                                       | Interdependency between Login System, Menu, and simply coded functions tested.<br> - Login system properly provides access to Menu<br> - Menu selection properly provides access to designated functions<br> - Can properly exit program from menu                                                                                                                                                                                                                 | 45 minutes        | Oct 1st                    | C             |
| 8            | Improve code-readability <br>for future developments and maintenance                                                                          | Code-readability of the structure improved. <br> - Better efficiency for further development(Programming the functions)                                                                                                                                                                                                                                                                                                                                            | 14 minutes        | Oct 1st                    | C             |
| 9            | Program basic_description function                                                                                                            | Finished coding of the basic_description function: <br> - Basic description of the USD Tether clearly explained<br> - Sources cited<br> - Returns to main menu post-execution of the function                                                                                                                                                                                                                                                                      | 30 minutes        | Oct 3rd                    | C             |
| 10           | Program wallet_balance function                                                                                                               | Finished coding of the wallet_balance function: <br> - function connected to external csv file that records crypto total balance of client<br> - function connected to yfinance to obtain live conversion rate<br> - function designed to show USDT and USD values of cryptocurrency<br> - Returns to main menu post-execution of the function                                                                                                                     | 1 hour            | Oct 3rd                    | C             |
| 11           | Program withdraw_deposit function                                                                                                             | Finished coding of the withdraw_deposit function:<br> - [Deposit,Withdrawal,Return to Main Menu,Exit] options created<br> - Each options programmed<br> - [Deposit, Withdrawal] interconnected to external csv database for write and read<br> - [Return to Main Menu,Exit] revised to ensure efficiency<br> - After each option executed, the program brings user back to the list of options<br> - Returns to main menu when "Main Menu" option selected by user | 2 hours           | Oct 3rd                    | C             |
| 12           | Program transaction_history function                                                                                                          | Finished coding of the transaction_history function:<br> - Function interconnected to external csv database for read<br> - Returns to main menu post-execution of the function                                                                                                                                                                                                                                                                                     | 1 hour            | Oct 3rd                    | C             |
| 13           | Program past_record function                                                                                                                  | Finished coding of the past_record function:<br> - Function connected to yfinance to obtain past records of USDT<br> -                                                                                                                                                                                                                                                                                                                                             | 30 minutes        | Oct 3rd                    | C             |
| 14           | Program Exit function                                                                                                                         | Finished coding of the exit function:<br> - Function properly executed only upon user choosing exit option from main menu                                                                                                                                                                                                                                                                                                                                          | 30 minutes        | Oct 3rd                    | C             |
| 15           | Improve code-readability for all functions and <br>fix interconnection bugs between Login system, <br>functions, and external files/libraries | Code-readability of the functions improved, <br>interconnection between Login System, functions and external csvs/libraries tested,<br>Program code organized by sections roughly divided into four: <br> - Initial Setup<br> - Login Page<br> - Functions<br> - Main Page                                                                                                                                                                                         | 1 hour            | Oct 4th                    | C             |
| 16           | Overall bugs fixed                                                                                                                            | Overall coding of the program reviewed, fixed, <br>and enhanced of code-readability and overall structure                                                                                                                                                                                                                                                                                                                                                          | 1 hour            | Oct 4th                    | C             |
| 17           | Design and user-friendliness enhanced                                                                                                         | The designs of the program is made improved:<br> - colorful design to enhance (Design)<br> - Easy-to-comprehend text, use-of-word (User-friendliness)<br> - Simplified program structure and interface (User-friendliness)                                                                                                                                                                                                                                         | 1 hour            | Oct 4th                    | C             |
| 18           | Create flowchart for <br>Login System, Wallet Balance System and Transaction History                                                          | 3 flowcharts of from the digital ledger is created to provide the client with an <br>insight into how the digital ledger was created. <br> - Flowcharts are created<br> - They are explained detailedly<br> - These flowcharts provide insight into what python tools are used in the program                                                                                                                                                                      | 2 hours           | Oct 5th                    | B             |
| 19           | Functional tests with 3 different users (non comsci students)                                                                                 | Verify the user-friendliness of the interface and the readability of the program                                                                                                                                                                                                                                                                                                                                                                                   | 15 x 3 = 45 mins  | Oct 5th                    | C             |
| 20           | Finish system diagram                                                                                                                         | Solidify and finalized system diagram based on the digital ledger final product                                                                                                                                                                                                                                                                                                                                                                                    | 30 minutes        | Oct 6th                    | B             |
| 21           | Complete test plan                                                                                                                            | Clear table of test plan finalized in order to help the client visualize the <br>process of testing the program                                                                                                                                                                                                                                                                                                                                                    | 30 minutes        | Oct 7th                    | B             |
| 22           |                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |                            |               |

# Criteria C: Development

## Techniques/Tools used: 
Functions 
For/while loops 
Input Validation 
If statements 

## Login System
```.py
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
            print(f"{colors[1]}You have entered the wrong Username or Password 3 times.\nAccess Denied. Please try again later.{end_code}")
            exit()
    else:
        login_status = True
        print(f"\n{colors[6]}[ACCESS GRANTED.]\nWelcome to your Crypto Wallet, {username_input}.{end_code}")
        break

database.close()
```
The code above allows the user to log into the digital ledger, also known as the crypto wallet. In this code, the user is asked to enter a username and a password. This input is then compared to a username and a password recorded in an external csv file. If the input and the recorded username&password does not match, the program asks the user to retry the input. The program gives the user 3 chances until it automatically exits the program due to exceeding the attempt number limit. If the user successfully inputs the correct username&password, the program breaks the set of doe seen above and proceeds the user to the main menu where they are given options to choose from the functions of the digital ledger. 


## Display wallet balance
```.py
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
```
The code above allows the user to see the wallet balance that they have. The code accesses an external csv database that the transaction records are kept. The code then splits the database per line by the given character to only leave the number of the balance, and remove all other unnecessary variables. With that variable, the code proceeds to convert the given cryptocurrency balance to USD. The code outputs the cryptocurrency balance as well as its value in United States Dollar. 


## Display transaction history
```.py
def transaction_history():
    print(f"\n{colors[11]}[4]TRANSACTION HISTORY:{end_code}")
    with open("Transaction_record.csv", "r") as file:
        record = file.readlines()
        i = 0
        for line in record:
            if i > 0:
                line = line.split(" : ")
                print(line[0] + " : " + line[1])
            i += 1
```
The code above allows the user to see the transaction history(Deposit, Withdrawal). The code accesses an external csv database where the deposit and withdrawal are all recorded and kept. The code above reads the lines of the database, and displays it to the user. 


## Works Cited
1. CoinDesk. “Tether Price | USDT Price Index and Chart.” CoinDesk, https://www.coindesk.com/price/tether/. Accessed 23 September 2022.
2. Hicks, Coryanne. “What Is Tether? How Does It Work? – Forbes Advisor INDIA.” Edited by Farran Powell. Forbes, 5 September 2022, https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-tether-usdt/. Accessed 23 September 2022.
3. Kriptomat. “What is Tether? And how does USDT work? (2022 edition).” Kriptomat, https://kriptomat.io/cryptocurrencies/tether/what-is-tether/. Accessed 23 September 2022.
4. Sandor, Krisztian. “What Is Tether? How USDT Works and What Backs Its Value.” CoinDesk, 1 June 2022, https://www.coindesk.com/learn/2022/06/01/what-is-tether-how-usdt-works-and-what-backs-its-value/. Accessed 23 September 2022.
5. Tether Operations Limited. “About Tether.” Tether, https://tether.to/en/about-us. Accessed 23 September 2022.
6. https://medium.com/@mindfiresolutions.usa/python-7-important-reasons-why-you-should-use-python-5801a98a0d0b
7. https://www.simplilearn.com/why-python-is-essential-for-data-analysis-article
8. https://www.geeksforgeeks.org/python-for-data-science/#:~:text=One%20of%20the%20main%20reasons,more%20suited%20for%20quick%20prototyping.
9. 
