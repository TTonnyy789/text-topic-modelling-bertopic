# BERTopic Dockerized Prediction Model

This is the project that uses the BERTopic model to predict topics based on input text. This project is containerized using Docker for easy deployment and execution.

This topic model was trained in several news articles and journals mainly based on Bloom Berg News and Foreign Affairs. The expected effect is to identify the most related topics for the input article, and there are some common topics will present after you input your text, such as Technology, Market, and Economy etc.

![BERTopic Logo](https://github.com/TTonnyy789/Pictueres/blob/main/Download/3632492bb621b51af9c5fccc02da54fe0e44374f-1824x1026.png)

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

Provide any text input when prompted to get the related topics.(Make sure there are no spaces or blank lines in the input text)

## Building the Docker Image Locally (Optional)

If you want to build the Docker image locally:

The multi-platform docker image builder is required in this case.

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

```
git clone https://github.com/TTonnyy789/Topic_Modelling.git
cd Topic_Modelling
docker buildx build --platform linux/amd64,linux/arm64 -t ttonnyy789/bertopic-bb --load .
docker run -it --rm ttonnyy789/bertopic-bb
```

## License
[MIT]((https://choosealicense.com/licenses/mit/))

## Acknowledgements

- Thanks to Docker and the BERTopic community for the foundational tools and resources.
- Special thanks to ChatGPT for project troubleshooting guidance.