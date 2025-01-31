# Text-to-Speech (TTS) Engine

## Overview
This Python-based Text-to-Speech (TTS) engine utilizes **StyleTTS 2** for high-quality voice synthesis. The system reads text input from a file and converts it into speech, saving the output as a **WAV** file.

## Features
- Reads text input from a file
- Uses **StyleTTS 2** for speech synthesis
- Outputs speech in **WAV** format
- Handles file read errors gracefully
- Supports error handling for empty or excessively long inputs

## Dependencies
Ensure you have the following dependencies installed before running the script:

```bash
pip install torch styletts2
```

## Usage
### Running the Script
1. Place the text you want to convert in `input.txt`.
2. Run the script:

```bash
python tts_engine.py
```

3. The generated speech will be saved as `output.wav`.

### Functionality
The script follows these steps:
1. Reads text from `input.txt`
2. Loads the **StyleTTS 2** model
3. Converts the text into speech
4. Saves the output as `output.wav`

## Edge Cases Handled
- Empty text files
- File not found errors
- Handling excessively long input

## Future Enhancements
- Support for multiple voices
- Adjustable speech parameters
- Integration with real-time text streaming

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, please open an issue or submit a pull request.

