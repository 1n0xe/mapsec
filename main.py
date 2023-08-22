# main.py 1
from enumeration import run_enumeration
from detection import run_detection
from exploitation import run_exploitation
from post_exploitation import run_post_exploitation

def main():
    print("Welcome to Pentest Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Enumeration")
        print("2. Detection")
        print("3. Exploitation")
        print("4. Post-Exploitation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_enumeration()
        elif choice == "2":
            run_detection()
        elif choice == "3":
            run_exploitation()
        elif choice == "4":
            run_post_exploitation()
        elif choice == "5":
            print("Exiting Pentest Tool.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
