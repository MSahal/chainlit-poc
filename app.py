# app.py
import chainlit as cl
from openai import AsyncOpenAI
from pymongo import MongoClient
from datetime import datetime
import os
import uuid

# Configurations
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Connexion à MongoDB
mongo_uri = os.getenv("MONGO_URI")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["chainlit"]
messages_collection = db["messages"]

@cl.on_chat_start
async def start():
    session_id = str(uuid.uuid4())
    cl.user_session.set("session_id", session_id)

    # Splash screen initial
    await cl.Message(
        author="Filhet-Allard Maritime",
        content="""
# 🌊 Bienvenue chez Filhet-Allard Maritime

Chargement de votre assistant dédié à l'assurance maritime...
""",
    ).send()

    # Récupérer l'historique pour la session actuelle
    previous_messages = messages_collection.find({"session_id": session_id}).sort("timestamp", 1)

    for msg in previous_messages:
        await cl.Message(author="Utilisateur", content=msg["user_message"]).send()
        await cl.Message(author="Filhet-Allard Maritime", content=msg["bot_response"]).send()

    # Message de bienvenue après l'historique
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

    # FAQ automatique
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
    session_id = cl.user_session.get("session_id")

    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un expert en assurance maritime travaillant pour Filhet-Allard Maritime. Sois professionnel, clair et propose une mise en relation humaine si nécessaire."},
            {"role": "user", "content": message.content}
        ]
    )

    bot_response = response.choices[0].message.content

    await cl.Message(content=bot_response).send()

    # Sauvegarder l'échange avec session_id
    messages_collection.insert_one({
        "session_id": session_id,
        "user_message": message.content,
        "bot_response": bot_response,
        "timestamp": datetime.utcnow()
    })
