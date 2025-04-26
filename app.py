
import chainlit as cl
import openai
import os

# Configure ton API Key OpenAI
openai.api_key = "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"

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
            cl.Action(name="contact", value="https://www.fa-maritime.com/en/contact/", label="📞 Contactez-nous")
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

cl.run(css_path="custom.css")
