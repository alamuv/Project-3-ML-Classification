from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from make_prediction2 import cvd_or_not

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index2.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_cvd2/', methods=['GET', 'POST'])
def render_message():

    # user-entered details
    details = ['age', 'totChol', 'MAP', 'BMI', 'cigsPerDay', 'heartRate', 'glucose', 'male', 'prevalentHyp']

    # error messages to ensure correct units of measure
    messages = [
                "Age",
                "Total Cholesterol",
                "Systolic BP",
                "BMI",
                "Ciarettes per Day",
                "HeartRate",
                "Glucose",
                "Male=1, Female=0",
                "Prevalent Hyp: 1=Yes, 0=No"
                ]

    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(details):
        user_input = request.form[ing]
        try:
            float_ingredient = float(user_input)
        except:
            return render_template('index2.html', message=messages[i])
        amounts.append(float_ingredient)

    # show user final message
    final_message = cvd_or_not(amounts)
    return render_template('index2.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)
