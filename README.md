
# Filhet-Allard Maritime - Assistant Chatbot 🚢

Bienvenue sur le projet **Assistant Virtuel Filhet-Allard Maritime** !

Ce chatbot intelligent est conçu pour accompagner les utilisateurs sur les services d'assurance maritime de Filhet-Allard Maritime. Il est basé sur **Chainlit** et utilise **GPT-4** pour générer des réponses précises et professionnelles.

---

## 🛠️ Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/ton-utilisateur/filhet-allard-chatbot.git
cd filhet-allard-chatbot
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez votre clé API OpenAI :
- Créez un fichier `.env`
- Ajoutez :
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

4. Lancez le serveur local :
```bash
chainlit run app.py -w
```

Accédez ensuite à `http://localhost:8000` dans votre navigateur.

---

## 🎨 Personnalisation

- **custom.css** : adapte l'apparence du chatbot pour correspondre à la charte graphique de Filhet-Allard Maritime.
- **public/logo.png** : ajoutez ici votre logo si besoin.

---

## 🚀 Déploiement

Recommandé : [Render.com](https://render.com)

- Connectez votre dépôt GitHub.
- Configurez un nouveau service Python avec la commande de démarrage :
```bash
chainlit run app.py --host 0.0.0.0 --port 10000
```
- Définissez votre variable d'environnement `OPENAI_API_KEY`.

---

## 📦 Structure du projet

| Dossier/Fichier   | Rôle                                          |
|-------------------|-----------------------------------------------|
| app.py            | Code principal du chatbot                    |
| custom.css        | Styles personnalisés du chatbot              |
| requirements.txt  | Dépendances Python                            |
| public/logo.png   | Logo de Filhet-Allard Maritime                |

---

## 📞 Contact

Pour toute question ou personnalisation spécifique, contactez l'équipe projet.

---
