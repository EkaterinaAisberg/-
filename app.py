import flask
from flask import render_template
import pickle

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    if flask.request.method == 'POST':
        with open('net_model.pkl', 'rb') as f:
            loader_model = pickle.load(f)

        X1 = float(flask.request.form['matr'])
        X2 = float(flask.request.form['plotn'])
        X3 = float(flask.request.form['upr'])
        X4 = float(flask.request.form['otv'])
        X5 = float(flask.request.form['epox'])
        X6 = float(flask.request.form['temp'])
        X7 = float(flask.request.form['p_plot'])
        X8 = float(flask.request.form['smol'])
        X9 = float(flask.request.form['grad'])
        X10 = float(flask.request.form['shag'])
        X11 = float(flask.request.form['p_nash'])
        y_pred_LR_all = loader_model.predict([[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11]])

        return render_template('main.html', result=y_pred_LR_all)


if __name__ == '__main__':
    app.run(debug=True)
