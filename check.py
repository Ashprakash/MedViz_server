import json
import pandas as pd

# with open('js1.json','r') as f1:
#     for line in f1:
#         json_data1= json.loads(line)
#         break
# with open('js2.json', 'r') as f2:
#     for line in f2:
#         json_data2=json.loads(line)
#         break
#
# json_data1 = pd.read_json('js1.json')
# json_data2 = pd.read_json('js2.json')


import json

with open('webmd-answer.json','r') as json_file:
    for line in json_file:
        json_data = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        answersList = {}
        print(len(json_data))
    for element in json_data:
        # print(element['topicId'])
        if element['questionId'] in answersList:
            answersList[element['questionId']].append(element)
        else:
            answersList[element['questionId']] = [element]
    # for line in answersList['1197531']:
    #     print(line)
    max = 0
    key = ""
    for key, values in answersList.items():
        max += len(values)
    print(max)
with open('webmd-question.json', 'r') as json_file:
    for line in json_file:
        json_data1 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
    flag = True
    for element in json_data1:
        if element['questionId'] in answersList:
            element['answers'] = answersList[element['questionId']]
            #for ids in answersList[element['questionId']]:
               # element['answers'].append(json_data[ids])

with open('webmd-mixed.json', 'w') as json_file:
    json.dump(json_data1, json_file)

with open('webmd-mixed.json','r') as json_file:
    for line in json_file:
        json_data2 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        topics = {}
        print(len(json_data))
    for element in json_data2:
        # print(element['topicId'])
        if element['questionId'] in topics:
            topics[element['questionId']].append(element)
        else:
            topics[element['questionId']] = [element]
    # for line in answersList['1197531']:
    #     print(line)
    max = 0
    key = ""
    for key, values in topics.items():
        max += len(values)
    print(max)
with open('webmd-related_topic.json', 'r') as json_file:
    for line in json_file:
        json_data3 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
    flag = True
    for element in json_data3:
        if element['questionId'] in topics:
            element['questionId'] = topics[element['questionId']]




with open('webmd-mixed1.json', 'w') as json_file:
    json.dump(json_data3, json_file)

with open('webmd-mixed1.json', 'r') as json_file:
    for line in json_file:
        json_data4 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        diseases = {}
        print(len(json_data))
    for element in json_data4:
        # print(element['topicId'])
        if element['topicId'] in diseases:
            diseases[element['topicId']].append(element)
        else:
            diseases[element['topicId']] = [element]
    # for line in answersList['1197531']:
    #     print(line)
    max = 0
    key = ""
    for key, values in diseases.items():
        max += len(values)
    print(max)

with open('webmd-topics.json', 'r') as json_file:
    for line in json_file:
        json_data5 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
    flag = True
    for element in json_data5:
        if element['topicId'] in diseases:
            element['topicId'] = diseases[element['topicId']]


with open('webmd-mixed2.json', 'w') as json_file:
    json.dump(json_data5, json_file)

with open('webmd-mixed2.json','r') as json_file:
    for line in json_file:
        json_data6 = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        print(json_data6[10])
        part={}
        for element in json_data6:
            if 'head' in part:
                part[element['topicId']].append({'brain'})


