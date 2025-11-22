"""this the program to solve day to day life problem of how to manage there finencial record and how to make a good use of there
    money , so this program will collect the data of the person expenses, there income and give a detail tabuler report on how
    much the person spend and his/her remaning money as well."""


def spending_money():  #this is a function that will get the user expenses and return the type of spending and amount in a list. 
    spending=[]
    print("enter the spending you made (type done to finish.)")
    while True:       #loop to take multiple input for the user until he/she type done. 
        type_of_spending=input("Enter where you spend your money:").lower()
        if type_of_spending =="done":
            break
        else:
            try:                             
                amount=float(input("Enter the amount of money spend on the services: "))
                spending.append((type_of_spending,amount))
            except ValueError:
                print("the input is not valid(use numbers only!)")
    return spending

def body():
    #in this first the income is ask and then all the calculation is done then print the fomate as shown.
    print("----------BUDGET TRACKING SYSTEM----------")
    __income__=float(input("enter your monthly income: ₹"))
    pays= spending_money()
    total_spending=sum(amount for type_of_spending, amount in pays)
    balance= (__income__-total_spending)
        
    print("***************BUDGET REPORT***************")
    print(f"monthly income: ₹{__income__}")
    print()
    print("type of spending"," "*12,"amount")
    print("-"*43)

    for spending , amount in pays: #this loop is use to get the values of amount and spending from the variable pays
        print("{:<26}{:>10}".format(spending,amount))

    #the formate functon is builtin function of pythom which can formate the print statement like it was used :< means that for the string set the width from the right,
    #similearly :> this is for the values of that string making the width finite from left.
    print("-"*43)
    print("{:<26}{:>10}".format("your monthly expenses",total_spending))
    print("{:<26}{:>10}".format("balance",balance))
    print("*********************end*********************")

if __name__== body:
    body()