#strip method removes characters both on left and right based on an argument (a string specifying the set of characters to remove)
email = input("Enter your email: ").strip()
#index() is an inbuilt function in Python, which searches for a given element from the start of the list and returns the lowest index where the element appears
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format = (f"Your username is '{username}' and your domain is '{domain_name}' ")
print(format)