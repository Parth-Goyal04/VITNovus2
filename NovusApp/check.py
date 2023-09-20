file_path = "user_input.txt"  # Replace with the path to your .txt file
try:
    with open(file_path, "r") as file:
        # Read the entire content of the file into a string
        file_contents = file.read()
        user_input = file_contents

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

lst = ['a', 'e', 'i', 'o', 'u']
print(user_input)


user_input = user_input[len(user_input)//2]
if user_input in lst:
    print("yes")

else:
    print("no")