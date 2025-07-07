from pydub import AudioSegment
from pydub.utils import which

try:
    AudioSegment.converter = which("ffmpeg")

    print("Loading audio file…")
    audio = AudioSegment.from_file(r"D:\Python\Audio Splitter\SAVE JUNGAL TRAILER.mp3")
    print(f"Audio duration: {len(audio) / 1000} seconds")

    chunk_length_ms = 8 * 1000  # 8 seconds
    for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
        chunk = audio[start:start + chunk_length_ms]
        chunk.export(f"chunk_{i+1}.mp3", format="mp3")

    print("Done splitting into 8-second chunks.")

except Exception as e:
    print(f"Error: {e}")
