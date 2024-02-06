# from transformers import BertModel, BertTokenizer, BertConfig
from transformers import AutoTokenizer, AutoModelForSpeechSeq2Seq

import torch
import librosa


# enc = BertTokenizer.from_pretrained("NbAiLab/nb-whisper-small-beta")
enc = AutoTokenizer.from_pretrained("NbAiLab/nb-whisper-small-beta")

import numpy as np

# Load audio file and convert to mel spectrogram
audio_file = "sample.wav"
audio, sr = librosa.load(audio_file, sr=16000)  # Load audio with a sampling rate of 16kHz
mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=400, hop_length=160, n_mels=80)
mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)  # Convert to dB scale

# Pad or truncate mel spectrogram to have a length of 3000 frames
target_length = 3000
if mel_spectrogram.shape[1] < target_length:
    # Padding along the time dimension
    mel_spectrogram = np.pad(mel_spectrogram, ((0, 0), (0, target_length - mel_spectrogram.shape[1])), mode='constant')
else:
    # Truncate if longer than target_length
    mel_spectrogram = mel_spectrogram[:, :target_length]

# Convert mel spectrogram to tensor
mel_tensor = torch.tensor(mel_spectrogram)

# Dummy segments tensor (not needed for Whisper model)
segments_tensor = torch.zeros_like(mel_tensor)

# # Tokenizing input text
# text = "[CLS] Who was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"
# tokenized_text = enc.tokenize(text)

# # Masking one of the input tokens
# masked_index = 8
# tokenized_text[masked_index] = '[MASK]'
# indexed_tokens = enc.convert_tokens_to_ids(tokenized_text)
# segments_ids = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# # Creating a dummy input
# tokens_tensor = torch.tensor([indexed_tokens])
# segments_tensors = torch.tensor([segments_ids])
# dummy_input = [tokens_tensor, segments_tensors]

# Load the tokenizer and model for BERT
model = AutoModelForSpeechSeq2Seq.from_pretrained("NbAiLab/nb-whisper-small-beta")

# Export the model to TorchScript
traced_model = torch.jit.trace(model, [mel_tensor, segments_tensor])
torch.jit.save(traced_model, "nb-whisper-small-beta.pt")