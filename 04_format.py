from transformers import AutoTokenizer
import json
import requests
import re
import os
import json
from keys import *
from config import *
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Readme: This script will create the inputs to our clean_text and format them into a proper dataset for finetuning.
# Outputs a structured_dataset.json

text_path = "dataset/summary_text.txt"

instruction = "Further develop the concept for the building by developing a detailed description of the project."

task = "You are an API that converts bodies of text into a single instruction object." \
        "Each JSON should include only an 'instruction' field." \
        "Create an instruction asking for the design of a building, framing your instruction in such a way that it relates to the idea behind the concept of the design." \
        "You should only fill in the instruction field with one sentence and it should begin in this format: 'Imagine a building that...' " \
        "Never directly refer to the name of the buiding or specific details of context of the design in your instruction." \
        "Only respond in the JSON format and no additional text.\n"

tokenizer = AutoTokenizer.from_pretrained("TheBloke/guanaco-13B-GPTQ")

def generate_completion(task, paragraph):
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": 
            "system", 
            "content": 
                task},
        {"role": 
            "user", 
            "content": paragraph}
        ],
        temperature=1.0,
        response_format={ "type": "json_object" },
        )
    result = response.choices[0].message.content
    return result

def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

def get_completion(task, paragraph):
        try:
            # print(f"TASK: \n{task}")
            # print(f"PARAGRAPH: \n{paragraph}")
            response = generate_completion(task, paragraph)
            if is_json(response):
                print(response)
                return json.loads(response)
            else:
                print(f"Request failed. Skipping this chunk.")
        except requests.exceptions.RequestException as e:
            return None

# Read the txt file
with open(text_path, 'r') as file:
    summaries = file.read()

paragraphs = summaries.split('\n\n')
responses = []
for paragraph in paragraphs:
    response = get_completion(task, paragraph)
    print(len(responses))
    if response is not None:
        paired_response = {
            "instruction": instruction,
            "input": response['instruction'],
            "output": paragraph
        }
        responses.append(paired_response)

# Write responses to a JSON file
with open('dataset/structured_dataset.json', 'w') as f:
    json.dump(responses, f, indent=2, ensure_ascii=False)

print(f"Saved the structured dataset containing {len(responses)} training examples.")