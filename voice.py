import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
RECORDING_SECONDS = 5


def record_audio(filename="recording.wav"):
    print("Barlo is listening...")

    audio = sd.rec(
        int(RECORDING_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print("Recording complete.")

    return filename


def transcribe_audio(filename):
    print("Barlo is transcribing...")

    model = WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(filename)

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()


if __name__ == "__main__":
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)

    print(f"You said: {transcription}")