import os
from transformers import AutoTokenizer
import os
from keys import *
from config import *
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Readme: This script will take a clean_text.txt and create summaries of each paragraph.
# It will output a summary_text.txt


# Input
clean_text = "/dataset/clean_text.txt"

# Define the LLM task
task = "You are an API that converts bodies of text into a single summary paragraph." \
        "Create a short summary paragraph of the building depicted in the following text." \
        "Reference the architecture features, form, shape, materiality, program, relation to the site, etc"\
        "Mention in the summary aspects related to the idea behind the concept of the design." \
        "You should only respond with a summary paragraph and no additional text."

# Get summaries from LLM
def generate_summary(task, chunk):
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": 
            "system", 
            "content": task},
        {"role": 
            "user", 
            "content": chunk}
        ],
        temperature=1.0,)
    
    result = response.choices[0].message.content
    return result
        
# Run
with open(clean_text, 'w') as file:
    content = file.read()

# Split into paragraphs
paragraphs = content.split('\n\n')

# Send to be summarized
summaries = []
for chunk in paragraphs:
    summary = generate_summary(task, chunk)
    print(len(summaries) + "/" + len(paragraphs))
    if summary is not None:
        summaries.append(summary)
        print(summary)

# Export to txt file
output_file = 'dataset/summary_text.txt'
with open(output_file, 'w') as file:
    for content in summaries:
        file.write(content + '\n\n')

print(f"Finished summarization, saved {output_file}.")