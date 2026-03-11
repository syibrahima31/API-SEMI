from flask import Flask, render_template 
from data import eleves

app = Flask(__name__)


# creation du route principale qui est le point entre de app 
@app.route("/")
def index(): 
    return render_template("index.html")

# creation dune route eleves qui affiche des donnes 
@app.route("/eleves")
def list_eleves(): 
    return render_template("list_eleves.html", students=eleves)



if __name__ == "__main__": 
    app.run(debug=True )
