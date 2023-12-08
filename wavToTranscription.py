import speech_recognition as sr
from pydub import AudioSegment

def convert_to_pcm_wav(input_file, output_file):
    # Load the input audio file using pydub
    audio = AudioSegment.from_wav(input_file)

    # Convert the audio to PCM format (16-bit, 1 channel)
    audio = audio.set_sample_width(2)
    audio = audio.set_channels(1)

    # Export the audio to the output PCM WAV file
    audio.export(output_file, format="wav")

def transcribe_pcm_wav(input_pcm_wav_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(input_pcm_wav_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)

# Example usage
input_wav_file = '/Users/jhavig/Downloads/testWav.wav'
output_pcm_wav_file = '/Users/jhavig/Downloads/testWav_output.wav'

# Convert the input WAV file to PCM format using pydub
convert_to_pcm_wav(input_wav_file, output_pcm_wav_file)

# Transcribe the PCM WAV file
transcribe_pcm_wav(output_pcm_wav_file)
