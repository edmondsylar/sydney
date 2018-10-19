from flask import Flask, jsonify, request

data = [
    {
        'name':'Edmond',
        'emai':'edmondsylar@gmail.com'
    }
]

class methods:

    def get(self):
        return data

    def post_data(self):
        detail = {
            'name':request.json['name'],
            'email':request.json['email']
        }
        data.append(detail)
        return "Posted"