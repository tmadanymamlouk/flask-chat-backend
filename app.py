from flask import Flask
from flask import json
from flask import request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello():
    return "Hello World!"

@app.route('/chat', methods = ['POST'])
@cross_origin()
def replyChat():
    message = request.json['message']
    userId = request.json['userId']
    print(message)
    print(userId)

    if message == 'start':
      data = {"message": "Hallo. Wie ist Dein Name?", "buttons": []}
    else:
      data = {"message": "Ich habe gerade keine weiteren Fragen. Möchtest Du weiter chatten?", "buttons": ['ja', 'nein', 'vielleicht']}

    response = app.response_class(
      response=json.dumps(data),
        status=200,
          mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()
