from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=443,
        ssl_context=(
            '/etc/letsencrypt/live/deanchik.ru/fullchain.pem',
            '/etc/letsencrypt/live/deanchik.ru/privkey.pem'
        ),
        debug=True,
        use_reloader=True
    )
