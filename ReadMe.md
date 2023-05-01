# gpt4allj

This repository contains three Python scripts: `gptOnAWS.py`, `app.py`, and `simpleApp.py`.

## Scripts

### `gptOnAWS.py`

This script is a simple program that can be run on an Ubuntu server. It uses the `gpt4all-j` package to generate text from a pre-trained model.

The model was obtained from here: https://gpt4all.io/models/ggml-gpt4all-j.bin

### `app.py`

This is an unfinished app that is meant to host an API. It can be used as a starting point for building a custom API that leverages `gpt4all-j`.

### `simpleApp.py (deprecated)`

This script is a simple program that can be run on a MacBook Pro with Apple Silicon. It was previously dependent on files in the libraries but they are no longer needed because `gpt4all-j` has been updated to include them.

## Installation

To install the necessary dependencies on Ubuntu, run the following commands:

sudo apt update  
sudo apt install -y python3-pip  
sudo apt install python3.10-venv  
python3 -m venv env  
source env/bin/activate  
pip3 install gpt4all-j  
python3 gptOnAWS.py  

OR

to run app.py on a server:  

pip install gunicorn  

gunicorn app:app








