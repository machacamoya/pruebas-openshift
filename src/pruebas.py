from flask import Flask
from flask import request

print("#######################")
print(__name__)
print("#######################")

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/p')
def parametros():
    par1 = request.args.get('par1','ninguno')
    par2 = request.args.get('par2','ninguno')
    return 'Se ha introducido.............{}--{}'.format(par1, par2)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
