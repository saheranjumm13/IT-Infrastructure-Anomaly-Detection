
import json
import bcrypt
from getpass import getpass
from pathlib import Path

USERS_FILE = Path(__file__).parent / "users.json"


def create_user(username, role):
    password = getpass(f"Enter password for {username}: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print("Passwords do not match.")
        return

    if len(password) < 12:
        print("Use a password with at least 12 characters.")
        return

    users = {}

    if USERS_FILE.exists():
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            users = json.load(file)

    if username in users:
        print("That username already exists.")
        return

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    users[username] = {
        "password_hash": password_hash,
        "role": role
    }

    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    print(f"Created {role} account: {username}")


if __name__ == "__main__":
    create_user("project_owner", "owner")
    create_user("dashboard_viewer", "viewer")
    print("User setup finished.")
