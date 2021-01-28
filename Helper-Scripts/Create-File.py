# Small Helper Script to create a File within the Challenge Folder

import os
import re

import requests

ROOT = os.getenv('CODEWARS_HOME', ".")

replacers = {
    "&amp;": "And",
    "-": "",
    r"\([^\)]*\)": "",
    r"\s+": " "
}

challengeUrl = input("What is the Challenge URL? : ")

# Ask for challenge URL
# if data can be fetched automatically use them as defaults
r = requests.get(challengeUrl)

# Extract the name and rank from the HTML using regex
fetchedName = re.search(r"(?<=\"name\":\s\")[^\"]+(?=\")", r.text.split("shell_content")[-1]).group()
fetchedRank = re.search(r"\d(?=\skyu)", r.text.split("shell_content")[-1]).group()

# Apply replacer options
for replacer in replacers:
    fetchedName = re.sub(replacer, replacers[replacer], fetchedName)

# Ask the user for the name and difficulty with the given defaults
challengeName = input(f"What is the Challenge Name? [{fetchedName}]: ") or fetchedName
challengeRank = input(f"What is the Challenge Difficulty? [{fetchedRank}]: ") or fetchedRank

# Remove spaces, and insert -
fileName = "".join([char if char != " " else "-" for char in challengeName] + [".py"])

# Create File Path
filePath = f"{ROOT}/Challenges-{challengeRank}kyu/{fileName}"

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
