Voice Assistant(Using Python)

Project Overview:

The Python Voice Assistant is a command-line based intelligent assistant that can listen to voice commands, respond using speech, tell the current time and date, and perform web searches. It uses speech recognition and text-to-speech technologies to create an interactive user experience.

This project demonstrates real-world usage of Python libraries related to voice processing, automation, and exception handling, making it an excellent beginner-to-intermediate level project.

Features:

i.Voice-based user interaction
ii.Converts speech to text using Google Speech Recognition
iii.Converts text to speech using pyttsx3
iv.Tells the current time
v.Tells today’s date
vi.Performs Google searches via voice command
vii.Graceful error handling for network, microphone, and engine issues
viii.Clean exit using voice commands like exit or stop

Technologies & Libraries Used:

1.Python 3
2.speech_recognition – for recognizing voice input
3.pyttsx3 – for text-to-speech output
4.datetime – for time and date
5.webbrowser – for opening search results
6.sys – for system-level handling 

How It Works:

a.The assistant initializes a text-to-speech engine.
b.It listens to the user using the system microphone.
c.Voice input is converted into text using Google Speech Recognition.
d.Based on recognized keywords:
e.search → performs a Google search
f.time → tells the current time
g.date → tells today’s date
h.exit / stop → terminates the program
i.The assistant responds using both voice and text output.

Author:
Disha Banik
Python Developer | Automation & AI Enthusiast