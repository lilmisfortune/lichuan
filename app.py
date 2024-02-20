from flask import FLask,request,rendeer_template
app = Flask(_name_）
@app.route("/",method = ["GET","POST"]
def index():
  return(render_template("index.html"))
if __name__ == "__main__":
   app.run()
