with open("source_filename.txt", "r") as file:
    content = file.read()

with open("output1.txt", "w") as outfile:
    outfile.write(content[::-1])