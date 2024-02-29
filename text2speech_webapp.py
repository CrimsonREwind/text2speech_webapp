from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import platform

if platform.system() == 'Windows':
    os.system('cls') 
elif platform.system() == 'Linux':
    os.system('clear') 
else:
    print("Unsupported operating system")

api=str(input("Enter api-key : "))
url=str(input("Enter url : "))
text_input=str(input("Enter the text you want to turn into speech : "))
file_input=str(input('Enter file name :'))

authenticator = IAMAuthenticator(api)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url)

file_name=file_input+'.wav'
print(file_name)
with open(file_name, 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text_input,
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
    
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_name)
if os.path.exists(file_path):
    print("text to speech generated successfully")
    print(f"generated file location - {file_path}")
else:
    print("unsuccessfull")
