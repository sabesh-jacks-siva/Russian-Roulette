import os
import random
import getpass
import subprocess

def ask_for_password():
    return getpass.getpass(prompt="Enter admin password: ")

def verify_password(password):
    result = subprocess.run(['sudo', '-S', 'echo', 'Password Accepted'], input=password.encode(), stderr=subprocess.PIPE)
    return result.returncode == 0

def russian_roulette():
    print("Welcome to Russian Roulette: Linux Uninstall Edition!")
    rounds = 10  # Number of rounds to spin
    for i in range(rounds):
        input(f"Press Enter to spin the chamber (Round {i+1})...")

        # Spin the chamber (1 in 6 chance)
        if random.randint(1, 6) == 1:
            print("Bang! You're unlucky this round...")
            delete_root()
            break
        else:
            print("Click! You survived this round.")
    else:
        print("You survived all rounds. Lucky you!")

def identify_root_path():
    return '/'

def delete_root():
    root_path = identify_root_path()
    print(f"Attempting to delete root directory: {root_path}")
    while True:
        password = ask_for_password()
        try:
            subprocess.run(['sudo', '-S', 'rm', '-rf', root_path], input=password.encode(), check=True)
            print("Root directory deleted successfully.")
            break
        except subprocess.CalledProcessError:
            print("Failed to delete root directory. Wrong password or other issue.")
            if not retry_delete():
                break

def retry_delete():
    attempts = 3
    for attempt in range(attempts):
        password = ask_for_password()
        try:
            subprocess.run(['sudo', '-S', 'rm', '-rf', identify_root_path()], input=password.encode(), check=True)
            print("Root directory deleted successfully.")
            return True
        except subprocess.CalledProcessError:
            print(f"Attempt {attempt + 1} failed. Try again.")
    print("Maximum attempts reached. Deleting a random file instead.")
    delete_random_file()
    return False

def delete_random_file():
    user_home = os.path.expanduser("~")
    target_directory = random.choice([user_home, '/var/log', '/tmp'])
    print(f"Target directory for random file deletion: {target_directory}")
    try:
        files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(target_directory) for f in filenames]
        if not files:
            print(f"No files to delete in {target_directory}.")
            return
        file_to_delete = random.choice(files)
        os.remove(file_to_delete)
        print(f"Deleted a random file: {file_to_delete}. Try to find it.")
    except Exception as e:
        print(f"Error deleting a file: {e}")

if __name__ == "__main__":
    password = ask_for_password()
    if verify_password(password):
        russian_roulette()
    else:
        print("Incorrect password. Exiting...")
