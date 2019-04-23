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
    output = {
                "name" : "Top rated topic for "+part,
              }
    content = [
                    {"name":"Disease", "children": []},
                    {"name": "General", "children": []}
                ]

    for typeKey, valueMap in data.items():
        for key, value in valueMap.items():
            obj = {}
            obj['name'] = value['topicName']
            obj['size'] = len(value['value'])
            obj['topicId'] = value['topicId']
            if typeKey == 'disease':
                content[0]["children"].append(obj)
            else:
                content[1]["children"].append(obj)

    output["children"] = content
    return Response(json.dumps(output), status=200)


@app.route('/get_map', methods=["POST"])
def get_map():
    map_data ={}
    text =''
    part_name = request.json['part']
    print(part_name)
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
                    text = "In "+row[0]+" there is a population of " +row[6]+ " which has "+row[5]+" cases of fatal diseases"
                    feature["properties"]["text"] = text

    map_data['features'] = features
    return Response(json.dumps(map_data), status=200)


@app.route('/get_network', methods=["GET"])
def get_network():
    key = request.args['key']
    with open('data/network_data.json', 'r') as json_file:
        network = json.loads(json_file.read(), strict=False)
        return Response(json.dumps(network[key]), status=200)


@app.route('/get_word_cloud', methods=["GET"])
def get_word_cloud():
    key = request.args['key']
    with open('data/word_count.json', 'r') as json_file:
        word_cloud = json.loads(json_file.read(), strict=False)
        return Response(json.dumps(word_cloud[key]), status=200)


@app.route('/get_content', methods=["GET"])
def get_content():
    processed = {}
    part = request.args['part']
    type = request.args['type']
    topic = request.args['topic']
    with open('data/webmd-processed.json', 'r') as json_file:
        processed = json.loads(json_file.read(), strict=False)
        json_file.close()
    topic_data = processed[part][type][topic]
    answers_list = []
    for question in topic_data['value']:
        for answer in question['question_answer']:
            if 'answerVoteNum' not in answer:
                answer['answerVoteNum'] = 0
            answers_list.append(answer)
    answers_list.sort(key=lambda x: x['answerVoteNum'], reverse=True)
    answers_list_1 = answers_list[0:10]
    answers_list_2 = answers_list[11:20]
    return Response(json.dumps([answers_list_1, answers_list_2]), status=200)

if __name__ == '__main__':
    app.run()
