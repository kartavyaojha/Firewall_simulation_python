import random 

# Log in function
def login():
    login_username = "admin"
    login_password = "admin"
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == login_username and password == login_password:
        return True
    else:
        print("Invalid username or password")
        return False

# Function to generate random ip address
def generate_random_ip():  
    return f"192.168.1.{random.randint(0,20)}"

# Function To Check The Firewall Rules
def check_firewall_rules (ip,rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # if nothing found allow the ip

# main function to generate random number, check against the firewall rules, and print result
def main():
    if login():  # Check login status before proceeding
        firewall_rules = {
            "192.168.1.4" : "block",
            "192.168.1.3" : "block",
            "192.168.1.8" : "block",
            "192.168.1.9" : "block",
        }
        # generate the random ip address
        for _ in range(12):
            ip_address = generate_random_ip() # generate random ip address
            action = check_firewall_rules(ip_address, firewall_rules) # check rules
            random_number = random.randint(0 ,9999) # generate random number
            print(f"IP:{ip_address}, Action : {action} , Random :{random_number}") # action taken
            if action == "Block":
                print("\tSecurity alert , Blocked IP found")
    else:
        print("Login failed. Exiting...")

# To execute run the main function if script is run directly
if __name__ == "__main__":
    main()
