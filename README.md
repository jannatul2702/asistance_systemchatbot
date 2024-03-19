### Susmita, Jannatul Ferdous - 22103847 

### Gurawaliya, Harsh - 22109730 

# Project Title: DegreeDiscovery CHATBOT

GIT LINK : https://mygit.th-deg.de/sj27847/assistance_syschatbot

WIKI LINK : https://mygit.th-deg.de/sj27847/assistance_syschatbot/-/wikis/home

## Project Description
A helpful chatbot which is build using Python and Rasa. The aim of this chatbot is to help all the new incoming students with their programs selection and to provide them with proper answers and guidance.

## Prerequisites
To run this project on your computer, you will need the following software and libraries:
1. Python [3.8]
2. Rasa [3.1]

## Installation
In order to use this chatbot offline on your personal system, follow the below steps:
- Download or clone this repository using following command:
```
git clone https://mygit.th-deg.de/sj27847/assistance_syschatbot
```
- Go to the cloned directory and install virtualenv package (if you don't have it already)
```
cd admission_assistant
pip install virtualenv
```
- Create a new virtual environment in current directory with specified version of Python and activate it
```
virtualenv "my_env_name" --python=python3.8
.\my_env_name\Scripts\activate.bat
```
`Note: Python3.8 is the recommanded Python version for this project. Install and add it to PATH incase there are any errors.`

## Basic Usage
- Next step is to install Rasa and train the model
```
pip install Rasa
rasa train
```
- To connect port, open another terminal, activate virtual environment and run following command
```
rasa run actions
```
- Open previous terminal and enter following command to start interacting with chatbot
```
rasa shell
```
KEY USE CASES:
It will help with frequently asked questions without the need for human interraction

## Work Done
Jannatul Ferdous Susmita:

1) Persona 
2) Example dialogs 
3) Implementation yml-files 
4) Implementation actions.py

Harsh Gurawaliya:

1) Use cases
2) Dialog flow
3) Implementation yml-files 
4) Implementation actions.py

