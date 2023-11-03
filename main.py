import openai
import gradio

with open('hidden.txt') as file:
    openai.api_key = file.read()

messages = [{"role": "system", "content": 'You are an Indian IPR and cyber Laws expert, you will generate answers to the queries raised by your client and help them understand what to do according to the information provided by the you client.You will also tell the client about the punishments acording to the sections of the indian IPR laws and cyber laws with the names of numbers of sections'}]


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