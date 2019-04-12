# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:37:40 2019

@author: AN389897
"""
import pymongo

class set_required_details:
    name = ""
    address = ""
    total_rating = {}
    my_list = {}
    
    def insert_details(self, food_rating, room_service_rating):
        client = pymongo.MongoClient("mongodb://sa:sa123@webdevtesting-shard-00-00-duzda.mongodb.net:27017,webdevtesting-shard-00-01-duzda.mongodb.net:27017,webdevtesting-shard-00-02-duzda.mongodb.net:27017/test?ssl=true&replicaSet=WebDevTesting-shard-0&authSource=admin&retryWrites=true")
        db = client.Customers
        mycol = db.Customers
        self.total_rating["food"] = int(food_rating)
        self.total_rating["room service"] = int(room_service_rating)
        self.my_list["rating"] = self.total_rating
        self.my_list["address"] = self.address
        self.my_list["name"] = self.name
        mycol.insert_one(self.my_list)
        
        client.close()


