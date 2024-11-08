# Video_Caption_Generator

This project is a desktop application that automates the process of generating captions for videos using speech recognition technology. It extracts audio from a video file, converts the audio to text, and displays captions on the video in real-time. Additionally, the application includes a secure login and registration system to ensure that only authorized users can access the video caption generation feature.

🚀 Project Overview

With the growing demand for accessible content, adding captions to videos has become essential for content creators, educators, and businesses. This application leverages Python's GUI capabilities along with powerful libraries for video processing and speech-to-text conversion, enabling users to quickly generate captions for their videos. The added login functionality ensures secure access for users, making it ideal for shared or professional environments.

🎯 Objectives

Automate Caption Generation: Extract audio from video files and convert it to text captions using speech recognition.
User Authentication: Implement a secure login and registration system to manage user access.
Video Playback with Captions: Overlay generated captions onto the original video in real-time.
Improve Accessibility: Provide a tool that enhances video content accessibility for viewers with hearing impairments.

📂 Project Structure

Login System:

Uses Tkinter for creating a user-friendly interface.
Stores user credentials securely using SQLite.
Provides options for user registration and login with error handling.

Video Caption Generator:

Uses MoviePy to extract audio from video files.
Converts audio to text using SpeechRecognition with the Google Web Speech API.
Displays the video with overlaid captions using OpenCV.

🔧 Technologies Used
Programming Language: Python
Tkinter: For building the graphical user interface.
MoviePy: For video and audio processing.
SpeechRecognition: For converting audio to text.
OpenCV: For displaying videos with real-time caption overlays.
SQLite3: For managing user credentials in a local database.


📋 Project Workflow
User Authentication:

Users must register or login to access the video caption generator.
Credentials are securely stored in a SQLite database.

Video Processing:

The user selects a video file from their system.
The application extracts audio using MoviePy and converts it to a .wav file.

Speech-to-Text Conversion:

The audio is processed through the SpeechRecognition library using Google's API to generate text captions.

Caption Overlay on Video:

Captions are displayed on the video using OpenCV, providing real-time text overlay as the video plays.

📈 Future Enhancements

Multi-language Support: Extend support for multiple languages in speech recognition.
Export Captions: Add functionality to save captions as a .srt subtitle file.
Improved Speech Recognition: Integrate other APIs for more accurate transcription (e.g., IBM Watson, Azure Speech-to-Text).
Customization: Allow users to customize caption styles (font size, color, position).

Result

The Video Caption Generator successfully extracts audio from video files, converts it to text using speech recognition, and displays real-time captions over the video. The integrated login system ensures secure access for registered users. Models like MoviePy, SpeechRecognition, and OpenCV are effectively utilized to automate caption generation, making video content more accessible.

Conclusion

This project enhances video accessibility by providing automated captions, making it valuable for content creators and educators. The secure login feature adds a layer of protection, ensuring only authorized users can access the tool. Future improvements could include multi-language support, exporting captions as subtitle files, and enhanced transcription accuracy.
