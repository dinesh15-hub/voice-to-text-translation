# Voice-to-Text Translation Application

This is a Python-based application that captures voice input, recognizes the spoken text, detects its language, translates it into a target language, and generates an audio file in the translated language.

## Features

- Captures voice input using the microphone.
- Recognizes spoken text using Google Speech Recognition.
- Detects the language of the recognized text.
- Translates the recognized text into a user-specified target language.
- Converts the translated text into an audio file using Google Text-to-Speech (gTTS).
- Saves the translated audio files in the `outputs/` folder.
- Automatically plays the translated audio once it's saved (if supported by your system).

## Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/dinesh15-hub/voice-to-text-translation.git
    ```

2. **Install the required libraries:**

    Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # On macOS/Linux, use: source venv/bin/activate
    ```

    Then install the dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Make sure your microphone is working and accessible.**

4. **Create an `outputs/` directory**, where the translated audio files will be saved.

## Usage

1. **Run the script**:

    ```bash
    python app.py
    ```

2. **Enter the target language** when prompted (e.g., Hindi, Telugu, Tamil, etc.).
3. **Speak into the microphone** when instructed.
4. The application will:
   - Recognize your speech.
   - Detect the language of the recognized text.
   - Translate the text into the specified target language.
   - Save the translated audio to an `outputs/` folder.
5. The translated audio will automatically play if your system supports it.

## Supported Languages

The application currently supports translation to the following languages:

- Hindi (`hi`)
- Telugu (`te`)
- Kannada (`kn`)
- Tamil (`ta`)
- Malayalam (`ml`)
- Bengali (`bn`)

## File Structure

