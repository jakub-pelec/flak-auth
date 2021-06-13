from flask import Flask
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)

app.secret_key = "supersekrit"
blueprint = make_github_blueprint(
    client_id="my-key-here",
    client_secret="my-secret-here",
)
app.register_blueprint(blueprint, url_prefix="/login")

from app import views