# admin.py
from flask import Flask, render_template_string, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["chainlit"]
messages_collection = db["messages"]

admin_template = """<!doctype html>
<title>Admin - Historique Sessions</title>
<h1>Historique des Sessions 📚</h1>
<ul>
{% for session in sessions %}
    <li><strong>Session ID:</strong> {{ session }} - <a href="/session/{{ session }}">Voir</a> - <a href="/delete/{{ session }}" style="color: red;">Supprimer</a></li>
{% endfor %}
</ul>"""

session_template = """<!doctype html>
<title>Détails Session</title>
<h1>Session: {{ session_id }}</h1>
<a href="/">← Retour</a>
<ul>
{% for msg in messages %}
    <li><b>Utilisateur:</b> {{ msg['user_message'] }}<br><b>Bot:</b> {{ msg['bot_response'] }}</li>
{% endfor %}
</ul>"""

@app.route("/admin")
def home():
    sessions = messages_collection.distinct("session_id")
    return render_template_string(admin_template, sessions=sessions)

@app.route("/session/<session_id>")
def view_session(session_id):
    messages = list(messages_collection.find({"session_id": session_id}).sort("timestamp", 1))
    return render_template_string(session_template, session_id=session_id, messages=messages)

@app.route("/delete/<session_id>")
def delete_session(session_id):
    messages_collection.delete_many({"session_id": session_id})
    return redirect("/admin")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
