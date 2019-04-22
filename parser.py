import json


def topic_part():
    topics_json = []
    type_map = {}
    with open('data/type.json','r') as json_file:
        topics_json = json.loads(json_file.read(), strict=False)
        json_file.close()
    for each in topics_json:
        if 'part' not in each:
            continue
        if each['part'] not in type_map:
            type_map[each['part']] = {}
        if each['type'] not in type_map[each['part']]:
            type_map[each['part']][each['type']] = []
        type_map[each['part']][each['type']].append(each)

    for key, valueMap in type_map.items():
        count = 0
        for key2, value in valueMap.items():
            count = count + len(value)
        print(key+"-->>"+str(count))

def process_combine():

    answers = {}
    members = {}
    questions = {}
    topics = {}
    topic_question_map = {}

    with open('data/webmd-member.json','r') as json_file:
        for line in json_file:
            member_json = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        for each in member_json:
            members[each['memberId']] = each


    with open('data/webmd-question.json','r') as json_file:
        for line in json_file:
            question_json = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        for each in question_json:
            questions[each['questionId']] = each


    with open('data/webmd-answer.json','r') as json_file:
        for line in json_file:
            answer_json = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)

        for each in answer_json:
            each['question'] = questions[each['questionId']]
            if each['answerMemberId'] not in members:
                each['answered_member'] = {'memberName': 'anonymous_user' }
            else:
                each['answered_member'] = members[each['answerMemberId']]

            if each['questionId'] not in answers:
                answers[each['questionId']] = []
            answers[each['questionId']].append(each)

    with open('data/webmd-related_topic.json','r') as json_file:
        for line in json_file:
            related_topics_json = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)
        for each in related_topics_json:
            if each['questionId'] not in answers:
                each['question_answer'] = []
            else:
                each['question_answer'] = answers[each['questionId']]
            if each['topicId'] not in topic_question_map:
                topic_question_map[each['topicId']] = []
            topic_question_map[each['topicId']].append(each)

    with open('data/webmd-topics.json', 'r') as json_file:
        for line in json_file:
            topics_json = json.loads(line.replace('\\\\\"','\"').replace('\r\n', '\\r\\n').replace('\r\n', '').replace('\\\"',' ').replace('\\',''), strict=False)

        for each in topics_json:
            each['info'] = topic_question_map[each['topicId']]
            topics[each['topicId']] = each

    types_json = []
    type_map = {}
    with open('data/typev2.json', 'r') as json_file:
        types_json = json.loads(json_file.read(), strict=False)
        json_file.close()
    for each in types_json:
        if 'part' not in each:
            continue
        if each['part'] not in type_map:
            type_map[each['part']] = {}
        if each['type'] not in type_map[each['part']]:
            type_map[each['part']][each['type']] = {}
        each['value'] = topics[each['topicId']]['info']
        type_map[each['part']][each['type']][each['topicId']] = each

    for key, valueMap in type_map.items():
        count = 0
        for key2, value in valueMap.items():
            count = count + len(value)
        print(key + "-->>" + str(count))

    with open('data/webmd-processed.json', 'w') as json_file:
        json.dump(type_map, json_file)


if __name__ == '__main__':
    process_combine()