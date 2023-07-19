from temperature import get_temperature

from wind import get_wind

from pressure import get_pressure




def main():
    while True:
        print("\nChoose an option:")
        print("1. Get Weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_temperature()
        elif choice == '2':
            get_wind()
        elif choice == '3':
            get_pressure()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__== "__main__":
    main()
