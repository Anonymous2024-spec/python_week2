# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.



def calculate_discount(price, discount_percent):
    # If discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Otherwise, return the original price
        return price

try:
    # Prompt the user to enter the original price and discount percentage
    price = float(input("Enter original price: "))
    discount_percent = float(input("Enter discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the final price with a message
    if discount_percent >= 20:
        print(f"Discount applied! The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for both price and discount percentage.")
