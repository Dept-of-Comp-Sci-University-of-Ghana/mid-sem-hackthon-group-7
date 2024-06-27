# Ambiguity Detection in Financial Sentences

This project aims to detect potential ambiguity in financial sentences by analyzing the similarity between target words and a predefined set of financial terms. It leverages natural language processing (NLP) techniques and a pre-trained language model to compute embeddings for both the target words and financial terms, and then calculates the cosine similarity between them. High similarity scores may indicate potential ambiguity, suggesting that a target word could be interpreted in multiple ways within the financial context.

## Project Structure

- **`ipython-input-10-80fb314c4322`:** Defines a set of financial terms categorized into different lists (bear market, stocks, market).
- **`ipython-input-12-80fb314c4322`:** Performs part-of-speech (POS) tagging on the input sentence to identify potential target words (nouns and proper nouns) and extracts embeddings for the sentence using a pre-trained language model.
- **`ipython-input-13-80fb314c4322`:** Defines a function to compute cosine similarity between two vectors.
- **`ipython-input-14-80fb314c4322`:** Tokenizes and extracts embeddings for each financial term in the predefined lists.
- **`ipython-input-24-80fb314c4322`:** Iterates through target words, checks if they are present in the tokenized sentence, and calculates the cosine similarity with relevant financial terms.

## Requirements
All requirements can be found in the requirements.txt file and can be installed using the command
``` bash
    pip install -r requirements.txt
```

## Usage

1. **Prepare Input:** Provide the financial sentence to be analyzed in the `sentence` variable (in `ipython-input-10-80fb314c4322`).
2. **Load Pre-trained Model:** Ensure a pre-trained language model and tokenizer are loaded (not shown in the provided code snippets).
3. **Execute Code:** Run the code in the provided order.
4. **Analyze Similarity Scores:** Examine the calculated cosine similarity scores. High similarity between a target word and multiple financial terms from different categories may indicate potential ambiguity.

## Example
Example sentence
sentence = ["The bear market is affecting stocks in Helsinki."]

Analyze similarity scores and flag potential ambiguities
For instance, if "Helsinki" shows high similarity to both "market" and "stocks" terms, it might be ambiguous.

## Note

- The provided code snippets assume that a pre-trained language model and tokenizer are already loaded and available in the environment.
- Further logic and thresholds can be implemented to determine the level of ambiguity based on the similarity scores.
- This project provides a foundation for ambiguity detection and can be extended with additional features like context analysis and disambiguation techniques.