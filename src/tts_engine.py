import torch
from styletts2 import StyleTTS2


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


def text_to_speech(input_file, output_file):
    """Converts text to speech using StyleTTS 2 and saves as WAV."""
    text = read_text_file(input_file)
    if not text:
        print("No text to convert.")
        return

    try:
        # Load the model
        model = StyleTTS2.load_model()

        # Generate speech
        speech_waveform = model.text_to_speech(text)

        # Save output
        torch.save(speech_waveform, output_file)
        print(f"Speech saved to {output_file}")
    except Exception as e:
        print(f"Error during speech synthesis: {e}")


def main():
    input_file = "input.txt"  # Replace with your text file path
    output_file = "output.wav"  # Replace with desired output file path
    text_to_speech(input_file, output_file)


if __name__ == "__main__":
    main()
