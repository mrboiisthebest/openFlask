from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource



app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

api = Api(app)

class Data:
    def __init__(self):
        self.Data = [
            {
                "Username": "BobTheGod",
                "Email": "bobsthebest@bobmail.com",
                "CreationDay": "Feb 17 2025",
                "Followers": "3",
                "FirstName": "Better Bob",
                "LastName": "bobert",
                "Residence": "his house",
            },
            {
                "Username": "BobTheGod2",
                "Email": "bobsthebest2@bobmail.com",
                "CreationDay": "Feb 16 2025",
                "Followers": "4",
                "FirstName": "Bob",
                "LastName": "bobert",
                "Residence": "his house",
            }

        ]
    def read(self):
        return self.Data

    def create(self, entry):
        self.Data.append(entry)

data_base = Data()


# API for data base post and get
class DataAPI(Resource):
    def get(self):
        return jsonify(data_base.read())

    def post(self):
        # Add a new entry to InfoDb
        entry = request.get_json()
        if not entry:
            return {"error": "No data provided"}, 400
        data_base.create(entry)
        return {"message": "Entry added successfully", "entry": entry}, 201

api.add_resource(DataAPI, '/api/data')


@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(port=5001)