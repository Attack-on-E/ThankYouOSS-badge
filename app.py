from flask import Flask

from src.fire_store import fetch_thank_count
from src.shields import download_image

app = Flask(__name__)


@app.route('/thank/<user_name>/<repo_name>.svg')
def index(user_name: str = "", repo_name: str = ""):
    count = fetch_thank_count(user_name, repo_name)
    image = download_image(count)
    return image


if __name__ == '__main__':
    app.run(debug=True)
