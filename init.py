from PIL import Image
import pytesseract
from gtts import gTTS
import os

# Path to the Tesseract-OCR executable (only required for Windows)
# For Windows, specify the path to tesseract.exe:
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# For Linux/Mac, if installed correctly, you can skip this step.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    #"""
    #Converts image to text using Tesseract OCR.
   # """
    # Open an image file
    img = Image.open('C://Users//DELL//Documents//miniproject//image2.jpg')
    
    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(img)
    
    return extracted_text

def text_to_speech(text, output_audio_path):
    """
    Converts text to speech and saves it as an audio file.
    """
    # Use Google Text-to-Speech (gTTS)
    tts = gTTS(text)
    
    # Save the audio file
    tts.save(output_audio_path)
    print(f"Audio saved at: {output_audio_path}")

def main(image_path, output_audio_path):
    # Step 1: Convert Image to Text
    extracted_text = image_to_text(image_path)
    
    if extracted_text.strip():  # Check if any text is extracted
        print("Extracted Text:", extracted_text)
        
        # Step 2: Convert Text to Speech
        text_to_speech(extracted_text, output_audio_path)
    else:
        print("No text detected in the image.")

if __name__ == "__main__":
    # Input image path and output audio path
    image_path = 'image_sample.png'  # Replace with your image path
    output_audio_path = 'output_speech.mp3'  # Output audio path
    
    main(image_path, output_audio_path)
