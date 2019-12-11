from flask import Flask, jsonify, request, abort, make_response
from bookDAO import bookDAO
from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

app = Flask(__name__, static_url_path='', static_folder='.')

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)
    return jsonify(foundBook)

@app.route('/pidat')
def piGetAll():
    piData = bookDAO.piGetAll()
    return jsonify(piData)

@app.route('/plot/piplot')
def piGetPlot():
    temp=[]
    humid=[]
    press=[]
    piData = bookDAO.piGetSome()
    #print(piData)
    for dat in piData:
        print('Pi Data Line: {}'.format(dat))
        temp.append(dat['temp'])
        humid.append(dat['humid'])
        press.append(dat['press'])
    
    fig=Figure()
    axis1 = fig.add_subplot(3,1,1)
    axis2 = fig.add_subplot(3,1,2)
    axis3 = fig.add_subplot(3,1,3)
    
    axis1.grid(True)
    axis2.grid(True)
    axis3.grid(True)
    xs=range(len(temp))
    
    axis1.plot(xs,temp, 'r')
    axis2.plot(xs,humid, 'g')
    axis3.plot(xs,press, 'b')
    axis1.legend(['Temp'])
    axis2.legend(['Humidity'])
    axis3.legend(['Pressure'])
    
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

# curl -v --trace debug.log -i -H "Content-Type:application/json" -X POST -d @post.json http://jattie.pythonanywhere.com/pisense
# post.json = {"TempExternal": 21, "TempOnboard": 26, "Brightness": -2, "Humidity": 20, "BaroTemp": 27, "BaroPressure": 1009.22, "MotionDetected": "False"}
@app.route('/pisense', methods=['POST'])
def processPiSensorData():
    if not request.json:
        abort(400)
    print(request.json)
    # {'TempExternal': 21, 'TempOnboard': 26, 'Brightness': -2, 'Humidity': 20, 'BaroTemp': 27, 'BaroPressure': 1009.22, 'MotionDetected': 'False'}
    data = {
        "TempExternal": request.json['TempExternal'],
        "TempOnboard": request.json['TempOnboard'],
        "Brightness": request.json['Brightness'],
        "Humidity": request.json['Humidity'],
        "BaroTemp": request.json['BaroTemp'],
        "BaroPressure": request.json['BaroPressure'],
        "MotionDetected": request.json['MotionDetected']
    }
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    values = (date_time, data['TempExternal'], data['TempOnboard'], data['Brightness'], data['Humidity'], data['BaroTemp'], data['BaroPressure'], data['MotionDetected'])
    newID = bookDAO.insertIntoSense(values)
    data['id'] = newID
    return jsonify(data)
    
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price'],
    }
    values =(book['Title'],book['Author'],book['Price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    if not foundBook:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundBook['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundBook['Price'] = reqJson['Price']
    values = (foundBook['Title'],foundBook['Author'],foundBook['Price'],foundBook['idx'])
    bookDAO.update(values)
    return jsonify(foundBook)
        
@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)
