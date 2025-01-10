with open("movie_posters.txt", "r") as file:
    lines = file.readlines()

# Process each line to replace only the first ': ' with '|'
updated_lines = [line.replace(": ", "|", 1) for line in lines]

# Write the updated lines back to the file
with open("movie_posters.txt", "w") as file:
    file.writelines(updated_lines)

print("Updated text file successfully!")