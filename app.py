users = {
    "admin_user": "admin",
    "regular_user": "user"
}


def login(username):
    # Simulates authentication by checking if the username exists
    if username in users:
        role = users[username]
        print(f"\nLogin successful!")
        print(f"Username: {username}")
        print(f"Role: {role}")
        return role
    else:
        print("\nLogin failed. User does not exist.")
        return None


def admin_action(role):
    # Only administrators can use this function
    if role == "admin":
        print("Access granted: You opened the ADMIN area.")
    else:
        print("Access denied: Admin role required.")


def user_action(role):
    # Only regular users can use this function
    if role == "user":
        print("Access granted: You opened the USER area.")
    else:
        print("Access denied: User role required.")

# note: change this value to test different users
current_username = "admin_user"

current_role = login(current_username)

if current_role:
    print("\nTesting Admin Action:")
    admin_action(current_role)

    print("\nTesting User Action:")
    user_action(current_role)
