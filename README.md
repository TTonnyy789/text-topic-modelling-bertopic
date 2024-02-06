# Topic Classification and Keyword Extraction from News Articles using BERTopic

This is the project that uses the BERTopic model to predict topics based on input text. This project is containerized using Docker for easy deployment and execution.

This topic model was trained in several news articles and journals mainly based on Bloom Berg News and Foreign Affairs. The expected effect is to identify the most related topics for the input article, and there are some common topics will present after you input your text, such as Technology, Market, and Economy etc.

<p float="left">
  <img src="https://private-user-images.githubusercontent.com/109502468/302138352-eb1e1732-e0f5-42dc-b4ff-899ecc10d412.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcwODY2MDksIm5iZiI6MTcwNzA4NjMwOSwicGF0aCI6Ii8xMDk1MDI0NjgvMzAyMTM4MzUyLWViMWUxNzMyLWUwZjUtNDJkYy1iNGZmLTg5OWVjYzEwZDQxMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwNFQyMjM4MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZmNkMmRhYmQ4ODRmNTE2NmExOGFkNWI3YjhhMjRiYTliNjVhZWNiN2ZkYzRmMGU2OTU3ZjBmZTU5ZDNhNjU3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.fcJWnnZ_NKWKIdslq3hM98a4MfWYomWHpqBthR6JcDY" width="400" />
  <img src="https://private-user-images.githubusercontent.com/109502468/302138352-eb1e1732-e0f5-42dc-b4ff-899ecc10d412.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcyMTUyODUsIm5iZiI6MTcwNzIxNDk4NSwicGF0aCI6Ii8xMDk1MDI0NjgvMzAyMTM4MzUyLWViMWUxNzMyLWUwZjUtNDJkYy1iNGZmLTg5OWVjYzEwZDQxMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwNlQxMDIzMDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04NWZmNmY2ZGNmZDlhY2IxNjQ3YjE4N2M1YWIyNzU2ZDVjZmRmZjQxNGM0YjhjNTllMTRmZTFlNDM3ZjJjNGE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.c-yF7Vr8e3cXBHeYevetlmtcnWOWtuf9NKrlPAoqdDQ" width="400" /> 
</p>

<!-- ![BERTopic Logo](https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/3632492bb621b51af9c5fccc02da54fe0e44374f-1824x1026.png)![Docker Logo](https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/docker%20logo1.png) -->

## Table of Contents

- [Features](#features)
- [Software and Tools Requirements](#software-and-tools-requirements)
- [Python Environment and Dependencies](#python-environment-and-dependencies)
- [Getting Started](#getting-started)
- [Building the Docker Image Locally](#building-the-docker-image-locally-optional)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features 

- **Model Loading**: Seamlessly load a pre-trained BERTopic model.
- **Prediction Endpoint**: Provide any text input to identify the top related topics.
- **Cross-Platform Docker Support**: Built for compatibility across both AMD64 & ARM64 architectures.

## Software And Tools Requirements

- **Docker**: Ensure Docker is installed on your machine. [Download Docker](https://www.docker.com/products/docker-desktop)
- **VSCodeIDE**: Main platform to compose your code. [Download VSCodeIDE](https://code.visualstudio.com)
- **Git** (Optional): For cloning and contributing to the repository. [Download Git](https://git-scm.com/downloads)

## Python Environment and Dependencies

The application is written in Python and requires Python 3.8.13 on Apple Silicon device. Dependencies are listed in the `requirements.txt` file in this repository, which include:

- BERTopic
- numpy
- pandas
- seaborn
- transformers
- tokenizers
- scikit-learn

For a complete list of dependencies and their versions, refer to `requirements.txt`.

## Getting Started

### Prerequisites

- Docker installed on your machine.
- Git for cloning the repository.

### Pulling the Docker Image

```bash
docker pull ttonnyy789/bertopic-bb:latest
```

### Running on Docker container
```bash
docker run -it --rm ttonnyy789/bertopic-bb
```

Once you execute the command, the follow result will present on your terminal. After the `Enter text:` appear you can provide any text input when prompted to get the related topics.

`Make sure there are no spaces or blank lines in the input text`


<img src="https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/input.jpg" alt="Image1" width="600"/>

<!-- ![Docker file run successfully](https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/input.jpg) -->

### Here is a simple result.
<img src="https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/result.jpg" alt="Image1" width="600"/>

<!-- ![Docker file run example](https://github.com/TTonnyy789/Pictueres/blob/main/Topic_Modelling/result.jpg) -->


## Building the Docker Image Locally (Optional)

If you want to build the Docker image locally:

The multi-platform docker image builder is required in this case. 
Take M1 Apple Silicon device as an example:

```bash
docker buildx create --use
docker buildx inspect --boostrap
```
You can execute the following commands to check this specific docker builder whether has been installed in your machine or not.

```bash
docker images
```

If it is successfully installed, you will be able to find a docker image on your local device called `moby/buildkit`.

Next step, execute the commands below, you would be able to build and run this docker file successfully.

```bash
git clone https://github.com/TTonnyy789/Topic_Modelling.git
cd Topic_Modelling
```
Once cloned this repositories from Github, you can run following commands and run this dockerized model locally. 

In this case, this image is built with `--platform linux/arm64,linux/amd64` setting, so it would not store image to your local device automatically if you did not add `--load`. 

Therefore, `--load` is essential in this stage, because this docker file is based on multi-platform, the initial configuration of building docker image will not store it directly on you device.

You can change `--load` to `--push` if you want to push this image onto your docker hub.

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t ttonnyy789/bertopic-bb --load .
```
Last but not least, execute this command and enjoy your topic predicting journey ! !

```bash
docker run -it --rm ttonnyy789/bertopic-bb
```

## License
[MIT]((https://choosealicense.com/licenses/mit/))

## Acknowledgements

- Thanks to Docker and the BERTopic community for the foundational tools and resources.
- Special thanks to ChatGPT for project troubleshooting guidance.
