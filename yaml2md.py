import yaml
import re
from habanero import Crossref, cn

def parse_pressprints(header, file):
    parsed_entries = f"# {header}\n---\n"
    
    # Read the entries from the YAML file
    with open('publications/' + file, 'r', encoding='utf-8') as f:
        entries = yaml.safe_load(f)

    if entries is not None:
        No = len(entries)
        for entry in entries:
            entryString = f"**{No}\.** {entry['authors']}, _{entry['title']}_, {entry['metadata']}\n\n"
            URLs = []
            try:
                url = entry['DOI']
                URLs.append(f"DOI: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
            except Exception as e:
                if entry['DOI']:
                    URLs.append(f"DOI: [{url}]({url})")
            try:
                url = entry['arXiv']
                URLs.append(f"arXiv: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
            except Exception as e:
                if entry['arXiv']:
                    URLs.append(f"arXiv: [{url}]({url})")
            try:
                url = entry['URL']
                URLs.append(f"URL: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
            except Exception as e:
                if entry['URL']:
                    URLs.append(f"URL: [{url}]({url})")
            entryString += " \| ".join(URLs) + "\n\n"
            parsed_entries += entryString
            No -= 1
    
    return parsed_entries

def parse_others(header, file):
    parsed_entries = f"# {header}\n---\n"
    
    # Read the entries from the YAML file
    with open('publications/' + file, 'r', encoding='utf-8') as f:
        entries = yaml.safe_load(f)

    if entries is not None:
        No = len(entries)
        for entry in entries:
            if entry['URL']:
                parsed_entries += f"**{No}\.** [{entry['metadata']}]({entry['URL']})\n\n"
            else:
                parsed_entries += f"**{No}\.** {entry['metadata']}\n\n"
            No -= 1
    
    return parsed_entries

cr = Crossref()

formatted_entries = '''---
layout: single
toc: true
toc_label: 'Publications List'
sidebar:
  nav: 'sidebar'
---
'''

formatted_entries += parse_pressprints('BOOKS', 'books.yaml')

formatted_entries += parse_pressprints('PRE-PRINTS', 'preprints.yaml')

formatted_entries += parse_pressprints('IN-PRESS', 'inpress.yaml')

# Read the entries from the YAML file
with open('publications/articles.yaml', 'r', encoding='utf-8') as f:
    entries = yaml.safe_load(f)

# Count how many entries contain 'bumpyear' as a key in 'entries'
bumpyears = sum(1 for item in entries if 'bumpyear' in item) + 1

# Split 'entries' into lists at the position where a 'bumpyear' key appears
split_entries = []
temp_list = []
for item in entries:
    if 'bumpyear' in item:
        if temp_list:
            split_entries.append(temp_list)
        temp_list = [item]
    else:
        temp_list.append(item)
if temp_list:
    split_entries.append(temp_list)

# Create a dictionary with 'bumpyears' items
bumpyear_dict = {1987 + bumpyears - i: split_entries[i] for i in range(bumpyears)}

# Remove entries containing 'bumpyear' as a key from the sublists in 'bumpyear_dict'
for year, sublist in bumpyear_dict.items():
    bumpyear_dict[year] = [item for item in sublist if 'bumpyear' not in item]

formatted_entries += f"# ARTICLES\n---\n## {max(bumpyear_dict)//10*10}'s\n\n"

# Create a string to store the formatted entries
id  = len(entries) - bumpyears + 1
for key, value in bumpyear_dict.items():
    if key%10 == 9 and key != max(bumpyear_dict):
        formatted_entries += f"## {key//10*10}'s\n\n"
    
    formatted_entries += f"### {key} ({id} - {id-len(value)+1})\n\n"
    for i, entry in enumerate(value):
        if "ID_deprecated" in entry and entry["ID_deprecated"] != None:
            id = int(entry["ID_deprecated"])

        entryString = f"<div id='{id}'></div> **{id}.** {entry['authors']}, _{entry['title']}_, {entry['metadata']}\n\n"
        URLs = []
        try:
            url = entry['DOI']
            URLs.append(f"DOI: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
        except Exception as e:
            if entry['DOI']:
                URLs.append(f"DOI: [{url}]({url})")
        try:
            url = entry['arXiv']
            URLs.append(f"arXiv: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
        except Exception as e:
            if entry['arXiv']:
                URLs.append(f"arXiv: [{url}]({url})")
        try:
            url = entry['URL']
            URLs.append(f"URL: [{re.search(r'https?://([^/]+/)?(.+)', url).group(2)}]({url})")
        except Exception as e:
            if entry['URL']:
                URLs.append(f"URL: [{url}]({url})")
        
        try:
            bibentry = cn.content_negotiation(ids = entry['DOI'], format = "bibentry")
            entryString += f"<button onclick='copyToClipboard(\"bib{id}\")'><i class='fas fa-copy'></i></button>\n" + " \| ".join(URLs) + f"\n<p id='bib{id}' style='display: none;'>{bibentry}</p>\n\n"
        except Exception as e:
            entryString += " \| ".join(URLs) + "\n\n"
            print(f"An error occurred while processing the BIBENTRY DOI {entry['DOI']}: {e}")
        
        try:
            result = cr.works(ids = entry['DOI'])
            if 'abstract' in result['message']:
                abstract = result['message']['abstract'].replace('<jats:p>', '').replace('</jats:p>', '').replace('<jats:title>Abstract</jats:title>', '')
                entryString += f"\n<details style='margin-bottom: 20px;'>\n  <summary>Abstract:</summary>\n  \n  {abstract}\n</details>"
        except Exception as e:
            print(f"An error occurred while processing the ABSTRACT of DOI {entry['DOI']}: {e}")
        
        formatted_entries += entryString + "\n\n"
        id -= 1

formatted_entries += parse_others('CONFERENCE PROCEEDINGS AND REPORTS','proceedingsandreports.yaml')

formatted_entries += parse_others('PATENTS', 'patents.yaml')

formatted_entries += parse_others('BOOK CHAPTERS', 'bookchapters.yaml')

formatted_entries += parse_others('WEBCASTS', 'webcasts.yaml')

formatted_entries += "# THESES\n---\n"

# Read the entries from the YAML file
with open('publications/theses.yaml', 'r', encoding='utf-8') as f:
    entries = yaml.safe_load(f)

for type in ['PhD Thesis','MS Thesis','BS Thesis']:
    formatted_entries += f"## {type.upper()}\n\n"
    No = len([entry for entry in entries if entry['type'] == type])
    for entry in entries:
        if entry['type'] == type:
            if 'URL' in entry:
                formatted_entries += f"**{No}\.** [{entry['metadata']}]({entry['URL']})\n\n"
            else:
                formatted_entries += f"**{No}\.** {entry['metadata']}\n\n"
            No -= 1

# Write the formatted entries to a .md file
with open('index.md', 'w', encoding='utf-8') as f:
    f.write(formatted_entries)
