import wave, uuid
from google import genai
from google.genai import types
from config import MODEL_TTS

client = genai.Client()

def speak(text):
    response = client.models.generate_content(
        model=MODEL_TTS,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore"
                    )
                )
            )
        )
    )

    audio = response.candidates[0].content.parts[0].inline_data.data
    file = f"tts_{uuid.uuid4().hex}.wav"

    with wave.open(file, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio)

    return file
