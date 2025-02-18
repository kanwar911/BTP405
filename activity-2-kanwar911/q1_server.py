import socket
import threading
import json
import os

USERS = {"user1": "password1", "user2": "password2"}

INVENTORY = {1001: 10, 1002: 15, 1003: 20}

LOGGED_IN_USERS = {}
# users and inventory from file

def load_data():
    global INVENTORY, LOGGED_IN_USERS
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            INVENTORY = json.load(f)
    if os.path.exists("logged_in.json"):
        with open("logged_in.json", "r") as f:
            LOGGED_IN_USERS = json.load(f)

def save_data():
    with open("inventory.json", "w") as f:
        json.dump(INVENTORY, f)
    with open("logged_in.json", "w") as f:
        json.dump(LOGGED_IN_USERS, f)

def handle_client(client_socket):
    user_id = None
    while True:
        try:
            request = client_socket.recv(1024).decode("utf-8")
            if not request:
                break
            data = json.loads(request)
            action = data.get("action")
            
            if action == "login":
                user_id = data.get("user_id")
                password = data.get("password")
                if user_id in USERS and USERS[user_id] == password:
                    LOGGED_IN_USERS[user_id] = True
                    client_socket.send(json.dumps({"status": "success", "message": "Login successful"}).encode("utf-8"))
                else:
                    client_socket.send(json.dumps({"status": "error", "message": "Invalid credentials"}).encode("utf-8"))
            
            elif action == "view_inventory":
                if user_id and user_id in LOGGED_IN_USERS:
                    client_socket.send(json.dumps({"status": "success", "inventory": INVENTORY}).encode("utf-8"))
                else:
                    client_socket.send(json.dumps({"status": "error", "message": "Unauthorized"}).encode("utf-8"))
            
            elif action == "purchase":
                if user_id and user_id in LOGGED_IN_USERS:
                    upc = int(data.get("upc", 0))
                    quantity = int(data.get("quantity", 0))
                    if upc in INVENTORY and INVENTORY[upc] >= quantity:
                        INVENTORY[upc] -= quantity
                        client_socket.send(json.dumps({"status": "success", "message": f"Purchased {quantity} units"}).encode("utf-8"))
                    else:
                        client_socket.send(json.dumps({"status": "error", "message": "Insufficient stock"}).encode("utf-8"))
                else:
                    client_socket.send(json.dumps({"status": "error", "message": "Unauthorized"}).encode("utf-8"))
            
            elif action == "logout":
                if user_id and user_id in LOGGED_IN_USERS:
                    del LOGGED_IN_USERS[user_id]
                    client_socket.send(json.dumps({"status": "success", "message": "Logged out of system"}).encode("utf-8"))
                break
            
            save_data()
        except json.JSONDecodeError:
            client_socket.send(json.dumps({"status": "error", "message": "Invalid JSON format"}).encode("utf-8"))
        except Exception as e:
            client_socket.send(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
    client_socket.close()

def start_server():
    load_data()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))  
    server.listen(5)
    print("Server is listening on port 5555")
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
