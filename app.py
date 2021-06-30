from logging import debug
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks =  [
    {
        "id":1,
        "title":u"buy grocceries",
        "discription":u"Milk,fruits, pizza",
        "done": False
    },
    {
        "id":2,
        "title":u"learn python",
        "discription":u"Find a good python tutorial on web",
        "done": False
    }
]
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
        "status":"error",
        "message":"please provide the data"
    },400)

    task  = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({"data":tasks})

if(__name__=="__main__"):
    app.run(debug=True)
