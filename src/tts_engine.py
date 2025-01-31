from yapper import Yapper, PiperSpeaker, PiperVoiceUK, PiperQuality


def read_text_file(file_path):
    """Reads text from a given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


alan = PiperSpeaker(
    voice=PiperVoiceUK.ALAN
)


def text_to_speech(input_file, output_file):
    """Converts text to speech using Yapper-TTS and saves as WAV."""
    text = read_text_file(input_file)
    if not text:
        print("No text to convert.")
        return

    try:
        alan.text_to_wave(text, output_file)
        print(f"Speech saved to {output_file}")
    except Exception as e:
        print(f"Error during speech synthesis: {e}")


def main():
    input_file = "/home/hunter/PycharmProjects/PythonProject/src/input.txt"  # Replace with your text file path
    output_file = "/home/hunter/PycharmProjects/PythonProject/src/test.wav"  # Replace with desired output file path
    text_to_speech(input_file, output_file)


if __name__ == "__main__":
    main()
