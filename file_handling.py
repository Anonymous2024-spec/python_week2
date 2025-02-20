# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_and_modify_file():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    # Modify the content (for example, converting it to uppercase)
    modified_content = content.upper()

    # Prepare a new filename for the modified content
    new_filename = f"modified_{filename}"

    try:
        # Write the modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        print(f"Modified content has been written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to file '{new_filename}'.")

# Execute the function
if __name__ == "__main__":
    read_and_modify_file()
