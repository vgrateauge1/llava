from langchain_community.llms import Ollama
from PIL import Image
import base64
from io import BytesIO
from IPython.display import HTML, display

import json, os, re

bakllava = Ollama(base_url="http://localhost:11434",model="llava")


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def plt_img_base64(img_base64):
    """
    Display base64 encoded string as image

    :param img_base64:  Base64 string
    """
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
    # Display the image by rendering the HTML
    display(HTML(image_html))

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings.
    :param pil_image: PIL image
    :return: Base64 string
    """
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def analyze_criteria_image(file_path, question):
    """
    Analyzes an image and returns the LLM's response.
    :param file_path: Path to the image file
    :return: LLM's response
    """

    pil_image = Image.open(file_path)
    image_b64 = convert_to_base64(pil_image)
    llm_with_image_context = bakllava.bind(images=[image_b64])
    return llm_with_image_context.invoke(question)

def analyze_image(file_path,prompt):
    """
    Analyzes an image and returns the LLM's response after using regex to extract json values.
    :param file_path: Path to the image file
    :return: LLM's response
    """
    # First Prompt:
    # Extract information about hair color, age, skin color, and gender from the data. The results should be formatted in JSON, including fields for 'hairColor', 'age', 'skinColor', and 'gender'. Each result must be accurate and reliable, with gender categorized as Male or Female. The age should be represented as a number. Skin color options include Dark, Ebony, Ivory, Light, Medium, or Unknown. Hair colors should be identified as Black, Blonde, Brown, Gray, Red, White, or Unknown. Don't add any comments or precision in the JSON but only the fields asked.

    # Second Prompt:
    # Analyze an image of food and identify all visible ingredients. Use this information to generate a list of possible dishes that can be made from these ingredients. Present the results in JSON format, categorizing them under two primary keys: 'ingredients' and 'possibleDishes'. Under 'ingredients', list each detected food item, and under 'possibleDishes', suggest names of dishes that could be prepared using these ingredients. Ensure that the ingredient detection is precise, and the dish suggestions are practical, reflecting common culinary practices. Don't add any comments or precision in the JSON but only the fields asked.

    # Third Prompt:
    # Conduct a detailed analysis of the clothing worn by a person in an image. Identify each article of clothing, noting its type, such as t-shirt, sweater, hoodie, or jeans. Specify the color of each item using precise descriptors like 'baby blue', 'dark green', and so on. Include any additional elements or distinctive features on the clothing, such as patterns, logos, or text. Structure the results as a list, with each entry detailing the 'type of clothing', 'color', and 'additional elements'. The description should be thorough, capturing subtle details and providing an accurate representation of the attire. Don't add any comments or precision in the JSON but only the fields asked.

    # Fourth Prompt:
    # Meticulously examine an image depicting a car accident. Count and confirm the total number of vehicles involved. Assess the severity of the accident using a scale from 'not serious' to 'very serious'. Format the analysis results in JSON, including keys for 'numberOfVehicles', with an integer value representing the count of vehicles, and 'accidentSeverity', with a string value describing the severity of the accident. Ensure the JSON output is precise and the assessment accurately reflects the visible details of the accident. The information should be presented clearly for straightforward interpretation. Don't add any comments or precision in the JSON but only the fields asked.
    
    if file_path is None:
        resultllm = askLlava(bakllava,prompt)
    else:
        resultllm = analyze_criteria_image(file_path,prompt)

    # Utilisation d'une expression régulière pour trouver tout ce qui est entre {}
    match = re.search(r'\{(.*?)\}', resultllm, re.DOTALL)
    result=resultllm

    if match:
        # Extraction et affichage du premier élément entre accolades
        result = "{"+match.group(1)+"}"
    else:
        print("Aucun contenu trouvé entre accolades.")
    print("Final Result from LLM : " + result)
    return dict(extractedPictureElements=json.loads(result)),resultllm


