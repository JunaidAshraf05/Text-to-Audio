from gtts import gTTS
import os

def text_to_audio(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    # Play the audio file (works on Windows)
    os.system(f'start {audio_file}')  # For Windows
    # os.system(f'xdg-open {audio_file}')  # For Linux
    # os.system(f'open {audio_file}')  # For macOS



# if __name__ == "__main__":
#     text = "hII every one."
#     text_to_audio(text)

if __name__ == "__main__":
  
    text = input("Enter the text you want to convert to audio: ")
    text_to_audio(text)