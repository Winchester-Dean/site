import asyncio
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
async def home():
    return render_template('index.html') 200

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=443,
        ssl_context=(
            'path/to/server.crt',
            'path/to/server.key'
        ),
        debug=True,
        use_reloader=True
    )
