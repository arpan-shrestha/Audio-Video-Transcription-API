import whisper
model = whisper.load_model("small")
result = model.transcribe("eps82.mp3", fp16=False)

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("Transcript saved!!!")

