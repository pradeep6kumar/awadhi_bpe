import gradio as gr
from bpe_Awadhi import AwadhiBPE
import json
import os

# Initialize the BPE model
bpe = AwadhiBPE(vocab_size=4500)

# Load the model if it exists, otherwise train it
def initialize_model():
    if os.path.exists('Awadhi_bpe.json'):
        bpe.load('Awadhi_bpe.json')
    else:
        # Load the text and train the model
        with open('sunderkand_awdhi.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        bpe.fit(text)
        bpe.save('Awadhi_bpe.json')

def process_text(input_text: str) -> dict:
    """Process input text and return tokenization results"""
    # Tokenize the text
    tokens = bpe.tokenize(input_text)
    
    # Calculate compression ratio
    original_size = len(input_text.encode('utf-8'))
    tokenized_size = len(tokens) * 2  # Assuming average 2 bytes per token
    compression_ratio = original_size / tokenized_size
    
    return {
        "Tokens": " ".join(tokens[:100]) + "..." if len(tokens) > 100 else " ".join(tokens),
        "Number of Tokens": len(tokens),
        "Original Size (bytes)": original_size,
        "Tokenized Size (bytes)": tokenized_size,
        "Compression Ratio": f"{compression_ratio:.2f}",
        "Vocabulary Size": len(bpe.vocab)
    }

# Create the Gradio interface
def create_interface():
    with gr.Blocks(title="Awadhi BPE Tokenizer") as demo:
        gr.Markdown("# Awadhi BPE Tokenizer")
        gr.Markdown("This tool implements Byte Pair Encoding (BPE) for Awadhi text compression.")
        
        with gr.Row():
            with gr.Column():
                input_text = gr.Textbox(
                    label="Input Awadhi Text",
                    placeholder="Enter Awadhi text here...",
                    lines=5
                )
            
            with gr.Column():
                output = gr.JSON(label="Tokenization Results")
        
        submit_btn = gr.Button("Tokenize")
        submit_btn.click(
            fn=process_text,
            inputs=input_text,
            outputs=output
        )
        
        gr.Markdown("""
        ### About
        - This tokenizer uses BPE to compress Awadhi text
        - Vocabulary size is limited to 4500 tokens
        - Aims for a compression ratio > 3.2
        """)
    
    return demo

# Initialize model and create interface
initialize_model()
demo = create_interface()

# Launch the app
if __name__ == "__main__":
    demo.launch() 