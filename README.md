# Ambiguity Detection in Financial Sentences

This project aims to detect potential ambiguity in financial sentences by analyzing the similarity between target words and a predefined set of financial terms. It leverages natural language processing (NLP) techniques and a pre-trained language model to compute embeddings for both the target words and financial terms, and then calculates the cosine similarity between them. High similarity scores may indicate potential ambiguity, suggesting that a target word could be interpreted in multiple ways within the financial context.

## Project Structure

- **`ipython-input-10-80fb314c4322`:** Defines a set of financial terms categorized into different lists (bear market, stocks, market).
- **`ipython-input-12-80fb314c4322`:** Performs part-of-speech (POS) tagging on the input sentence to identify potential target words (nouns and proper nouns) and extracts embeddings for the sentence using a pre-trained language model.
- **`ipython-input-13-80fb314c4322`:** Defines a function to compute cosine similarity between two vectors.
- **`ipython-input-14-80fb314c4322`:** Tokenizes and extracts embeddings for each financial term in the predefined lists.
- **`ipython-input-24-80fb314c4322`:** Iterates through target words, checks if they are present in the tokenized sentence, and calculates the cosine similarity with relevant financial terms.

## Requirements

- Python 3.x
- Libraries: numpy, torch, transformers (install using `!pip install numpy torch transformers`)

## Usage

1. **Prepare Input:** Provide the financial sentence to be analyzed in the `sentence` variable (in `ipython-input-10-80fb314c4322`).
2. **Load Pre-trained Model:** Ensure a pre-trained language model and tokenizer are loaded (not shown in the provided code snippets).
3. **Execute Code:** Run the code in the provided order.
4. **Analyze Similarity Scores:** Examine the calculated cosine similarity scores. High similarity between a target word and multiple financial terms from different categories may indicate potential ambiguity.

## Example