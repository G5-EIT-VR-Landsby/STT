from whisper_live.client import TranscriptionClient
if __name__ == "__main__":
    client = TranscriptionClient(
        "localhost",
        9090,
        is_multilingual=True,
        lang="en",
        translate=False,
        model="small"
    )
    client("sample.wav")

