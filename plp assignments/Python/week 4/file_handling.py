# reading from input.txt file
with open("input.txt", "r") as file:
    content = file.read()
#counting number of words in the file
word_count = len(content.split())
print(f"Number of words in the file: {word_count}")
#converting content to uppercase
uppercase_content = content.upper()
#writng to output.txt file
with open("output.txt", "w") as file:
    file.write("Processed Content:\n")
    file.write(uppercase_content+'\n\n')
    file.write(f"Word Count: {word_count}\n")
print("Content written to output.txt")