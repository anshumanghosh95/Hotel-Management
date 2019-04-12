# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:46:27 2019

@author: AN389897
"""

from set_details import set_required_details
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)

@app.route("/home", methods = ['GET'])
def home():
    return render_template("Home.html")

@app.route("/feedback", methods = ['GET','POST'])
def feedback():
    try:    
        if request.method == 'POST':
            db_inputs = set_required_details()
            
            db_inputs.name = str(request.form['name'])
            db_inputs.address = str(request.form['address'])
            food_rating = request.form['food_rate']
            room_rating = request.form['room_rate']
            db_inputs.insert_details(food_rating,room_rating)         

#            return "thank you"
            return redirect(url_for("feedback_thanks"))
        else:
            return render_template("Feedback.html")
    except Exception as e:
        return e

@app.route("/feedback?")
def feeback_get():
    return redirect(url_for('feedback'))
    
@app.route("/feedback/thanks")
def feedback_thanks():
    return render_template("Thanks.html")
@app.route("/homestay.html")
def homestay():
    return render_template("homestay.html")

if __name__ == "__main__":
    app.run(debug=True)
    

