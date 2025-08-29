from PIL import Image
import pytesseract
from gtts import gTTS
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
   
    # Open an image file
    img = Image.open('C://Users//DELL//Documents//miniproject//image2.jpg')
    
    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(img)
    
    return extracted_text

def text_to_speech(text, output_audio_path):
    
    # Use Google Text-to-Speech (gTTS)
    tts = gTTS(text)
    
    # Save the audio file
    tts.save(output_audio_path)
    print(f"Audio saved at: {output_audio_path}")

def main(image_path, output_audio_path):
   
    extracted_text = image_to_text(image_path)
    
    if extracted_text.strip():  # Check if any text is extracted
        print("Extracted Text:", extracted_text)
        
        text_to_speech(extracted_text, output_audio_path)
    else:
        print("No text detected in the image.")

if __name__ == "__main__":
  
    image_path = 'image_sample.png'  
    output_audio_path = 'output_speech.mp3'  
    
    main(image_path, output_audio_path)



