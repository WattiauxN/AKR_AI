# mp3_provider.py

import librosa
import numpy as np

class MP3Provider:
    def __init__(self, file_path):
        """Initializes the MP3Provider with the path to the MP3 file."""
        self.file_path = file_path
        self.audio_data = None
        self.sample_rate = None

    def load(self):
        """Loads the MP3 file into audio data and sample rate."""
        try:
            self.audio_data, self.sample_rate = librosa.load(self.file_path, sr=None)
            print(f"Loaded {self.file_path} successfully.")
        except Exception as e:
            print(f"Error loading MP3 file: {e}")

    def get_mfcc(self, n_mfcc=13):
        """Extracts MFCC features from the audio data."""
        if self.audio_data is None:
            print("No audio loaded. Please load an MP3 file first.")
            return None
        
        mfccs = librosa.feature.mfcc(y=self.audio_data, sr=self.sample_rate, n_mfcc=n_mfcc)
        return mfccs

    def get_duration(self):
        """Returns the duration of the audio in seconds."""
        if self.audio_data is not None:
            return librosa.get_duration(y=self.audio_data, sr=self.sample_rate)
        return 0
