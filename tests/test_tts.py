import unittest
from unittest.mock import patch, mock_open
import os
import deepseek_r1
from tts_engine import text_to_speech_from_file


class TestTTSEngine(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="Hello, this is a test.")
    @patch("deepseek_r1.generate_speech", return_value=b"FAKE_AUDIO_DATA")
    @patch("pydub.AudioSegment.from_file")
    def test_valid_input(self, mock_audio, mock_tts, mock_file):
        """Test correct speech generation for a valid text file."""
        text_to_speech_from_file("test_input.txt", "test_output.wav")
        mock_tts.assert_called_once_with("Hello, this is a test.")
        mock_audio.assert_called_once()
        self.assertTrue(os.path.exists("test_output.wav"))

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_file(self, mock_file):
        """Test handling of an empty input file."""
        with self.assertRaises(ValueError) as context:
            text_to_speech_from_file("empty.txt")
        self.assertEqual(str(context.exception), "Input text file is empty.")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_missing_file(self, mock_file):
        """Test handling of a missing input file."""
        with self.assertRaises(RuntimeError) as context:
            text_to_speech_from_file("missing.txt")
        self.assertIn("Error reading input file", str(context.exception))

    @patch("deepseek_r1.generate_speech", side_effect=Exception("API Failure"))
    @patch("builtins.open", new_callable=mock_open, read_data="Hello, this is a test.")
    def test_api_failure(self, mock_file, mock_tts):
        """Test resilience against API failures."""
        with self.assertRaises(RuntimeError) as context:
            text_to_speech_from_file("test_input.txt")
        self.assertIn("Error during speech synthesis", str(context.exception))

    @patch("builtins.open", new_callable=mock_open, read_data="Hello\uFFFD")
    def test_invalid_characters(self, mock_file):
        """Test handling of unsupported characters."""
        with self.assertRaises(ValueError):
            text_to_speech_from_file("invalid_chars.txt")


if __name__ == "__main__":
    unittest.main()
