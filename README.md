# EiT - Speech to Text Module

This module uses WhisperLive (https://github.com/collabora/WhisperLive) package to achieve a nearly real-time transcription module including VAD (Voice Activity Detection). Modifications are made on the WhisperLive source code to fit this project.

## Specifications
- A nearly real-time transcription module
- Two main models: 
  - faster-whisper (a reimplementation of OpenAI's Whisper model)
    - Can handle all language but less accurate in Norwegian (also other languages most likely)
  - NbAiLab Whisper Model
    - For handling Norwegian dialects

## Requirements 
- Install [docker](https://docs.docker.com/engine/install/) (Only if using Docker)
- Install [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) (Only if with GPU)
- ```pip install requirements/server.txt``` (if running server locally)
- ```pip install requirements/client.txt```

## Running server
### With Docker
To run it with the Norwegian model add a `-fw ./model/nb-whisper-small-beta-ct2` at `docker run`

NOTE: might have been some update in the docker but cannot make it to run with the GPU command as below. Current working command is:
```
docker run -it --gpus all -p 9090:9090 whisper-live:latest python run_server.py -fw  ./model/nb-whisper-small-beta-ct2
```

#### GPU (recommended):
  ```
  docker build . -t whisper-live -f docker/Dockerfile.gpu
  docker run -it --gpus all -p 9090:9090 whisper-live:latest
  ```
#### CPU:
```
docker build . -t whisper-live -f docker/Dockerfile.cpu
docker run -it -p 9090:9090 whisper-live:latest
```

### Locally
```
python run_server.py --port 9090 \
                      --backend faster_whisper
```

## Running client

```
python run_client.py
```

To change the global model that has been used, change the `model` parameter in the file when instantiating `TranscriptionClient`.

## Build the Norwegian model locally
Run these commands in the terminal.
```
mkdir /model
pip install transformers[torch]>=4.23
ct2-transformers-converter --model NbAiLab/nb-whisper-small-beta --output_dir ./model/nb-whisper-small-beta-ct2
```

Also possible to change out `NbAiLab/nb-whisper-small-beta` with other sizes. The format will then be `NbAiLab/nb-whisper-{SIZE}-beta` and the available sizes are:

- tiny
- base
- small
- medium
- large

For more information: https://huggingface.co/NbAiLab/nb-whisper-base