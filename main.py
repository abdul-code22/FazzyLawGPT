import openai
import gradio

with open('hidden.txt') as file:
    openai.api_key = file.read()

messages = [{"role": "system", "content": 'You are a lawyer that is expert in IPR laws and cyber laws of India so that you can give advice to the client.'}]

def CustomChatGPT(Client_Query):
    messages.append({"role": "user", "content": Client_Query})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages

    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Fazzy LawGPT- An AI Consultant")

demo.launch(share=True)