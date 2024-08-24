# LLaVa-Next vs GPT-4 and Practical Use Cases

Welcome to my GitHub repository where I explore the innovative capabilities of LLaVa-Next compared to GPT-4. This repository provides insights into the unique advantages and applications of LLaVa-Next, Meta AI's groundbreaking multimodal model.

## Overview
LLaVa-Next integrates advanced language and vision processing in a compact and efficient form, setting a new benchmark in AI technology. Unlike GPT-4, LLaVa-Next operates locally on devices, requiring less than 5GB and minimal hardware, showcasing its suitability for a wide range of applications without compromising privacy or security.

![LLaVa model (2)](https://github.com/vgrateauge1/llava/assets/76152677/2f5a440f-71bd-4d66-9662-455e3c67ece9)


## Key Highlights

### Compact and Efficient
LLaVa-Next's design allows for high performance on devices as basic as a 2019 Intel MacBook Pro without the need for cloud computing resources, contrasting with GPT-4's dependency on substantial cloud infrastructure.

### Privacy and Security
With its local processing capability, LLaVa-Next ensures user data remains private and secure, making it ideal for use in sensitive fields such as healthcare and finance. This approach aligns with stringent data protection regulations and reduces the risk of data breaches.

### Versatile Applications
From auto accident analysis to food recognition and fashion insights, LLaVa-Next demonstrates versatile real-world applications. It processes complex visual and textual data to provide actionable insights, enhancing services in insurance, culinary arts, and retail.

### Structured Data Output
One of LLaVa-Next's core objectives is to transform complex multimodal inputs into structured, easily consumable outputs such as JSON. This capability allows developers to integrate LLaVa-Next's outputs directly into applications without additional data processing. The model's ability to format information into well-defined, organized data structures ensures that the outputs are not only accurate but also immediately usable by various software systems. This feature is crucial for deploying AI in environments where real-time data parsing and decision-making are essential, thereby enhancing both the utility and adaptability of applications across different industries.

## Get Involved
Explore the repository to understand more about LLaVa-Next's capabilities and how it compares to GPT-4. Check out detailed examples, installation guides, and more to see how LLaVa-Next can be integrated into your projects.

Read the full article for more detailed information: [Explore LLaVa-Next vs GPT-4 Full Article](https://medium.com/@valentin.grateau1309/llava-next-vs-gpt-4-and-some-wonderful-use-cases-83c3929bac0a).

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
