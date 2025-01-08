from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница "Контакты"
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')


if __name__ == '__main__':
    app.run(debug=True)
