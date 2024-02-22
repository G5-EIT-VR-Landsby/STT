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
python run_server.py
```

## Running client

```
python run_client.py
```