# LLM-Finetuning

The repository contains **Part 3** of an LLM Pipeline for Design Exploration.

This project covers different techniques to collect, clean and format a text dataset to be used for LLM finetuning - checkout [Part 1](https://github.com/jomi13/LLM-Knowledge-Pool-RAG) and [Part 2](https://github.com/jomi13/LLM-Conversational-Agents) first.

## Setup
1. Clone this repo into the same parent folder as the previous repos.
```bash
git clone https://github.com/jomi13/LLM-Finetuning
```
2. Your folder structure should now look like this:
```bash
>parent folder<
    -LLM-Knowlege-Pool-RAG
    -LLM-Conversational-Agents
    -LLM-Finetuning
    -myenv
```
3. In Visual Studio Code, don´t forget to choose python to use `myenv`

## Running

--This project contains a few resources to be explored by order:
- `01_concept_generator` generates 5 short concepts that respond to the context retrieved by the RAG agent on the knowledge pool.
- `02_concept_tasks` takes one concept you want to investigate further with pre-defined tasks.
- `03_concept_q&a` is similar, but uses questions instead of tasks.
- `04_concept_chaining` is a prompt-chaining script where you can chain your instructions.
- `05_concept_discussion` makes a conversation between an intern (creates concepts) and a jury (asks questions about them).
- `06_image_caption` creates detailed descriptions from images to create caption datasets.
- `07_image_discussion` opens a conversation where images are generated and reviewed to check if they belong to the building on the first image.

**Experiment with these scripts to see how they interact with the LLM. Each one serves as an example. Adapt them to your logic, map out successful chains, and explore different ideas in system prompts. Have fun.**
