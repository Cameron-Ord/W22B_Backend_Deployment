#importing
import json
from flask import Flask,request, make_response, jsonify
import dbhelper, api_helper, dbcreds
import uuid
app = Flask(__name__)

@app.post('/api/client')
#function gets called on api request
def new_client():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'email', 'password', 'bio', 'image_url']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL new_client(?,?,?,?,?)', [request.json.get('username'), request.json.get('email'), request.json.get('password'), request.json.get('bio'), request.json.get('image_url')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')


@app.post('/api/login')
#function gets called on api request
def login():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'password']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to insert sent information into the DB
         token = uuid.uuid4().hex
         results = dbhelper.run_proceedure('CALL client_login(?,?,?)', [token, request.json.get('username'), request.json.get('password')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')
      
      
@app.delete('/api/login')
#function gets called on api request
def delete_log():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['token']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to delete information from the DB based on input
         results = dbhelper.run_proceedure('CALL log_out(?)', [request.json.get('token')])
         #returns results from db run_procedure
         return make_response(jsonify(results), 200)
     

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')

@app.get('/api/client')
#function gets called on api request
def get_client():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.args, ['token']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the procedure to retrieve information from the DB
         results = dbhelper.run_proceedure('CALL get_client(?)', [request.args.get('token')])
         #returns results from db run_procedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something has gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print('something went wrong')

#running @app
if(dbcreds.production_mode == True):
   print()
   print('----Running in Production Mode----')
   print()
   import bjoern #type: ignore
   bjoern.run(app,"0.0.0.0", 5532)
else:
   from flask_cors import CORS
   CORS(app)
   print()
   print('----Running in Testing Mode----')
   print()
   app.run(debug=True)