# LLM-Finetuning

The repository contains **Part 3** of an LLM Pipeline for Design Exploration.

This project covers collecting, cleaning and formatting a text dataset to be used for LLM finetuning - checkout [Part 1](https://github.com/jomi13/LLM-Knowledge-Pool-RAG) and [Part 2](https://github.com/jomi13/LLM-Conversational-Agents) first.

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
3. In Visual Studio Code, don´t forget to choose python to use `myenv`. Take a look at Part 2 for more details.

## Running

--This project contains a few scripts that can help you build a custom dataset for finetune:
- `01_scrape_text` is an example of a web scraper that collects a text corpus.
- `02_cleanup` merges and cleans the text collected previously. 
- `03_summarize` adds an intermediate step of processing our text before we use it in finetune.
- `04_format` creates a json file ready to be used for finetuning with the Alpaca dataset format.

If you want to use a corpus of text you already have, or want to extract one from a PDF (check Part 2 to find out how), you can disregard scripts `01 / 02`.

Once your finetune dataset is ready, head over to [this collab notebook](https://colab.research.google.com/drive/1gIzuNutwRh08iuRhQmNAti2wDB2X4fmJ?usp=sharing) to finetune a base model. We are using an edited version of an original notebook by the [unsloth team](https://github.com/unslothai/unsloth). Props to them!

**Use this as a starting point to understand how finetune datasets need to be formatted, and then go build your own. Unsloth gives you plenty of options when choosing a base model. Think about which would work best for your usecase**
