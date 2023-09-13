from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        values = []

        for i in range(1, 30):
            value = float(request.form.get(f'v{i}', 0))
            values.append(value)

        model = joblib.load('credit_card_model.joblib')
        y_pred = model.predict([values])

        if y_pred == 0:
            result = 'Normal Transaction'
        else:
            result = 'Fraud Transaction'

        return jsonify({'result': result})  # Return result as JSON response

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
