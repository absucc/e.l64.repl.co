from flask import Flask
import os
app = Flask("")
def clean(): os.system("cls" if os.name=="nt" else "clear")
clean()
@app.route("/")
def thing2():
  clean()
  return "<div style='text-align:center;font-family:sans-serif;'><h1>Eposting Short URL service</h1><p>Tadaaa - <a href='https://eposting.herokuapp.com'>Eposting</a> - <a href='https://github.com/absucc/e.l64.repl.co'>GitHub</a></p></div>"
@app.route("/<id>")
def thing1(id):
  clean()
  return '<meta http-equiv="refresh" content="0;url=https://eposting.herokuapp.com/?pub&n='+id+'">'
if __name__ == "__main__":
  app.run(host="0.0.0.0")
  clean()
