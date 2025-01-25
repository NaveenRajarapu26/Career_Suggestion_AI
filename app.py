from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def home():
    return "Hello how are You?"

@app.route("/second")
def second_page():
    return "I am the second page"

if __name__=="__main__":
    app.run(debug=True)