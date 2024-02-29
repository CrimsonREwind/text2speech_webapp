from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import streamlit as st

exp=st.sidebar.expander("Settings")
api=exp.text_input("API-Key")
url=exp.text_input("Url")

st.title("Text To Speech")


def on_button_click():
    st.sidebar.success("Generating Audio File")
    file_name=file_input+'.wav'
    print(file_name)
    with open(file_name, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text_input,
                voice=voice_sel,
                accept='audio/wav'        
            ).get_result().content)
        
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, file_name)

    if os.path.exists(file_path):
        st.sidebar.success("text to speech generated successfully")
    else:
        st.sidebar.error("unsuccessfull")
    st.audio(file_path)


authenticator = IAMAuthenticator(api)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url)

text_input=st.text_input("Text to convert into speech")
file_input=st.text_input("File Name")
voice_sel=st.selectbox("Select a Voice", ["en-AU_HeidiExpressive", "en-US_LisaExpressive", "en-US_EmmaExpressive", "en-US_AllisonExpressive", "de-DE_BirgitVoice", "en-US_MichaelVoice", "ko-KR_JinV3Voice", "en-AU_JackExpressive", "fr-FR_ReneeVoice", "de-DE_DieterVoice", "en-US_MichaelExpressive", "en-US_AllisonVoice", "en-GB_KateVoice", "de-DE_BirgitV3Voice", "de-DE_DieterV3Voice", "en-US_HenryV3Voice", "es-ES_EnriqueV3Voice", "en-US_LisaVoice", "ja-JP_EmiVoice", "en-US_MichaelV2Voice", "ko-KR_JinV2Voice", "es-ES_EnriqueVoice", "fr-CA_LouiseV3Voice", "es-LA_SofiaVoice", "es-ES_LauraVoice", "nl-NL_MerelV3Voice", "en-GB_KateV3Voice", "en-US_OliviaV3Voice", "pt-BR_IsabelaV3Voice", "en-US_KevinV3Voice", "it-IT_FrancescaVoice", "de-DE_DieterV2Voice", "ja-JP_EmiV3Voice", "en-US_AllisonV3Voice", "de-DE_ErikaV3Voice", "en-US_LisaV2Voice", "fr-FR_NicolasV3Voice", "en-US_MichaelV3Voice", "en-US_EmilyV3Voice", "en-GB_CharlotteV3Voice", "pt-BR_IsabelaVoice", "es-US_SofiaVoice", "de-DE_BirgitV2Voice", "it-IT_FrancescaV3Voice", "it-IT_FrancescaV2Voice", "en-US_AllisonV2Voice", "es-US_SofiaV3Voice", "en-US_LisaV3Voice", "fr-FR_ReneeV3Voice"])

file_name=file_input+'.wav'


if st.button("Generate"):
    on_button_click()