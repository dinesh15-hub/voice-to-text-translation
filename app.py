import os
import platform
from flask import Flask, render_template, request
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/outputs'

# Create output directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

language_map = {
    'hindi': 'hi',
    'telugu': 'te',
    'tamil': 'ta',
    'kannada': 'kn',
    'malayalam': 'ml',
    'bengali': 'bn',
    'english': 'en'
}

def capture_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

def translate_text(text, target_lang):
    return GoogleTranslator(target=target_lang).translate(text)

def text_to_audio(text, lang_key):
    file_name = f"translated_{lang_key}.mp3"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    tts = gTTS(text=text, lang=lang_key)
    tts.save(file_path)
    return file_name

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    target_language = request.form["language"].lower()
    lang_key = language_map.get(target_language, 'en')

    recognized_text = capture_voice_input()
    if not recognized_text:
        return render_template("index.html", error="Could not recognize speech")

    translated_text = translate_text(recognized_text, target_language)
    audio_file = text_to_audio(translated_text, lang_key)

    return render_template("index.html", 
                           recognized_text=recognized_text, 
                           translated_text=translated_text,
                           audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)
