import hashlib
import json
try:
    with open('users.jk', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}
products = [
    {"name": "laptop", "price": 10, "category": "Category1", "stock": 100},
    {"name": "mobile", "price": 20, "category": "Category2", "stock": 50},
    {"name": "toys", "price": 15, "category": "Category3", "stock": 75},
]
def save_users():
    with open('users.jk', 'w') as file:
        json.dump(users, file)
def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    login_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = login_password
    save_users()
    print("Registration successful!")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == login_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def display_products():
    print("Available Products:")
    for idx, product in enumerate(products):
        print("{idx+1}. {product['name']} - ${product['price']} - {product['category']} - Stock: {product['stock']}")
while True:
    print("\n Welcome to E-commerce System")
    print("1.Register")
    print("2.Login")
    print("3.Display Products")
    print("4.Placeorder")
    print("5.Exit")
    a=int(input("Enter your choice: "))
    if a==1:
        register()
    elif a==2:
        if login():
            pass
        else:
            continue
    elif a==3:
        display_products()
    elif a==4:
        place_order()
    elif a==5:
        print("Thank you.visit again")
        break
    else:print("invalid choice.please try again")
