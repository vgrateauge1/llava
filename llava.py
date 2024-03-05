from langchain_community.llms import Ollama
from PIL import Image
import base64
from io import BytesIO
from IPython.display import HTML, display


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

def askLlava(llm,question,image):
    message = llm.invoke("text":question,"image":image)
    return message


llava = createLlava()
pil_image = Image.open("/Users/val/Downloads/download.jpeg")
image_b64 = convert_to_base64(pil_image)
plt_img_base64(image_b64)
print(askLlava(llava,"whats in this image ?",image_b64))