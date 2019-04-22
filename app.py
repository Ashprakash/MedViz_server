from flask import Flask, request, Response
import json
import csv


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

@app.route('/get_map', methods=["POST"])
def get_map():
    map_data ={}
    text =''
    part_name = request.json['part']
    file_name = part_name + '.csv'
    with open('mapData/map_data.json', 'r') as json_file:
        processed = json.loads(json_file.read(), strict=False)
        map_data = processed
    features = map_data['features']
    with open('mapData/'+file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for feature in features:
                if(row[0]==feature["properties"]["name"]):
                    feature["properties"]["value"]= row[5]
                    text = "In 2015 age adjusted data of lung diseases was"+row[4]+"per 100,000 people"+"/n"+ row[5]+ " cancel cases was reported"
                    feature["properties"]["text"] = text

    map_data['features'] = features


    return Response(json.dumps(map_data), status=200)


if __name__ == '__main__':
    app.run()
