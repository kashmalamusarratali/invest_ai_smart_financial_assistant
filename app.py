import gradio as gr
from config import MODEL_CHAT
from data.database import init_db
from llm.agent import chat_with_agent
from tts.voice import speak

init_db()

def chat(message, history):
    messages = [{"role": "system", "content": "You are InvestAI"}]

    for h in history:
        messages.append(h)

    messages.append({"role": "user", "content": message})

    reply = chat_with_agent(messages, MODEL_CHAT)
    audio = speak(reply)

    history.append({"role": "assistant", "content": reply})
    return history, audio

with gr.Blocks() as ui:
    chatbot = gr.Chatbot(type="messages")
    audio = gr.Audio(autoplay=True)
    msg = gr.Textbox(label="Ask about stocks")

    msg.submit(chat, [msg, chatbot], [chatbot, audio])

ui.launch()
