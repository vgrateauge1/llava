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

def createLlava():
    llm = Ollama(model="llava")
    return llm


def askLlava(question,image):
    message = bakllava.invoke(question)
    return message

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

    # Extracting the file path from the tuple

    # Using os.path.basename to extract the file name
#        image_name = os.path.basename(file_path)
#        print("DEBUG "+image_name)
    pil_image = Image.open(file_path)
    image_b64 = convert_to_base64(pil_image)
    llm_with_image_context = bakllava.bind(images=[image_b64])
    return llm_with_image_context.invoke(question)

def analyze_image(file_path):
    """
    Analyzes an image and returns the LLM's response.
    :param file_path: Path to the image file
    :return: LLM's response
    """
    prompt ="""Extract the following information: hair color, age, skin color and gender. """
    prompt+="""Format the results in JSON text, ensuring to include the fields \"hairColor\", \"age\", \"skinColor\" and \"gender\". """
    prompt+="""The expected result characteristics are: """
    prompt+="""The results must be accurate and reliable."""
    prompt+="""Gender values should Male or Female. """
    prompt+="""age should be a number. """
    prompt+="""skinColor should be one of this values Dark, Ebony, Ivory, Light, Medium or Unknown """
    prompt+="""hairColor should be one of this values  Black, Blonde, Brown, Gray, Red, White or Unknown. """

    resultllm = analyze_criteria_image(file_path,prompt)

    # Utilisation d'une expression régulière pour trouver tout ce qui est entre {}
    match = re.search(r'\{(.*?)\}', resultllm, re.DOTALL)
    result=resultllm

    if match:
        # Extraction et affichage du premier élément entre accolades
        result = "{"+match.group(1)+"}"
    else:
        print("Aucun contenu trouvé entre accolades.")
    print("Final Result from LLM : "+result)
#        age= self.analyze_criteria_image(file_path,"what is the age  ? Reply only the age")
#        skin = self.analyze_criteria_image(file_path,"what is the color of skin  ? Reply only Clear or Medium or Dark ")
#        gender = self.analyze_criteria_image(file_path,"Is it a woman or a man  ? Reply only by Woman or Man")
#        return dict(hair_color=hair_color,age=age,skin=skin,gender=gender)        
#        age=32
#        skin="Clear"
#        gender="Female"
    return dict(extractedPictureElements=json.loads(result)),resultllm

def fake_analyse(self, file_path):
    """
    Analyzes an image and returns the LLM's response.
    :param file_path: Path to the image file
    :return: LLM's response
    """
#        hair_color = self.analyze_criteria_image(file_path,"what is the hair color ? Reply only the color")

#        age= self.analyze_criteria_image(file_path,"what is the age  ? Reply only the age")

#        skin = self.analyze_criteria_image(file_path,"what is the color of skin  ? Reply only Clear or Medium or Dark ")

#        gender = self.analyze_criteria_image(file_path,"Is it a woman or a man  ? Reply only by Woman or Man")
    hair_color="Red"
    age=5
    skin="Light"
    gender="Female"
    return dict(extractedPictureElements=dict(hairColor=hair_color,age=age,skinColor=skin,gender=gender))
