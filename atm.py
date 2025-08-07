def atm_withdraw(amount,balance):
    if amount % 100 !=0:
     return "amount should be multiple of 100"
    elif amount>balance:
     return "insuficient balance"
    else:
         balance -=amount
         return f"withdraw:{amount}.remaining balance:{balance}"
print(atm_withdraw(1200,5000))

    