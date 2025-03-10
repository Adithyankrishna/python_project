def deposit():
    while True:
        amout = input("what would you like to deposit")
        if amout.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("amount must be greater than zero")
    return amount
