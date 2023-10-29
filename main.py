from db import getThreadsInCategory, get_all_categories
from user import User, Thread, Comment
from art import tprint
from colorama import Back
import hashlib
import re

def is_valid_email(email):
    # Regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def allCategories():
    for category in get_all_categories():
        print(category)

def printAllThreads(category_name):
    threads = getThreadsInCategory(category_name)
    if threads:
        for thread in threads:
            print(f"Thread ID: {thread[0]}, Title: {thread[1]}, Content: {thread[2]}, Created At: {thread[3]}, Author: {thread[4]}")
    else:
        print("No threads found in the specified category.")

def registerUser():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password = hashlib.sha256(password.encode()).hexdigest()
        email = input("Enter your email: ")

        if is_valid_email(email):
            user = User(username, password, email)
            print(Back.GREEN + f"Created a new user with user ID {user.userId}")
            break  # Exit the loop when registration is successful
        else:
            print(Back.RED + "Invalid email address. Please try again.")

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User.login(username, password)
        if user:
            print(Back.GREEN + f"Logged in as user ID {user.userId}")
            return user
        else:
            print(Back.RED + "Invalid username or password. Please try again.")

def addThread(user):
    content = input("Enter the content of the thread: ")
    title = input("Enter the title of the thread: ")
    thread = Thread(title, content, user)
    print(Back.GREEN + f"Created a new thread with thread ID {thread.thread_id}")

def addComment(user):
    content = input("Enter the content of the comment: ")
    thread_id = input("Enter the ID of the thread: ")
    comment = Comment(thread_id, content, user)
    print(Back.GREEN + f"Created a new comment with comment ID {comment.comment_id}")

def main():
    tprint("TECH", font='block')
    tprint("FORUM", font='block')

    while True:
        print("\nMenu:")
        print("1. View Categories")
        print("2. View Threads in a Category")
        print("3. Register")
        print("4. Login")
        print("5. Add Thread")
        print("6. Add Comment")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            allCategories()
        elif choice == "2":
            category_name = input("Enter the name of the category: ")
            printAllThreads(category_name)
        elif choice == "3":
            registerUser()
        elif choice == "4":
            user = login()
        elif choice == "5":
            if user:
                addThread(user)
            else:
                print(Back.RED + "Please log in first.")
        elif choice == "6":
            if user:
                addComment(user)
            else:
                print(Back.RED + "Please log in first.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print(Back.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
