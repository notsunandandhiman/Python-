def calculate_due_amount(total_bill, amount_paid):
    return total_bill - amount_paid

total_bill = float(input("Enter total bill: "))
amount_paid = float(input("Enter amount paid: "))

print("Due amount: ", calculate_due_amount(total_bill, amount_paid))