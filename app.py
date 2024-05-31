from flask import Flask, jsonify, request

from products import products

class User:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.username = ""
        self.email = ""
        self.password = ""

    def getDiccionary(self):
        element = {"name":self.name, "surname":self.surname, "username":self.username, "email":self.email, "password":self.password}
        return element
    
    def setValues(self, data):
        self.name = data['name']
        self.surname = data['surname']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']


app = Flask(__name__)

users = []

@app.route('/create', methods=['GET','POST'])
def createMethod():
    obj = User()
    content = request.get_json()
    obj.setValues(content)
    print(content)
    users.append(obj.getDiccionary())
    return jsonify({"users":users})

@app.route('/view')
def viewMethod():
    args = request.args
    var = request.args["email"]
    dictionary = {"users":users}
    for user in users:
        for key,value in user.items():
            if key == "email":
                if value == var:
                    return user


@app.route('/modify', methods=['GET','POST','PUT'])
def modifyMethod():
    content = request.get_json()
    args = request.args
    email = request.args['email']
    dictionary = {"users":users}
    for user in users:
        for key,value in user.items():
            if key == 'email':
                if value == email:
                    users.remove(user)
                    user = {key: content.get(key, val) for key, val in user.items()}
                    users.append(user)
                    print("El usuario si ha sido modificado")
                    print(str(user))
                    
    return "Usuario modificado"


@app.route('/delete',methods=['GET','POST','DELETE'])
def deleteUser():
    content = request.get_json()
    users.remove(content)
    print("El usuario se ha eliminado.")
    return "El usuario se ha eliminado."

if __name__ == "__main__":
    app.run(debug=True)

    