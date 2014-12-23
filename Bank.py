class Operations:
    def __init__(self, bal, log):
        Operations.self = self
        self.bal = bal
        self.log = log

    def error(self, errorType):
        # check the parameter for the type of error called
        if errorType == "value":
            print("You do not appear to have entered a valid number.")
        elif errorType == "unrecog":
            print("Sorry, your command was not recognised.")
        elif errorType == "overdraft":
            print("Sorry, that would breach your overdraft limit of £-100.")
        else:
            print("We are sorry, an error has occured.")

    def deposit(self, log):
        valid = False
        # user enters amount, test if it is a valid number or not
        # also checks if the user is breaching their overdraft
        # continue letting the user enter until the input is valid
        # when the result is valid, the while loop is exited
        while not valid:
            try:
                amt = float(input("Please enter the amount you wish to deposit: "))
                while self.bal + amt < -100:
                    self.error("overdraft")
                    amt = float(input("Please enter the amount you wish to deposit: "))
                valid = True
            except ValueError:
                self.error("value")
        # add amt to bal
        self.bal += amt
        # record transaction to log and say thank you to user
        log.append("DEPOSIT \t\t £{}\n".format(amt))
        print("Thank you for your deposit.")

    def withdraw(self, log):
        valid = False
        # user enters amount, test if it is a vald number or not
        # also checks if the user is breaching their overdraft
        # continue letting the user enter until the input is valid
        # when the result is valid, the while loop is exited
        while not valid:
            try:
                amt = float(input("Please enter the amount you wish to withdraw: "))
                while self.bal - amt < -100:
                    self.error("overdraft")
                    amt = float(input("Please enter the amount you wish to withdraw: "))
                valid = True
            except ValueError:
                self.error("value")

        # minus amt from bal
        self.bal -= amt
        # record transaction log
        log.append("WITHDRAW \t\t £{}\n".format(amt))
        print("Thank you for your withdrawal.")

        

class Run:
    choice = 0
    op = Operations(100, ["TRANSACTION TYPE \t AMOUNT\n"])
    while choice != 3:
        print("Your balance is £{}".format(op.bal))
        valid = False
        # user enters their choice, check if it is a valid number or not
        # while loop runs until it is valid
        while not valid:
            try:
                choice = int(input("Please enter 1 to deposit, 2 to withdraw or 3 to exit: "))
                valid = True
            except ValueError:
                op.error("value")
        #check the user's choice and call the required function
        if choice == 1:
            op.deposit(op.log)
        elif choice == 2:
            op.withdraw(op.log)
        elif choice != 3:
            op.error("unrecog")

    # open statement file
    file = open("statement.txt","w")
    # write each value in the log variable to the statement file
    for entry in op.log:
        file.write(entry)
    file.write("\nCLOSING BALANCE: £{}.".format(op.bal))
    # close file connection
    file.close()
    print("Your statement is now available in the file 'statement.txt'.")
    print("Thank you for using the bank, your closing balance is £{}.".format(op.bal))
            
            
    
    
