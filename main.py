from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/contacts/")
def contact():
    return render_template('contacts.html')

@app.route("/blog/")
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run()