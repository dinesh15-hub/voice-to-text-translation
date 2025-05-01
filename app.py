import os
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import platform
import subprocess

# Create the outputs directory if it doesn't exist
if not os.path.exists("outputs"):
    os.makedirs("outputs")

def capture_voice_input():
    """Capture voice input from the microphone."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Please speak now...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        speech_text = recognizer.recognize_google(audio)
        print(f"Recognized text: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None

def translate_text(text, target_language):
    """Translate the recognized text to the target language."""
    translated = GoogleTranslator(target=target_language).translate(text)
    print(f"Translated text: {translated}")
    return translated

def text_to_audio(text, target_language):
    """Convert translated text into an audio file and save it."""
    language_map = {
        'hindi': 'hi',
        'telugu': 'te',
        'tamil': 'ta',
        'kannada': 'kn',
        'malayalam': 'ml',
        'bengali': 'bn'
    }

    target_language_code = language_map.get(target_language, 'en')
    audio_file = f"translated_{target_language_code}.mp3"

    try:
        tts = gTTS(text=text, lang=target_language_code)
        tts.save(audio_file)
        print(f"Translated audio saved to {audio_file}")

        # Auto-play the audio
        system_platform = platform.system()
        if system_platform == "Windows":
            os.startfile(audio_file)
        elif system_platform == "Darwin":  # macOS
            subprocess.call(["open", audio_file])
        else:  # Linux
            subprocess.call(["xdg-open", audio_file])

    except ValueError as e:
        print(f"Error: {e}")


def play_audio(file_path):
    """Play the audio file based on the user's OS."""
    system = platform.system()
    if system == "Windows":
        os.system(f'start {file_path}')
    elif system == "Darwin":  # macOS
        os.system(f'open {file_path}')
    else:  # Linux
        os.system(f'xdg-open {file_path}')

def main():
    print("🎤 Voice-to-Text Translation Application 🎧\n")
    print("Supported languages: hindi, telugu, tamil, kannada, malayalam, bengali\n")

    target_language = input("Enter target language (e.g., 'hindi', 'telugu'): ").strip().lower()

    speech_text = capture_voice_input()

    if speech_text:
        translated_text = translate_text(speech_text, target_language)
        text_to_audio(translated_text, target_language)

if __name__ == "__main__":
    main()
