import whisper
import gradio as gr
import os

model = whisper.load_model("small")


def transcript_audio(file):
    result = model.transcribe(file, fp16=False)
    
    filename = os.path.splitext(file.name)[0]
    output_file=f"{filename}_transcript.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    return result["text"], output_file

app=gr.Interface(
    fn=transcript_audio,
    inputs=gr.File(type="filepath", label='Upload mp3/wav'),
    outputs=[
        gr.Textbox(label="Transcript"),
        gr.File(label="Download Transcript")
    ],
    title="Whisper Transcript Generator",
    description="Upload audio and get transcript"
)
app.launch()