from flask import Flask,render_template,request
import google.generativeai as palm
import os

api_key = os.getenv("GOOGLE_API")
palm.configure(api_key=api_key)#google api设置
model = {"model":"models/chat-bison-001"} #model选择


app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("name")
    appearence = request.form.get("appearence")
    char = request.form.get("characteristic")
    other = request.form.get("other")
    genre = request.form.get("genre")
    prompt = "generate an story for my character,the character's name is:" + str(name)
    prompt += ",and the appearence is like:" + str(appearence)
    prompt += ",the character has the characteristic like:" + str(char)
    prompt += "besides,we have some other description of the character says:" + str(other)
    prompt += "finally,the character is created for a  "
    prompt += ",if you see none after a \':\',generate the part with your imagination"
    if genre is not None:
        prompt += genre + "movie/novel"
    q = prompt
    r = palm.chat(**model,messages=q)

    return(render_template("main.html",r=r.last))

if __name__ == "__main__":
    app.run()
