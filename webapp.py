from flask import Flask, render_template

app = Flask(__name__, template_folder='webapp')


@app.get('/')
def root():
    return render_template('index.html')


@app.get('/<path:path>')
def push(path: str):
    return render_template(path)


if __name__ == '__main__':
    app.run()
