import json

USERS_FILE = "user.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def login():
    users = load_users()
    
    
    print("\n===LOGIN===")
    username = input("Username anda: ")
    password = input("Password anda: ")
    
    for user in users:
        if user["username"]== username and user ["password"] == password:
            
            print(f"\nLogin berhasil! Selamat datang, {username} ({user['role']})\n")
            return user ["role"]
    print("\nLogin gagal! Username atau pasword salah.\n")
    return None


