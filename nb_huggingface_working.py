import torch
from transformers import AutoTokenizer, AutoModelForSpeechSeq2Seq

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("NbAiLab/nb-whisper-small-beta")
model = AutoModelForSpeechSeq2Seq.from_pretrained("NbAiLab/nb-whisper-small-beta")

# Save the model
torch.save(model.state_dict(), "nb-whisper-small-beta.pt")
