# Text-to-Speech Web App

## Overview
This web app uses IBM Cloud Text-to-Speech API to convert text into speech. It's built with Streamlit for a user-friendly interface.

## Features
- Input text in a user-friendly interface.
- Choose voice preferences using the IBM Cloud Text-to-Speech API.


## Prerequisites
Make sure you have the following installed:
- Python
- Streamlit
- IBM Cloud Text-to-Speech API credentials

## Installation
1. Clone the repository: `git clone https://github.com/CrimsonREwind/text2speech_webapp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your IBM Cloud Text-to-Speech API credentials.

## Screenshot
![Screenshot from 2024-03-05 07-27-06](https://github.com/CrimsonREwind/text2speech_webapp/assets/106526797/4c97a3a7-f6e4-4740-a35a-7280bac15134)

![Screenshot from 2024-03-05 07-27-30](https://github.com/CrimsonREwind/text2speech_webapp/assets/106526797/edff03e6-4479-462e-aa8c-9a4d9d208f32)

![Screenshot from 2024-03-05 07-30-01](https://github.com/CrimsonREwind/text2speech_webapp/assets/106526797/15a3d73b-a443-4043-ab0c-032665478439)


## Usage
1. Run the Streamlit app: `streamlit run app.py`
2. Visit `http://localhost:8501` in your browser to access the web app.
3. set up ibm cloud text to speech api-key and url.
4. Input text, select voice preferences, and generate speech.

## IBM Cloud Text-to-Speech API Credentials
Obtain your API key and URL from IBM Cloud.

## Sample
Input: \n
```"Hello there! This is a test for text-to-speech functionality. I hope this message finds you well. Technology is amazing, isn't it? It's fascinating how computers can convert written words into spoken ones. Let me know how this sounds on your end, and if there's anything else you'd like to try!"```

Output: \n
![Generated audio](https://raw.githubusercontent.com/CrimsonREwind/text2speech_webapp/16603ad9a7b0c12cba52391d617c8d74a55abc1f/sample/audio/generated.wav)

## Contributing
Feel free to contribute to the project! If you find bugs, have feature requests, or want to improve the code, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/bugfix-your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/bugfix-your-feature`.
5. Submit a pull request.
