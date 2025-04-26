
import chainlit as cl
import openai
import os

# Configure ton API Key OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@cl.on_chat_start
def start():
    cl.Message(
        author="Filhet-Allard Maritime",
        content=""""
# 👋 Bienvenue chez Filhet-Allard Maritime

Je suis votre assistant virtuel dédié à l'assurance maritime.
Posez-moi vos questions sur nos services : navires, fret, ports, responsabilité civile maritime...
""",
        actions=[
            cl.Action(name="contact", label="📞 Contactez-nous", payload="https://www.fa-maritime.com/en/contact/")
        ]
    ).send()

@cl.on_message
def respond(message: cl.Message):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un expert en assurance maritime travaillant pour Filhet-Allard Maritime. Sois professionnel, clair et propose une mise en relation humaine si nécessaire."},
            {"role": "user", "content": message.content}
        ]
    )
    response = completion.choices[0].message.content
    cl.Message(content=response).send()
