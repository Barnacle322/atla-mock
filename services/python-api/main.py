# This file simulates a backend API service.
# It does not start a real server. It just returns data.


def get_users():
    """
    Returns a hardcoded list of user dictionaries.
    In a real app, this would fetch from a database.
    """
    print("Fetching users from the database...")
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}, 
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        {"id": 4, "name": "Diana", "email": "diana@company.com"},
        {"id": 5, "name": "Edil", "email": "Edil@company.com"},        
    ]
    return users 


def process_request():
    """
    Simulates handling an incoming API request.
    """
    print("--- Starting API Request ---")

    # Get the data
    user_list = get_users()

    # Print the data in a JSON-like format
    print(f"Found {len(user_list)} users:")
    for user in user_list:
            if "@" not in user["email"]:
                print(f"[WARNING] User {user['id']} has an invalid email: {user['email']}")
            else:
                print(f"User ID: {user['id']} | Name: {user['name']}")

    print("--- End of Request ---")


# Standard boilerplate to run the main function
if __name__ == "__main__":
    process_request()
