from whisper_live.client import TranscriptionClient
import threading    
from queue import Queue
import time
# import keyboard



if __name__ == "__main__":
    
    client = TranscriptionClient(
        "localhost",
        9090,
        is_multilingual=True,
        lang="en",
        translate=False,
        model="small"
    )

    queueToSend = Queue()

    def start_client():
        client()         

    def get_prompt():
        while True:
            prompt = client.client.get_prompt()
            if prompt:
                print(prompt)

    thread_functions = [start_client, get_prompt]

    threads = []
    for func in thread_functions:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()




    

    



