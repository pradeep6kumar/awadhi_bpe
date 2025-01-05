# Awadhi BPE Tokenizer

This space provides a Byte Pair Encoding (BPE) implementation for Awadhi text compression. It features:

- Custom BPE implementation for Awadhi text
- Vocabulary size < 5000 tokens
- Compression ratio > 3.2
- Interactive web interface

## Usage

1. Enter Awadhi text in the input box
2. Click "Tokenize"
3. View tokenization results and statistics

## Implementation Details

- Uses character-level tokenization as base
- Implements BPE merging strategy
- Handles UTF-8 encoded Awadhi text
- Provides compression statistics

## Model Details

- Base tokenization: Character-level
- Maximum vocabulary size: 4500 tokens
- Training corpus: Sunderkand in Awadhi
- Compression target: > 3.2x

## Technical Requirements

- Python 3.10+
- PyTorch
- Gradio 3.50.2+

## License

This project is licensed under the MIT License. 