from flask import Flask
import os
app = Flask()
def clean():
  os.system("cls" if os.name=="nt" else "clear")
clean()
@app.route("/")
def thing2():
  clean()
  return "<div style='text-align:center'><h1>Eposting Short URL service</h1><p>Tadaaa</p><p><a href='https://eposting.herokuapp.com'>Eposting</a></p></div>"
@app.route("/<id>")
def thing1(id):
  clean()
  return '<meta http-equiv="refresh" content="0;url=https://eposting.herokuapp.com/?pub&id='+id+'">'
if __name__ == "__main__":
  app.run(debug=False, host=host, port=port)
  clean()
