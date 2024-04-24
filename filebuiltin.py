# Open file in write mode
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, World!\nThis is a test file.\n")

# Close the file
file.close()

# Open file in read mode
file = open("example.txt", "r")

# Read content from the file
content = file.read()
print("File Content:")
print(content)

# Close the file
file.close()

# Open file in read mode
file = open("example.txt", "r")

# Read the first line
line1 = file.readline()
print("\nFirst Line:")
print(line1)

# Read all lines and print them
print("\nRemaining Lines:")
remaining_lines = file.readlines()
for line in remaining_lines:
    print(line.strip())

# Close the file
file.close()

# Open file in append mode
file = open("example.txt", "a")

# Append more content
file.write("\nAppending new content.")

# Close the file
file.close()