while True:
    # Get input from the user
    user_input = input("Enter the number of LEDs to switch on (1-10): ")

    try:
        # Try to cast the input to an integer
        num_leds = int(user_input)
        
        # Check if the number is within the valid range (1-10)
        if 1 <= num_leds <= 10:
            # Turn on LEDs using a for loop
            for i in range(1, num_leds + 1):
                print(f"LED {i} is ON")

            # Prompt if the user wants to start again
            restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
            if restart == 'n':
                print("Program ended.")
                break  # Exit the loop and end the program if the user types 'n'
        else:
            print("Number out of range. Please enter a number between 1 and 10.")

    except ValueError:
        # Handle invalid input (e.g., if the user enters something that's not an integer)
        print(f"'{user_input}' is not a valid integer. Please enter a number between 1 and 10.")
