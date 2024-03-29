from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "Hello World!"

@app.route("/<string:name>")
def dojo(name):
    # lower_case = name
    # upper_case = lower_case.capitalize()
    return f"{name.capitalize()}!"

@app.route("/say/<string:name>")
def say(name):
    name_output = name.capitalize()
    return f"Hi {name_output}!"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(word, num):
    output = ""
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

if __name__ == "__main__":
    app.run(debug=True)