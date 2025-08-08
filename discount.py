def apply_discount(total):
    if total > 1000:
        discount = 0.10 * total
        return f"Discount: ₹{discount}, Final: ₹{total - discount}"
    else:
        return f"No discount. Pay ₹{total}"

# Ask user for input
user_input = float(input("Enter the total amount: ₹"))
print(apply_discount(user_input))
