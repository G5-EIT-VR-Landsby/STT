from whisper_live.client import TranscriptionClient
import threading    
from queue import Queue
import time
import keyboard



if __name__ == "__main__":
    
    client = TranscriptionClient(
        "localhost",
        9090,
        is_multilingual=True,
        # lang="en",
        translate=False,
        model="small"
    )

    queueToSend = Queue()

    def start_client():
        client()         

    def record():
        recordToQueue = False
        listToQueue = []

        while True:
            if keyboard.is_pressed('1'):
                recordToQueue = True
            elif keyboard.is_pressed('0'):
                recordToQueue = False

            if recordToQueue:
                listToQueue = listToQueue.append(client.client.getQueue())
            elif not recordToQueue and not hasSent:
                queueToSend.put("".join(listToQueue))
                listToQueue = []
                hasSent = True    

    thread_functions = [start_client, record]

    threads = []
    for func in thread_functions:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()




    

    



