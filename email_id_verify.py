email = input("Enter gmail:")  # Prompt the user to enter an email address

if email.count("@") > 1:  # Check if "@" appears more than once
    print("Invalid Email Id")
    exit()



t = email.partition("@")  # Split the email address into username, "@" symbol, and company domain
print(t)
username = t[0]  # Extract the username from the tuple
company_domain = t[2]  # Extract the company domain from the tuple


if email[0].isdigit()==True or len(username)==0:
    print("Invalid email")
    exit()


check_username = False  # Flag to track username validity
check_company = False  # Flag to track company name validity
check_domain = False  # Flag to track domain validity

# Check each character in the username
for alphabet in username:
    if alphabet.isalpha() or alphabet.isdigit() or "_" in alphabet:
        # If the character is alphanumeric or underscore, continue to the next character
        pass
    else:
        # If an invalid character is encountered, break out of the loop
        break
else:
    check_username = True  # Set check_username to True if the loop completes without breaking

c_d = company_domain.partition(".")  # Split the company domain into company name and domain extension
company = c_d[0]  # Extract the company name from the tuple
domain = c_d[2]  # Extract the domain extension from the tuple

if company.isalnum():  # Check if the company name consists of alphanumeric characters only
    check_company = True  # Set check_company to True if the company name is valid

if len(domain) <= 3 and domain.islower():  # Check if the domain extension is lowercase and has length <= 3
    check_domain = True  # Set check_domain to True if the domain extension is valid

if check_username and check_company and check_domain:  # Check if all validity checks pass
    print("Valid email")
else:
    print("Invalid email")