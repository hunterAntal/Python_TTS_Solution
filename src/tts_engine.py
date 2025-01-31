import deepseek_r1  # Assuming Deepseek R1 has a Python package
from pydub import AudioSegment
import os


def text_to_speech_from_file(input_file: str, output_file: str = "output.wav"):
    """
    Reads text from a file, converts it to speech using Deepseek R1, and saves it as a WAV file.

    :param input_file: The path to the text file containing the text to be converted.
    :param output_file: The name of the output WAV file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read().strip()
    except Exception as e:
        raise RuntimeError(f"Error reading input file: {str(e)}")

    if not text:
        raise ValueError("Input text file is empty.")

    if len(text) > 5000:  # Arbitrary limit to prevent excessive length
        raise ValueError("Input text is too long. Please provide a shorter text.")

    try:
        # Generate speech using Deepseek R1 (placeholder API call)
        speech_data = deepseek_r1.generate_speech(text)

        # Save to temporary file
        temp_file = "temp_output.raw"
        with open(temp_file, "wb") as f:
            f.write(speech_data)

        # Convert to WAV using PyDub
        audio = AudioSegment.from_file(temp_file, format="raw")
        audio.export(output_file, format="wav")

        # Cleanup temporary file
        os.remove(temp_file)

        print(f"Speech synthesis complete. Output saved as {output_file}")
    except Exception as e:
        raise RuntimeError(f"Error during speech synthesis: {str(e)}")


# Example usage
if __name__ == "__main__":
    input_text_file = "input.txt"
    text_to_speech_from_file(input_text_file)
