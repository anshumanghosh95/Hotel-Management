# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:46:27 2019

@author: AN389897
"""
#import pymongo
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
#            client = pymongo.MongoClient("mongodb://sa:sa123@webdevtesting-shard-00-00-duzda.mongodb.net:27017,webdevtesting-shard-00-01-duzda.mongodb.net:27017,webdevtesting-shard-00-02-duzda.mongodb.net:27017/test?ssl=true&replicaSet=WebDevTesting-shard-0&authSource=admin&retryWrites=true")
#            db = client.Customers
#            mycol = db.Customers
#            my_list = {}
#            total_rating = {}
#            total_rating["food"] = str(request.form['food_rate'])
#            total_rating["room service"] = str(request.form['room_rate'])
#            my_list["rating"] = total_rating
#            my_list["address"] = str(request.form['address'])
#            my_list["name"] = str(request.form['name'])
#             mycol.insert_one(my_list)
#             client.close()
#            return jsonify(my_list)
            return redirect(url_for(feedback_thanks))
#            return request.form['name']
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
    

