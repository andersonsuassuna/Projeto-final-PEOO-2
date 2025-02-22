from app import app
import os

# hospedar com heroku
if __name__ == 'main':
    port=int(os.getenv("PORT"), "5000")
    app.run(host="0.0.0.0, port=port")