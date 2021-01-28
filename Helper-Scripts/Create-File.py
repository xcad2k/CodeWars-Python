# Small Helper Script to create a File within the Challenge Folder

import os


challengeName = input("What is the Challenge Name?: ")
challengeRank = input("What is the Challenge Difficulty?: ")
challengeUrl = input("What is the Challenge URL? :")

# Remove spaces, and insert -
fileName = "".join([char if char != " " else "-" for char in challengeName] + [".py"])

# Create File Path
filePath = f"./Challenges-{challengeRank}kyu/{fileName}"

if os.path.exists(filePath):
    print("File is already existing")
    exit(1)

try:
    with open(filePath, 'x', encoding='utf-8') as f:
        f.write(f"# Challenge-URL: {challengeUrl}\n")
        f.write(f"# Challenge-Name: {challengeName}\n")
        f.write("#\n# ---\n#\n")
except:
    print("Failed!")
