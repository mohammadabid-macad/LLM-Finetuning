import os
from transformers import AutoTokenizer
import json
import requests
import re
import os
import json
from keys import *
from config import *

# Readme: This script will take any txt file collected in the previous script and merge it into a single txt file.
# It will output a clean_text.txt

# Path to the .txt files
directory = 'scrape_data'

txt_files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]

txt_files = txt_files[:50] # How many projects to use

# Cleanup text
merged_text = []
for filename in txt_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        lines = file.readlines()
        non_empty_lines = [line.strip() for line in lines if line.strip()]
        file_content = '\n'.join(non_empty_lines)
        merged_text.append(file_content)

# Save to txt file
output_file = 'dataset/clean_text.txt'
with open(output_file, 'w') as file:
    for content in merged_text:
        file.write(content + '\n\n')

print(f"Saved {output_file}")