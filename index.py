from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    # return "Bienvenido o bienvenida a mi sitio web con python!"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"
"""


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/temperatura')
def temp():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(debug=True, port=1345)
