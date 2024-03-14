from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Логика регистрации пользователя
        return 'Пользователь зарегистрирован'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)