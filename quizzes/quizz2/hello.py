from flask import Flask
from flask import request, json, Response, jsonify

app = Flask(__name__)
users = []

# get homepage
@app.route("/")
def hello():
    return "Hello World!"

# create new users
@app.route("/users",methods=['POST'])
def new_user():
    name = request.form['name']
    uid = 0
    if len(users) == 0:
        uid = 1
        users.append({'name':name, 'id':uid})
    else:
        uid = users[len(users)-1]['id'] + 1
        users.append({'name': name, 'id': uid})
    newUser = {'id':uid, 'name':name}
    response = app.response_class(
        response = json.dumps(newUser),
        status = 201,
        mimetype = 'application/json'
    )
    return response


# get users by id
@app.route("/users/<int:uid>",methods=['GET'])
def get_user(uid):
    curUser = {}
    for user in users:
        if (user['id'] == uid):
            curUser = user
    if len(curUser) != 0:
        return Response(json.dumps(curUser), status=200, mimetype='application/json')
    return Response(status=404)

# DELETE users
@app.route("/users/<int:uid>",methods=['DELETE'])
def delete_user(uid):
    i = 0
    flag = False
    for i in range(len(users)):
        if (users[i]['id'] == uid):
            flag = True
            break
    if flag:
        users.pop(i)
        return Response(status=204)
    return Response(status=400)



