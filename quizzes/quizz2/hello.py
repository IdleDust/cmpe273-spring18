from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users",methods=['POST'])
def new_user():
    name = request.form['name']
    uid = request.form['id']
    return 'hello {}!'.format(name) #response should be Json data, 
    #change the default status code 200 to 201 by the framework


''''
1 GET / -> hello world
2 POST /users
    'name=foo' 
    data store {} in memory
    return 201 & JSON data

get "/users/1"
    response: {'id':1, "name": "x"}

3. GET users/1 ->200
4. DELETE users/1 =>204
