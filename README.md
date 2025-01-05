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

## Example:
Here is an excerpt from "Hanuman Chalisa" Written in Awadhi (A dialect of Hindi). If you run this on Huggingface [Spaces](https://huggingface.co/spaces/pradeep6kumar2024/awadhi_bpe)

You would get below mentioned Answer:

Input: 

॥ चौपाई ॥ 
जय हनुमान ज्ञान गुण सागर। 
जय कपीस तिहुँ लोक उजागर ॥ 
राम दूत अतुलित बल धामा। 
अंजनि पुत्र पवनसुत नामा ॥ 
महाबीर बिक्रम बजरंगी | 
कुमति निवार सुमति के संगी ॥ 
कंचन बरन बिराज सुबेसा। 
कानन कुण्डल कुंचित केसा ॥ 
हाथ बज्र अरु ध्वजा बिराजै | 
काँधे मूँज जनेऊ छाजै ॥ 
शंकर स्वयं केसरी नन्दन | 
तेज प्रताप महा जग बन्दन ॥ 
बिद्यावान गुणी अति चातुर । 
राम काज करिबे को आतुर ॥ 
प्रभु चरित्र सुनिबे को रसिया | 
राम लखन सीता मन बसिया ॥ 
सूक्ष्म रूप धरि सियहिं दिखावा | 
बिकट रूप धरि लंक जरावा ॥ 
भीम रूप धरि असुर सँहारे | 


Output:

{
"Tokens": "॥ चौ पाई ॥ जय हनुमान ज्ञा न गु ण सागर। जय कपीस तिहुँ लोक उजा गर ॥ राम दूत अतुलित बल धा मा । अंजनि पु त्र पवनसुत नामा ॥ महा बी र बि क्रम बजरंग ी | कुमति निवा र सुमति के संग ी ॥ कं चन बरन बि राज सुबे सा। कानन कु ण ् ड ल कु ं चित के सा ॥ हा थ ब ज्र अरु ध ् व जा बि राजै | का ँ धे मू ँ ज जने ऊ छा जै ॥ श ं कर स्व य ं के सरी नन् द न..." ,
"Number of Tokens": 173 ,
"Original Size (bytes)": 1304 ,
"Tokenized Size (bytes)": 346 ,
"Compression Ratio": "3.77" ,
"Vocabulary Size": 2849
} 

## License

This project is licensed under the MIT License. 
