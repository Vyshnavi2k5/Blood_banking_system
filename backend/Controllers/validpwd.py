#Write a Python program that asks the user to enter a password using input(), 
#checks if it contains uppercase, lowercase, digits and special characters, 
#then validates and prints the strength as Weak, Medium or Strong. Also generate 
#a random strong password using random and string modules. Add proper comments 
#for each step and display sample outputs in comments. also take user input
import random
import string
def check_password_strength(password):
    # Initialize strength level
    strength = "Weak"
    
    # Check for uppercase, lowercase, digits and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Determine strength based on criteria
    if has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif (has_upper and has_lower) or (has_upper and has_digit) or (has_lower and has_digit):
        strength = "Medium"
    
    return strength