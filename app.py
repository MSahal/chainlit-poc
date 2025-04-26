import chainlit as cl
from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cl.on_chat_start
async def start():
    # Splash screen initial
    await cl.Message(
        author="Filhet-Allard Maritime",
        content="""
# 🌊 Bienvenue chez Filhet-Allard Maritime

Chargement de votre assistant dédié à l'assurance maritime...
"""
    ).send()

    # Message de bienvenue
    await cl.Message(
        author="Filhet-Allard Maritime",
        content="""
# 👋 Bonjour !

Je suis votre assistant virtuel dédié à l'assurance maritime.
Posez-moi vos questions sur nos services : navires, fret, ports, responsabilité civile maritime...
""",
        actions=[
            cl.Action(
                name="contact",
                label="📞 Contactez-nous",
                payload={"url": "https://www.fa-maritime.com/en/contact/"}
            )
        ]
    ).send()

    # FAQ automatique au démarrage
    faq_message = """
## Questions Fréquentes 🌟

- Quels types d'assurances proposez-vous pour les navires ?
- Couvrez-vous les risques liés au transport de marchandises ?
- Comment déclarer un sinistre maritime ?
- Quels sont les délais de traitement pour une indemnisation ?
- Proposez-vous une assistance en cas d'avarie en mer ?

N'hésitez pas à poser votre question !
"""
    await cl.Message(content=faq_message).send()

@cl.on_message
async def respond(message: cl.Message):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un expert en assurance maritime travaillant pour Filhet-Allard Maritime. Sois professionnel, clair et propose une mise en relation humaine si nécessaire."},
            {"role": "user", "content": message.content}
        ]
    )
    await cl.Message(content=response.choices[0].message.content).send()
