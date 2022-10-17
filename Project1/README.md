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
| Task No | Planned Action        | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|-----------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min        | Sep 24                 | B         |


## Works Cited
1. CoinDesk. “Tether Price | USDT Price Index and Chart.” CoinDesk, https://www.coindesk.com/price/tether/. Accessed 23 September 2022.
2. Hicks, Coryanne. “What Is Tether? How Does It Work? – Forbes Advisor INDIA.” Edited by Farran Powell. Forbes, 5 September 2022, https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-tether-usdt/. Accessed 23 September 2022.
3. Kriptomat. “What is Tether? And how does USDT work? (2022 edition).” Kriptomat, https://kriptomat.io/cryptocurrencies/tether/what-is-tether/. Accessed 23 September 2022.
4. Sandor, Krisztian. “What Is Tether? How USDT Works and What Backs Its Value.” CoinDesk, 1 June 2022, https://www.coindesk.com/learn/2022/06/01/what-is-tether-how-usdt-works-and-what-backs-its-value/. Accessed 23 September 2022.
5. Tether Operations Limited. “About Tether.” Tether, https://tether.to/en/about-us. Accessed 23 September 2022.
6. https://medium.com/@mindfiresolutions.usa/python-7-important-reasons-why-you-should-use-python-5801a98a0d0b
7. https://www.simplilearn.com/why-python-is-essential-for-data-analysis-article#:~:text=Thanks%20to%20Python's%20focus%20on,needs%20when%20using%20older%20languages.
8. https://www.geeksforgeeks.org/python-for-data-science/#:~:text=One%20of%20the%20main%20reasons,more%20suited%20for%20quick%20prototyping.
9. 
