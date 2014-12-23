
class Type:
    def __init__(self, password, numbers, upper, lower, total):
        # define each of the variables used in the program.
        # the values upper, numbers, lower and total should be lists for mutability.
        Type.self = self
        self.password = password
        self.numbers = numbers
        self.upper = upper
        self.lower = lower
        self.total = total

        return

        
    def checkType(self, password, numbers, upper, lower, total):
        for letter in password:
            up = letter.isupper()
            low = letter.islower()
            num = letter.isdigit()
            if up == True:
                upper[0] += 1
            elif low == True:
                lower[0] += 1
            elif num == True:
                numbers[0] += 1

        values = (numbers[0], upper[0], lower[0])
        for val in values:
            if val < 1:
                total[0] -= 1
        
        return
    
    def checkStrength(self, total):
        if total[0] < 2:
            print("Your password is weak. ")
        elif total[0] < 3:
            print("Your password is medium.")
        else:
            print("Your password is strong.")

class Execute:
        t = Type(str(input("Please enter a password: ")),[0],[0],[0],[3])
        while len(t.password) < 6 or len(t.password) > 12:
            if len(t.password) < 6:
                t.password = str(input("Sorry, your password is too short. Please enter a password between 6 and 12 characters: "))
            elif len(t.password) > 12:
                t.password = str(input("Sorry, your password is too long. Please enter a password between 6 and 12 characters: "))
        else:
            t.checkType(t.password,t.numbers,t.upper,t.lower,t.total)
            t.checkStrength(t.total)
    
