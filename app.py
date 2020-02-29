from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
import joblib

app = Flask(__name__)



@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")





@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            online_order=float(request.form['online_order'])
            book_table = float(request.form['book_table'])
            votes = float(request.form['votes'])
            location = float(request.form['location'])
            rest_type = float(request.form['rest_type'])
            cuisines = float(request.form['cuisines'])
            cost = float(request.form['cost'])
            type = float(request.form['type'])
            city = float(request.form['city'])
            filename = 'zomato_prediction_rate.sav'
            loaded_model = joblib.load(filename)
            prediction=loaded_model.predict([[online_order,book_table,votes,location,rest_type,cuisines,cost,type,city]])
            print('prediction is', prediction)
            return render_template('results.html',prediction=(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)