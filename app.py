import calc as ca 


user_data={
    "username":"ezhilan",
    "acc no"  : 7537688133,
    "pin"     : 2005,
   "total_bal": 12000
}


def user_info():

    if user_data and user_data["username"]:
        return f"hi welcome user {user_data['username']} your acc.no is {user_data['acc no']}"
    else:
        False

def withdrawn(withdrawal_amt):
    if withdrawal_amt > user_data["total_bal"]:
        return False
    else:
        amount=ca.withdraw_calc(user_data["total_bal"],withdrawal_amt)
        user_data["total_bal"]=amount
        return amount 
def deposit(deposit_amount):
    if deposit_amount:
        amount=ca.deposit_calc(user_data["total_bal"],deposit_amount)
        user_data["total_bal"]=amount
        return amount
def check_bal():
      return user_data["total_bal"]


def main():
      print("welcome to AtM")
      print("="*20)

      pin=int(input("enter your pin no to proceed: "))

      if pin ==user_data["pin"]:
          print(user_info())

          while True:
              choice=int(input("1. withdraw\n2. deposit\n3. check balance\n4. exit\n Enter your choice: "))

              match choice:
                  case 1: 
                      amount=int(input("ENTER THE AMOUNT TO WITHDRAW: "))
                      withdraw_respone=withdrawn(amount)
                      if withdraw_respone is not False:
                          print(f"your withdraw amount is suceesfull, your total balance is {withdraw_respone}")
                      else:
                          print("Insufficient balaance") 
                  case 2: 
                      amount=int(input("Enter your deposit amount: "))
                      print(f"your amount deposit sucessfully, your total balance is {deposit(amount)}") 
                  case 3:
                      print(f"your balance is {check_bal()}")
                  case 4:
                      print("===THANKS FOR USING ATM===")
                      break
                  case _:
                      print("Invalid input,please Enter the between 1 to 4")
      else:
          print("INVALID PIN TRY AGAIN")
          return
if __name__=="__main__":
        main()
             
                  
