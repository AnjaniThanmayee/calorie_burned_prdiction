# # from flask import Flask, request, jsonify, render_template
# # import pandas as pd
# # import joblib

# # app = Flask(__name__, template_folder='templates')
# # model = joblib.load('calories_predict.pkl')  

# # @app.route('/')
# # def home():
# #    return render_template('form.html')
    

# # @app.route('/output', methods=['GET', 'POST'])
# # def predict():
# #     if request.method == 'POST':
# #         input_data = pd.DataFrame({
# #     'male': [int(request.form.get('gender'))],
# #     'Age': [int(request.form.get('age'))],
# #     'Height': [float(request.form.get('height'))],
# #     'Weight': [float(request.form.get('weight'))],
# #     'Duration': [int(request.form.get('duration'))],
# #     'Heart_Rate': [float(request.form.get('heart_rate'))],
# #     'Body_Temp': [float(request.form.get('body_temp'))]
# # })
        
# #         print(input_data)
# #         prediction = model.predict(input_data)
# #         return (f'Calories Burned: {prediction[0]}')
# #     else:
# #         return 'Send a POST request with JSON data to this endpoint to get predictions.'

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5001)
# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import joblib

# app = Flask(__name__, template_folder='templates', static_folder='static')
# model = joblib.load('calories_predict.pkl')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/output', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         input_data = pd.DataFrame({
#             'male': [int(request.form.get('gender'))],
#             'Age': [int(request.form.get('age'))],
#             'Height': [float(request.form.get('height'))],
#             'Weight': [float(request.form.get('weight'))],
#             'Duration': [int(request.form.get('duration'))],
#             'Heart_Rate': [float(request.form.get('heart_rate'))],
#             'Body_Temp': [float(request.form.get('body_temp'))]
#         })
        
#         print(input_data)
#         prediction = model.predict(input_data)
#         return render_template('result.html', prediction=prediction[0])
#     else:
#         return 'Send a POST request with JSON data to this endpoint to get predictions.'

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__, template_folder='templates', static_folder='static')
model = joblib.load('calories_predict.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/output', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = pd.DataFrame({
            'male': [int(request.form.get('gender'))],
            'Age': [int(request.form.get('age'))],
            'Height': [float(request.form.get('height'))],
            'Weight': [float(request.form.get('weight'))],
            'Duration': [int(request.form.get('duration'))],
            'Heart_Rate': [float(request.form.get('heart_rate'))],
            'Body_Temp': [float(request.form.get('body_temp'))]
        })
        

        prediction = model.predict(input_data)
        return render_template('result.html', prediction=prediction[0],duration = input_data['Duration'].iloc[0])
    else:
        return 'Send a POST request with JSON data to this endpoint to get predictions.'



@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/why')
def why():
    return render_template('why.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
