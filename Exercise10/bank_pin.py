# High-street bank mechanism for checking a PIN.
# The user is allowed 3 attempts to enter the correct PIN.
import getpass
# Correct pin number.

import getpass
correct_pin = "0000"

# Set starting number of attempts to 0
attempts = 0
allowed_attempts = 3

# Loop until the user enters the correct PIN or has exhausted all attempts (allowed_attempts).
while attempts < allowed_attempts:

    # Enter hidden PIN.
    supplied_pin = getpass.getpass("Enter your PIN: ")

    # Check if the PIN is correct.
    if supplied_pin == correct_pin:

        # Correct PIN!
        print("PIN accepted.")
        # break ends while statement even when it is still valid
        break

    else:

        # {} with .format to inform how many attempts used / remaining
        print("Attempt {} - you entered an incorrect PIN. You have {} attempts remaining."
              .format(attempts + 1, allowed_attempts - 1 - attempts))
        # Add 1 to the number of attempts.
        attempts += 1

# After 3 incorrect attempts lock account.
if attempts == allowed_attempts:
    print("Too many incorrect PIN attempts. Account locked.")
