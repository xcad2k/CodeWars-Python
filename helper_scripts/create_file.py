# Small Helper Script to create a File within the Challenge Folder

import os
import re

import requests

from create_markdown import generate_md

# Load environment variables for configuration
ROOT = os.getenv('CODEWARS_HOME', ".")
PYTHON_EDITOR = os.getenv('PYTHON_EDITOR', 'code')
PREFER_CAMEL_CASE = os.getenv('CODEWARS_PREFER_CAMEL_CASE', "false").lower() == "true"

# Set replacers for filename
replacers = {
    "&amp;": "And",
    "-": "",
    "&#39;": "",
    r"\([^\)]*\)": "",
    r"\s+": " ",
    r"\\u0026": "And"
}


# converts the given text into a formatted line for the header
def createLine(text, l, spacer=" "):
    return "#   " + text + spacer * (l - len(text) - 5) + "#"


# Ask for challenge URL
challengeUrl = input("What is the Challenge URL? : ")

# if data can be fetched automatically use them as defaults
r = None
try:
    r = requests.get(f"https://www.codewars.com/kata/{re.findall(r'(?<=kata/)[a-f0-9]+', challengeUrl)[0]}/train/python")
except:
    print("Couldn't resolve url!")

# Extract the name and rank from the HTML using regex
fetchedName = "Name couldn't be found"
try:
    fetchedName = re.search(r"(?<=\"name\":\s\")[^\"]+(?=\")|(?<=\"name\":\")[^\"]+(?=\")", r.text.split("shell_content")[-1].replace("&quot;", '"')).group().strip()
except:
    pass

fetchedRank = "Rank couldn't be found"
try:
    fetchedRank = re.search(r"\d(?=\skyu)", r.text.split("shell_content")[-1]).group().strip()
except:
    pass

# fetchedCode = ""
# try:
#     loadedData = requests.post(f"https://www.codewars.com/kata/projects/{re.findall(r'(?<=kata/)[a-f0-9]+', challengeUrl)[0]}/python/session")
#     print(loadedData.text)
# except:
#     pass

# Apply replacer options
for replacer in replacers:
    fetchedName = re.sub(replacer, replacers[replacer], fetchedName)

# Ask the user for the name and difficulty with the given defaults
challengeName = input(f"What is the Challenge Name? [{fetchedName}]: ") or fetchedName
challengeRank = input(f"What is the Challenge Difficulty? [{fetchedRank}]: ") or fetchedRank

# Remove spaces, and insert -
fileName = f"{challengeName.strip().replace(' ', '_').lower()}.py" if not PREFER_CAMEL_CASE else f"{challengeName[0].lower()}{''.join(word[0].upper() + word[1:] for word in challengeName.strip().split(' '))[1:]}.py"

# Create File Path
filePath = f"{ROOT}/challenges_{challengeRank}kyu/{fileName}"

if os.path.exists(filePath):
    print("File is already existing")
    exit(1)

# Generate file content
challengeNameLine = f"NAME:     {challengeName}"
challengeUrlLine = f"URL:      {challengeUrl}"
challengeRankLine = f"RANK:     {challengeRank}kyu"
length = max(len(challengeNameLine), len(challengeUrlLine), len(challengeRankLine)) + 8
breakLine = "#" * length
challengeNameLine = createLine(challengeNameLine, length)
challengeUrlLine = createLine(challengeUrlLine, length)
challengeRankLine = createLine(challengeRankLine, length)

try:
    if not os.path.exists(os.path.dirname(filePath)):
        try:
            os.makedirs(os.path.dirname(filePath))
        except OSError as exc:  # Guard against race condition
            print("Couldn't create directory!")

    with open(filePath, 'x', encoding='utf-8') as f:
        f.write(f"""{breakLine}
{createLine("", length)}
{challengeNameLine}
{challengeRankLine}
{challengeUrlLine}
{createLine("", length)}
{breakLine}

""")

    # generate Markdown
    generate_md(filePath)

    if os.system(f"{PYTHON_EDITOR} {filePath}") != 0:
        print(f"Couldn't open {'Visual Studio Code' if PYTHON_EDITOR == 'code' else PYTHON_EDITOR}")
except:
    print("Failed!")
