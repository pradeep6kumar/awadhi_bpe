import torch
from collections import defaultdict, Counter
import re
from typing import Dict, List, Tuple, Set
import json

class AwadhiBPE:
    def __init__(self, vocab_size: int = 5000):
        self.vocab_size = vocab_size
        self.merges: Dict[Tuple[str, str], str] = {}
        self.vocab: Set[str] = set()
        
    def get_stats(self, vocab: Dict[str, int]) -> Dict[Tuple[str, str], int]:
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[symbols[i], symbols[i+1]] += freq
        return pairs
    
    def merge_vocab(self, pair: Tuple[str, str], v_in: Dict[str, int]) -> Dict[str, int]:
        v_out = {}
        bigram = ' '.join(pair)
        replacement = ''.join(pair)
        for word in v_in:
            w_out = word.replace(bigram, replacement)
            v_out[w_out] = v_in[word]
        return v_out
    
    def fit(self, text: str) -> None:
        # Initial character-level tokenization
        words = text.split()
        word_freqs = Counter(words)
        
        # Initialize vocabulary with characters
        vocab = {}
        for word, freq in word_freqs.items():
            chars = ' '.join(list(word))
            vocab[chars] = freq
            self.vocab.update(set(word))

        num_merges = min(self.vocab_size - len(self.vocab), len(vocab))
        
        for i in range(num_merges):
            pairs = self.get_stats(vocab)
            if not pairs:
                break
                
            best = max(pairs, key=pairs.get)
            vocab = self.merge_vocab(best, vocab)
            self.merges[best] = ''.join(best)
            self.vocab.add(self.merges[best])
            
    def tokenize(self, text: str) -> List[str]:
        words = text.split()
        tokens = []
        
        for word in words:
            chars = ' '.join(list(word))
            for pair, merge in self.merges.items():
                chars = chars.replace(' '.join(pair), merge)
            tokens.extend(chars.split())
            
        return tokens

    def save(self, path: str) -> None:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({
                'merges': {' '.join(k): v for k, v in self.merges.items()},
                'vocab': list(self.vocab)
            }, f, ensure_ascii=False)
            
    def load(self, path: str) -> None:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.merges = {tuple(k.split()): v for k, v in data['merges'].items()}
            self.vocab = set(data['vocab'])

# Training and evaluation code
def main():
    # Read the text file
    with open('sunderkand_awdhi.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Create and train BPE
    bpe = AwadhiBPE(vocab_size=4500)  # Using slightly less than 5000 to be safe
    bpe.fit(text)
    
    # Save the trained model
    bpe.save('Awadhi_bpe.json')
    
    # Tokenize the text
    tokens = bpe.tokenize(text)
    
    # Calculate compression ratio
    original_size = len(text.encode('utf-8'))
    tokenized_size = len(tokens) * 2  # Assuming average 2 bytes per token
    compression_ratio = original_size / tokenized_size
    
    print(f"Original size (bytes): {original_size}")
    print(f"Tokenized size (bytes): {tokenized_size}")
    print(f"Compression ratio: {compression_ratio:.2f}")
    print(f"Vocabulary size: {len(bpe.vocab)}")

if __name__ == "__main__":
    main() 