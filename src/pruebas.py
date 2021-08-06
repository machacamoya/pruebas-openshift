from flask import Flask, request
from time import strftime
from os import getenv

print("#######################")
print(__name__)
print("#######################")

app = Flask(__name__)

@app.route('/')
def hello():
    with open("/log/pcm.log","a") as fp:
        fp.write( "Fecha y hora " + strftime("%c"))
        fp.write('\t- Hello, World!\n')
        if getenv('PCM'):
            fp.write(getenv('PCM') + '\n')
    return 'Hello, World!'

@app.route('/p')
def parametros():
    par1 = request.args.get('par1','ninguno')
    par2 = request.args.get('par2','ninguno')
    with open("/log/pcm.log","a") as fp:
        fp.write( "Fecha y hora " + strftime("%c"))
        fp.write('\t- Se ha introducido.............{}--{}\n'.format(par1, par2))
        if getenv('PCM'):
            fp.write(getenv('PCM') + '\n')
    return 'Se ha introducido.............{}--{}'.format(par1, par2)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
