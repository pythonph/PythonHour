#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, jsonify, json, request
app = Flask(__name__)

# serve a static html page
@app.route("/")
def hello():
    return app.send_static_file("index.html")

# simple api implementation
@app.route("/user")
def user():
    return jsonify({
        'name': 'Jeff',
        'email': 'jeff@python.ph'
    })

# Demonstrate http methods and flask routing

# api to get a cat
@app.route("/cat", methods=['GET'])
def cat():
    return jsonify({
        'name': 'mingming',
        'type':'🐈',
        'color': 'orange'
    })
    
# api to search for a cat
@app.route("/search-cat", methods=['GET'])
def search_cat():
    # get parameter from request
    name = request.args.get('name')
    print(name)
    
    # read record from a temporary file
    with open('/tmp/data.txt','r') as file:
        data = file.read()
        records = json.loads(data)
    for record in records:
        if record['name'] == name:
            return jsonify(record)
    return jsonify({'error': 'I cant find the data'})

# api to create a cat
@app.route("/create-cat", methods=['PUT'])
def create_cat():
    record = json.loads(request.data)
    print(record)
    # read record from a temporary file
    with open('/tmp/data.txt','r') as file:
        data = file.read()
    if not data:
        # create a new record
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    
    # store record into a temporary file
    with open('/tmp/data.txt','w') as file:
        file.write(json.dumps(records, indent=2))
    
    # return body 
    return jsonify(record)

# api to delete a cat record
@app.route("/delete-cat", methods=['DELETE'])
def delete_cat():
    record = json.loads(request.data)
    new_records = []
    # read record from a temporary file
    with open('/tmp/data.txt','r') as file:
        data = file.read()
        records = json.loads(data)
    for item in records:
        if item['name'] == record['name']:
            continue
        new_records.append(item)
    
    # store record into a temporary file
    with open('/tmp/data.txt','w') as file:
        file.write(json.dumps(new_records, indent=2))
    
    # return body
    return jsonify(new_records)


# Run the Flask application
if __name__ == '__main__':
  app.run(debug=True)
  
# Run this application by typing this in terminal:
# > python app.py