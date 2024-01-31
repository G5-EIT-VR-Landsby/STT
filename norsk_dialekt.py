# Load model directly
from transformers import AutoModel, AutoProcessor, AutoModelForSpeechSeq2Seq, AutoTokenizer

processor = AutoProcessor.from_pretrained("NbAiLab/nb-whisper-tiny-beta")
model = AutoModel.from_pretrained("NbAiLab/nb-whisper-tiny-beta")
tokenizer = AutoTokenizer.from_pretrained("NbAiLab/nb-whisper-tiny-beta")
model.save_pretrained("./norsk_model.pt", save_weights_only=True)
tokenizer.save_pretrained("./norsk_model")