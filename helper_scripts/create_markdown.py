"""
The task of this file is to fetch all the assignments from codewars for every solution.

They will be stored local only and are only for reference directly in your code editor.
"""
import json
import os
import re
from pathlib import Path

import requests

ROOT = os.getenv('CODEWARS_HOME', ".")


def generate_all_md():
    for path in Path(ROOT).glob('**/*.py'):
        if "venv" not in str(path):
            generate_md(path)


def generate_md(path):
    md_path = str(path).replace(".py", ".task.md")
    if os.path.exists(md_path):
        print(f"\U00002757 The file {md_path} already exists")
        return

    with open(path) as python_file:
        url_match = re.search(r"#\s*URL:\s*(htt.*/kata/[a-f0-9]+)", python_file.read())
        if url_match is None:
            print(f"\U00002757 The file {path} doesn't contain a codewars url")
            return
        url = url_match.groups()[0]

    data = requests.get(url)
    json_data = re.search(r"data: JSON\.parse\([\"'](.*)[\"']\)", data.text)
    if json_data is None:
        print(f"\U00002757 The description couldn't be found.")
        return
    raw_json_string = json_data.groups()[0].replace('\\"', '"').replace("\\\\", "\\")
    desc = json.loads(raw_json_string)['description']

    with open(md_path, 'x', encoding='utf-8') as f:
        f.write(desc)

# Comment this back in to download the markdown files for ALL currently existing challenges.
# generate_all_md()
