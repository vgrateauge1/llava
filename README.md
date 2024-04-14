# Installation
## Ollama
To try easily LLaVa model from Meta, download [Ollama](https://ollama.com). 
Then, open a terminal and write 
```bash
ollama run llava
```
You can now talk with the model locally. To add images paste the relative path for the image 
```bash
>>> describe this image C:\Users\user\Downloads\1682279377208.jpeg
Added image 'C:\Users\user\Downloads\1682279377208.jpeg'
```

## Python / Langchain application
First, you need to create a python virtual environnement that you can easily delete as you want. 
Ensure that you have python installed on your machine.
```bash
git clone https://github.com/vgrateauge1/llava.git
cd llava
pip install virtualenv
python -m virtualenv llavaEnv
.\llavaEnv\Scripts\activate
```

Now install the librairies
```bash
pip install -r requirements.txt
```

Then start the application and connect to it throw this link in your navigator http://127.0.0.1:5000.
```bash
python HTTPserver.py
```
