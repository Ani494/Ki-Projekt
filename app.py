from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Lade API-Key aus .env-Datei
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher KI-Assistent für Unternehmen."},
                {"role": "user", "content": user_input}
            ]
            
        )
        response_text = response.choices[0].message.content
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
