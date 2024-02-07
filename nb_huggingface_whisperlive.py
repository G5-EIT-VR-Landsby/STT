import torch
# Load model directly
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

processor = AutoProcessor.from_pretrained("NbAiLab/nb-whisper-small-beta")
model = AutoModelForSpeechSeq2Seq.from_pretrained("NbAiLab/nb-whisper-small-beta")

# model.save_pretrained("saved_model/", from_pt=True)
torch.save(model.state_dict(), "saved_model/nb-whisper-small-beta.bin")