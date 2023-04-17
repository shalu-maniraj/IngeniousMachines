import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "SmartAIchatBot"}]

def CustomChatGPT(Ask_me_a_Question):
    messages.append({"role": "user", "content": Ask_me_a_Question})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "SmartAIchatBot")

demo.launch(share=True)