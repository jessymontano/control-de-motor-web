from flask import Flask, render_template, request

app = Flask(__name__)

estado_de_motor = 'p'
estado = 'Motor en pausa'

@app.route('/', methods=['GET', 'POST'])
def index():
    global estado_de_motor
    global estado 

    if request.method == 'GET':
        gif = f'./static/images/rueda-{estado_de_motor}.gif'
        return render_template('index.html', gif=gif, estado=estado)
    
    if request.method == 'POST':
        estado_de_motor = request.form['action']
        gif = f'./static/images/rueda-{estado_de_motor}.gif'
        if estado_de_motor == 'i':
            estado = 'Motor girando a la izquierda'
        elif estado_de_motor == 'p':
            estado = 'Motor en pausa'
        elif estado_de_motor == 'd':
            estado = 'Motor girando a la derecha'
        return render_template('index.html', gif=gif, estado=estado)
