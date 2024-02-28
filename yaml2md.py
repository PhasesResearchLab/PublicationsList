import yaml
import re
from habanero import Crossref

def parse_pressprints(header, file):
    parsed_entries = f"# {header}\n---\n"
    
    # Read the entries from the YAML file
    with open('publications/' + file, 'r', encoding='utf-8') as f:
        entries = yaml.safe_load(f)

    No = len(entries)
    for entry in entries:
        entryString = f"**{No}\.** {entry['authors']}, _{entry['title']}_, {entry['metadata']}\n\n"
        URLs = []
        if entry['DOI']:
            url = entry['DOI']
            URLs.append(f"DOI: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        if entry['arXiv']:
            url = entry['arXiv']
            URLs.append(f"arXiv: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        if entry['URL']:
            url = entry['URL']
            URLs.append(f"URL: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        entryString += " \| ".join(URLs)
        parsed_entries += entryString
        No -= 1
    
    return parsed_entries

def parse_others(header, file):
    parsed_entries = f"# {header}\n---\n"
    
    # Read the entries from the YAML file
    with open('publications/' + file, 'r', encoding='utf-8') as f:
        entries = yaml.safe_load(f)

    No = len(entries)
    for entry in entries:
        if entry['URL']:
            parsed_entries += f"**{No}\.** [{entry['metadata']}]({entry['URL']})\n\n"
        else:
            parsed_entries += f"**{No}\.** {entry['metadata']}\n\n"
        No -= 1
    
    return parsed_entries

cr = Crossref()

formatted_entries = parse_pressprints('PRE-PRINTS', 'preprints.yaml')

formatted_entries += parse_pressprints('IN-PRESS', 'inpress.yaml')

formatted_entries += "# ARTICLES\n---\n"

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

# Create a string to store the formatted entries
id  = len(entries) - bumpyears + 1
for key, value in bumpyear_dict.items():
    formatted_entries += f"## {key} ({id} - {id-len(value)+1})\n\n"
    for i, entry in enumerate(value):
        if "ID_deprecated" in entry:
            id = int(entry["ID_deprecated"])

        entryString = f"<div id='{id}'></div> **{id}.** {entry['authors']}, _{entry['title']}_, {entry['metadata']}\n\n"
        URLs = []
        if entry['DOI']:
            url = entry['DOI']
            URLs.append(f"DOI: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        if entry['arXiv']:
            url = entry['arXiv']
            URLs.append(f"arXiv: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        if entry['URL']:
            url = entry['URL']
            URLs.append(f"URL: [{re.search(r'https?://[^/]+/(.+)', url).group(1)}]({url})\n\n")
        entryString += " \| ".join(URLs)
        
        try:
            result = cr.works(ids = entry['DOI'])
            if 'abstract' in result['message']:
                abstract = result['message']['abstract'].replace('<jats:p>', '').replace('</jats:p>', '').replace('<jats:title>Abstract</jats:title>', '')
                entryString += f"\n<details style='margin-bottom: 20px;'>\n  <summary>Abstract:</summary>\n  \n  {abstract}\n</details>"
        except Exception as e:
            print(f"An error occurred while processing DOI {entry['DOI']}: {e}")
        
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
            if entry['URL']:
                formatted_entries += f"**{No}\.** [{entry['metadata']}]({entry['URL']})\n\n"
            else:
                formatted_entries += f"**{No}\.** {entry['metadata']}\n\n"
            No -= 1

formatted_entries += '''
<h1 style="text-align: right;">New Contributions</h1>
---
To contribute to the list of publications, please follow the instructions below:

1\. Go to ['PRL/PublicationsList'](https://github.com/PhasesResearchLab/PublicationsList) repository in GitHub.

2\. Update the corresponding YAML file(s) in the 'publications' directory with your contributions.

**Warning:** Entries are numbered sequentially in reverse chronological order. For articles, the ID field is currently deprecated and can be omitted; however, it can still be used to set a specific number to an article.
{: .notice--warning}

**Note:** Please be observative that years are not automatically collected from entries, so make sure to add a 'bumpyear' entry between articles of different years.
{: .notice--info}

3\. After updating the YAML file(s), commit the changes to the main branch, and you're good to go! The list will soon be automatically updated in the [PRL Publications List](https://phasesresearchlab.github.io/PublicationsList/).
'''

# Write the formatted entries to a .md file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(formatted_entries)
