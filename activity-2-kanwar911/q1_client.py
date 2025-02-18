import socket
import json

def send_request(action: str, data: dict = {}):
    data["action"] = action
    client_socket.send(json.dumps(data).encode("utf-8"))
    response = json.loads(client_socket.recv(1024).decode("utf-8"))
    return response

def login():
    user_id = input("Provide userID: ")
    password = input("Password: ")
    response = send_request("login", {"user_id": user_id, "password": password})
    print(response["message"])
    return response["status"] == "success"

def view_inventory():
    response = send_request("view_inventory")
    if response["status"] == "success":
        print("Current Inventory:")
        for upc, quantity in response["inventory"].items():
            print(f"UPC: {upc}, Quantity: {quantity}")
    else:
        print(response["message"])

def purchase_item():
    upc = input("Enter UPC code for item: ")
    quantity = input("Enter quantity: ")
    response = send_request("purchase", {"upc": upc, "quantity": quantity})
    print(response["message"])

def logout():
    response = send_request("logout")
    print(response["message"])

def main():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))
    
    if login():
        while True:
            print("\nOptions:")
            print("1. View current Inventory")
            print("2. Purchase some Item")
            print("3. Logout of system")
            choice = input("Enter selection: ")
            
            if choice == "1":
                view_inventory()
            elif choice == "2":
                purchase_item()
            elif choice == "3":
                logout()
                break
            else:
                print("Invalid selection")
    client_socket.close()

if __name__ == "__main__":
    main()

