## Install Dependencies:
Ensure you have *ffmpeg* installed on your system (required by Whisper). 
Then install the Python packages:
```Bash
pip install openai-whisper gradio
brew ffmpeg (mac/linux) / winget install -e --id Gyan.FFmpeg (windows)
```
---
## Run the Application:

```Bash
python main.py
```
---
## How to Use
-  Run the script to launch the local web server.
-  Open the URL provided in your terminal (usually http://127.0.0.1:7860).
-  Upload your audio file.
-  Click Submit.
-  Once processed, you can copy the text from the box or download the generated text file.

