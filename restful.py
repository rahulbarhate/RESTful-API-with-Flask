from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name' : 'Python'}, {'name' : 'C++'}, {'name' : 'Java'}]

@app.route("/", methods=['GET'])
def test():
    return jsonify({'message' : 'The App Works!'})

@app.route("/lang", methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@app.route("/lang/<string:name>", methods=['GET'])
def returnOne(name):
    langs = [x for x in languages if x['name']==name]
    return jsonify({'name':langs[0]})

@app.route("/lang", methods = ['POST'])
def addOne():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

@app.route("/lang/<string:name>", methods= ['PUT'])
def editOne(name):
    langs = [x for x in languages if x['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

@app.route("/lang/<string:name>", methods = ['DELETE'])
def deleteOne(name):
    langs = [x for x in languages if x['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages' : languages})

if __name__=='__main__':
    app.run(debug=True)