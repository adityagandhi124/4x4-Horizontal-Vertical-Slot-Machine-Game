import random 


# 1. write a function to find how much money the user is depositing 
# 2. function that asks the user how many lines he or she is betting 
# 3. function that asks the user her total bet amount / by the lines she is betting

# This slot machine is going to be 4 x 4 
MAX_ROWS = 4
MAX_COLUMNS = 4

SYMBOLS = {
    "A" : 10, 
    "B" : 10, 
    "C" : 10, 
    "D" : 10
}

MULTIPLIER = {
    "A" : 10, 
    "B" : 8, 
    "C" : 3, 
    "D" : 2 
}

def DEPOSIT(USER_NAME = "NAME NOT DISCLOSED TO CASINO"):  
    while (True): 
        USER_INPUT = input('How much money do you want to deposit: ')
        
        if USER_INPUT.isdigit: 
            DEPOSIT = float(USER_INPUT) 
            if(DEPOSIT <= 0): 
                x = True
                print('Invalid deposit - enter the money you want to deposit')
            else: 
                break
        else: 
            print("Please enter a number")
    
    print(f"{DEPOSIT:.2f}$ in {USER_NAME}'s account")
    
    return DEPOSIT


def LINES_BET():
    while(True): 
         USER_INPUT = input('How many lines would you like to bet on (Range: 1 <= x <= 4): ')
         if USER_INPUT.isdigit(): 
            LINES = float(USER_INPUT)
            if(LINES < 1 or LINES > 4): 
                print("Please select again, lines need to be between 1 - 4")
            else: 
                break 
         else: 
            print("Please enter a number")

    print(f"You have selected to bet {LINES}")
    return LINES

def LINES_BET_BONUS_DIAGONAL(): 
    while (True): 
        USER_INPUT = input('How many diagonal lines would you like to bet on? ')
        if USER_INPUT.isdigit():
            LINES = int(USER_INPUT)
            if(LINES < 1 or LINES > 2):
                print("Please select again, lines need to be between 1- 2")
            else: 
                break
        else: 
            print("Please enter a number")

    print(f"You have selected to bet {LINES}")
    return LINES

def LINES_BET_BONUS_COLUMN(): 
    while (True): 
        USER_INPUT = input('How many column lines would you like to bet on? ')
        if USER_INPUT.isdigit():
            LINES = int(USER_INPUT)
            if(LINES < 1 or LINES > 2):
                print("Please select again, lines need to be between 1- 2")
            else: 
                break
        else: 
            print("Please enter a number")

    print(f"You have selected to bet {LINES}")
    return LINES

def MONETARY_BET (BALANCE, LINES): 
    while (True): 
        USER_INPUT = input('How much money do you want to bet per line: ')
        if USER_INPUT.isdigit(): 
            MONEY_BET = float(USER_INPUT)
            if MONEY_BET > (BALANCE / LINES): 
                print("Insufficient Funds, please enter a valid bet amount")
            else: 
                break
        else: 
            print("Please enter a number")
    
    print(f"Bet is locked... you have bet {MONEY_BET} ")    
   
    return MONEY_BET


def SPIN():   
    # Example of List Comprehension
    # The first symbol represents the item that will be stored in the resulting array
    # The second symbol represents a loop variable, represents the current key
    # count represents the count associated with the loop variable so "A" = 4 
    # for _ in range(count) means that the loop will iterate 4 times and append "A" to the array
    # Overall, there is one outer loop and one inner loop working
    # #
    MASTER_ARRAY = [symbol for symbol, count in SYMBOLS.items() for _ in range(count)]

    FOURBYFOUR_ARRAY = []
    for i in range(MAX_COLUMNS): 
        COPY_ARRAY = MASTER_ARRAY[:]
        FOURBYFOUR_ARRAY.append([])  
        for _ in range(MAX_ROWS):
             RANDOM_INDEX = random.randint(0, len(COPY_ARRAY) - 1)
             RANDOM_VALUE = COPY_ARRAY[RANDOM_INDEX]
             FOURBYFOUR_ARRAY[i].append(RANDOM_VALUE)
             COPY_ARRAY.remove(RANDOM_VALUE) 

    

    return FOURBYFOUR_ARRAY

def TRANSPOSE_ARRAY (FOURBYFOUR_ARRAY):  
    TRANSPOSED_ARRAY = []
    for i in range(MAX_COLUMNS): 
        TRANSPOSED_ARRAY.append([])
        for j in range(MAX_ROWS): 
            TRANSPOSED_ARRAY[i].append(FOURBYFOUR_ARRAY[j][i]) 

    
    return TRANSPOSED_ARRAY

def PRINT_ARRAY (TRANSPOSED_ARRAY) : 
    for SUB_ARRAY in TRANSPOSED_ARRAY: 
        row = ""
        for INDEX, ELEMENT in enumerate(SUB_ARRAY): 
            row += str(ELEMENT) 
            if(INDEX != len(SUB_ARRAY) - 1): 
                row += " | "        
        print(row)
       

#This code checks rows horiztontally 
def GET_WINNINGS (TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE):
    WINNINGS = 0
    TORF = False 

    for i, SUB_ARRAY in enumerate(TRANSPOSED_ARRAY): 
        if(i < LINES): 
            CHECK_VALUE = SUB_ARRAY[0]
            for j in range(len(SUB_ARRAY)): 
                if (SUB_ARRAY[j] != CHECK_VALUE): 
                    break
                elif (j == (len(SUB_ARRAY) - 1)): 
                    WINNINGS += MULTIPLIER[CHECK_VALUE] * MONEY_BET    
        else: 
            break
    
    if(WINNINGS > 0): 
        BALANCE
        NEW_BALANCE = BALANCE + (WINNINGS) 
        print(f"Hey you have won {WINNINGS:.2f} your balance went from {BALANCE:.2f} to {NEW_BALANCE:.2f}")
    else: 
        TORF = True
        BALANCE
        NEW_BALANCE = BALANCE - (MONEY_BET * LINES)
        print(f"Hey you LOST! your balance decreased from {BALANCE:.2f}$ to {NEW_BALANCE:.2f}$")
    
    return WINNINGS, NEW_BALANCE, TORF  

def BONUS_WINNINGS_DIAGONAL (TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE): 

    WINNINGS = 0 
    LEFT_DIAGONAL_ARRAY = []
    RIGHT_DIAGONAL_ARRAY = []
    MERGE_ARRAY = []

    i = j = 0 

    x = 0
    y = 3

    for _ in range(MAX_COLUMNS): 
        LEFT_DIAGONAL_ARRAY.append(TRANSPOSED_ARRAY[i][j])
        i += 1 
        j += 1
        RIGHT_DIAGONAL_ARRAY.append(TRANSPOSED_ARRAY[x][y])
        x += 1
        y -= 1

    for i in range (LINES): 
        if(i == 0): 
            MERGE_ARRAY.append([])
            for j in range(MAX_ROWS): 
                MERGE_ARRAY[i].append(LEFT_DIAGONAL_ARRAY[j])
        elif(i == 1): 
            MERGE_ARRAY.append([])
            for x in range(MAX_ROWS):
                MERGE_ARRAY[i].append(RIGHT_DIAGONAL_ARRAY[x]) 

    for INDEX, SUB_ARRAY in enumerate(MERGE_ARRAY): 
        if(INDEX < LINES): 
            CHECK_VALUE = SUB_ARRAY[0]
            for i in range(len(SUB_ARRAY)): 
                if(SUB_ARRAY[i] != CHECK_VALUE): 
                    break 
                elif(i == len(SUB_ARRAY) - 1): 
                    WINNINGS += MULTIPLIER[CHECK_VALUE] * MONEY_BET
        else: 
            break 

    if(WINNINGS > 0): 
        BALANCE
        NEW_BALANCE = BALANCE + (MONEY_BET * LINES) 
        print(f"Hey you have won {WINNINGS} your balance went from {BALANCE:.2f}$ to {NEW_BALANCE:.2f}")
    else: 
        BALANCE
        NEW_BALANCE = BALANCE - (MONEY_BET * LINES)
        print(f"Hey you LOST! your balance decreased from {BALANCE:.2f}$ to {NEW_BALANCE:.2f}$")

    return WINNINGS, NEW_BALANCE

def BONUS_WINNINGS_COLUMNS (TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE): 

    WINNINGS = 0 

    if(LINES == 1): 
        CHECK_VALUE = TRANSPOSED_ARRAY[0][1]
        for i in range(MAX_COLUMNS): 
            if(TRANSPOSED_ARRAY[i][1] != CHECK_VALUE): 
                break
            elif(i == (MAX_COLUMNS - 1)): 
                WINNINGS += MULTIPLIER[CHECK_VALUE] * MONEY_BET          
    elif(LINES == 2): 
        for x in range(2): 
            CHECK_VALUE = TRANSPOSED_ARRAY[0][x]
            for y in range(MAX_COLUMNS): 
                if(TRANSPOSED_ARRAY[y][x] != CHECK_VALUE): 
                    break
                elif(y == (MAX_COLUMNS - 1)): 
                    WINNINGS += MULTIPLIER[CHECK_VALUE] * MONEY_BET

    if(WINNINGS > 0): 
        BALANCE
        NEW_BALANCE = BALANCE + (MONEY_BET * LINES) 
        print(f"Hey you have won {WINNINGS} your balance went from {BALANCE:.2f}$ to {NEW_BALANCE:.2f}")
    else: 
        BALANCE
        NEW_BALANCE = BALANCE - (MONEY_BET * LINES)
        print(f"Hey you LOST! your balance decreased from {BALANCE:.2f}$ to {NEW_BALANCE:.2f}$")

    return WINNINGS, NEW_BALANCE



def DIAGONAL_EXAMPLE ():
    SAMPLE_MATRIX = [
        ["A", "C", "D", "B"], 
        ["D", "A", "B", "C"],
        ["C", "B", "A", "D"], 
        ["B", "D", "C", "A"]
    ]

    for SUB_ARRAY in SAMPLE_MATRIX: 
        row = ""
        for INDEX, ELEMENT in enumerate(SUB_ARRAY): 
            row += str(ELEMENT)
            if(INDEX != len(SUB_ARRAY) - 1): 
                row += " | "    
        print(row) 


def COLUMN_EXAMPLE (): 
    SAMPLE_MATRIX2 = [
        ["C", "D", "D", "A"], 
        ["A", "D", "D", "C"], 
        ["C", "D", "D", "B"], 
        ["D", "D", "D", "A"] 
    ]  
    
    for SUB_ARRAY in SAMPLE_MATRIX2: 
        row = ""
        for INDEX, ELEMENT in enumerate(SUB_ARRAY): 
            row += str(ELEMENT)
            if(INDEX != len(SUB_ARRAY) - 1): 
                row += " | "
        print(row)

# #This code checks columns horizontally, and diagonally 
# def BONUS_WINNINGS () : 

def main(): 
    print("-----------------------------------------------------------------------------------------")
    print("Welcome to the Slot Machine Gambling Game")
    print("(1) The game will ask you to enter a bet per row in a randomly generated 4x4 Matrix")
    print("(2) If the row you bet money on has the same letter then you will win money")
    print("(3) If not then you will lose money based on your bet")
    print("(4) If you lose... hope is not lost! You can enter the bonus round to win your money back!")
    print("(5) Have fun and gamble responsibly")
    print("-----------------------------------------------------------------------------------------")

    
    USER_NAME = input('Name of Player: ')
    BALANCE = DEPOSIT.DEPOSIT(USER_NAME)
    
    
    while True: 

        LINES = LINES_BET()
        MONEY_BET = MONETARY_BET(BALANCE, LINES)
        print("----------------------------------------------")
        print("Generating 4x4 Matrix, 3, 2, 1!")
        print("----------------------------------------------")
        FOURBYFOUR_ARRAY = SPIN()
        TRANSPOSED_ARRAY = TRANSPOSE_ARRAY(FOURBYFOUR_ARRAY) 
        PRINT_ARRAY(TRANSPOSED_ARRAY)
        print("----------------------------------------------")
        WINNINGS, BALANCE, TORF = GET_WINNINGS(TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE)

        if TORF: 
            USER_INPUT = input('Hey even though you lost do you want to enter the bonus round to win some more money?... ENTER (Yes/No): ')    
            if(USER_INPUT == "Yes"): 
                print("----------------------------------------------------------------------------------------------------------------------------------")
                print("Since you selected 'Yes', let me explain to you how the bonus round works:")
                print("A new 4x4 matrix will be generated, and you will win money if the two diagonals or the vertical columns have the same alphabet.")
                print("----------------------------------------------------------------------------------------------------------------------------------")

                print("Here is an example of a matrix with matching diagonals:")
                DIAGONAL_EXAMPLE()
                print("----------------------------------------------------------------------------------------------------------------------------------")

                print("Here is an example of a matrix with matching middle columns:")
                COLUMN_EXAMPLE()
                print("----------------------------------------------------------------------------------------------------------------------------------")
                while True:
                    SELECTION = input('Do you want to bet on matching diagonals or matching columns? Select (DG/COL): ')
                    if SELECTION != "DG" and SELECTION != "COL":
                        continue
                    else:
                        break
                print("----------------------------------------------------------------------------------------------------------------------------------")
                
                if(SELECTION == "DG"): 
                    LINES = LINES_BET_BONUS_DIAGONAL()
                    MONEY_BET = MONETARY_BET(BALANCE, LINES)
                    print("----------------------------------------------")
                    print("Generating BONUS, 4x4 Matrix, 3, 2, 1!")
                    print("----------------------------------------------")
                    FOURBYFOUR_ARRAY = SPIN()
                    TRANSPOSED_ARRAY = TRANSPOSE_ARRAY(FOURBYFOUR_ARRAY)
                    PRINT_ARRAY(TRANSPOSED_ARRAY)
                    WINNINGS, BALANCE = BONUS_WINNINGS_DIAGONAL(TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE)           
                elif(SELECTION == "COL"): 
                    LINES = LINES_BET_BONUS_COLUMN() 
                    MONEY_BET = MONETARY_BET(BALANCE, LINES)
                    print("----------------------------------------------")
                    print("Generating BONUS, 4x4 Matrix, 3, 2, 1!")
                    print("----------------------------------------------")
                    FOURBYFOUR_ARRAY = SPIN()
                    TRANSPOSED_ARRAY = TRANSPOSE_ARRAY(FOURBYFOUR_ARRAY)
                    PRINT_ARRAY(TRANSPOSED_ARRAY)
                    WINNINGS, BALANCE = BONUS_WINNINGS_COLUMNS(TRANSPOSED_ARRAY, MONEY_BET, LINES, BALANCE)

            else: 
                print(f"Round is finished, you have {BALANCE:.2f}")
        
        CONTINUATION = input('Round is finished, would you like to play again? (Yes/No)? ')
        if(CONTINUATION == "Yes"): 
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------------------------------------------------------------")
            continue
        elif(CONTINUATION == "No"): 
            break



    
    
    print("Program is finsihed")        
    



main() 