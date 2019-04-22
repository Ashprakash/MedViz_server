from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get_disease', methods=["POST"])
def get_disease():
    processed = {}
    part = request.json['part']
    type = request.json['type']
    topic = request.json['topic']
    with open('data/webmd-processed.json', 'r') as json_file:
        processed = json.loads(json_file.read(), strict=False)
        json_file.close()
    data = processed[part]

    if type is None or type == '':
        return Response(json.dumps(processed[part]), status=200)
    elif type != '' and topic == '':
        return Response(json.dumps(data[type]), status=200)
    else:
        return Response(json.dumps(data[type][topic]), status=200)



if __name__ == '__main__':
    app.run()
