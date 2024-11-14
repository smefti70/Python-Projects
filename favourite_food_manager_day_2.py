# Initialize an empty list for favourite foods
favourite_foods = []

while True:
    print("\nFavourite Foods Manager")
    print("0. Exit")
    print("1. Add a Favourite Food")
    print("2. Remove a Favourite Food")
    print("3. View All Favourite Foods\n")

    choice = int(input("Enter your choice: "))

    # Exits from application
    if choice == 0:
        print("\nThanks for using Favourite Foods Manager.")
        break

    # Adds a Favourite Food
    elif choice == 1:
        food = input("Enter your favourite food name: ")
        favourite_foods.append(food)
        print(f"'{food}' added successfully.")

    # Remove a Favourite Food
    elif choice == 2:
        food = input("Enter the food name to be removed: ")
        # Deleting Food from Favourite Food
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"'{food}' removed successfully.")
        # Case Handling: If Food is not in the Favourite Food list.
        else:
            print(f"'{food}' is not in your Favourite Foods.")

    # View All Favourite Foods
    elif choice == 3:
        # Displaying Favourite Foods if it has any.
        if favourite_foods:
            print("Your Favourite Foods:")
            for index,food in enumerate(favourite_foods,start=1):
                print(f"{index}.{food}")

        # Case Handling: Empty Favourite Food List.
        else:
            print("You haven't added any favourite foods yet.")

    # Case Handling: Invalid Choice
    else:
        print("Invalid choice. Please try again with valid input.")


