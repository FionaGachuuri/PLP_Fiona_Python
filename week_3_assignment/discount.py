#!/usr/bin/env python3
"""
This module calculates the final price of a product after a discount
"""

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage

    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Validate inputs
    if original_price < 0 or discount_percentage < 0:
        print("Error: Price and discount percentage cannot be negative.")
    else:
        # Calculate and display the final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Check if discount was applied
        if discount_percentage >= 20:
            saved_amount = original_price - final_price
            print(f"A {discount_percentage}% discount was applied.")
            print(f"Original price: ${original_price:.2f}")
            print(f"You saved: ${saved_amount:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. The discount percentage ({discount_percentage}%) is less than 20%.")
            print(f"Final price: ${final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
