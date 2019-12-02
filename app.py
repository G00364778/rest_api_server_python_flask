from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
  return "Hello, World This is changed"

@app.route('/book/<ont:id>')
def getBook(id):
  return "you want book with "+ str(id)

if __name__ == '__main__':
  app.run(debug = True)