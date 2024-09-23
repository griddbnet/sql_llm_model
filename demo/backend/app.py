from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
#from context import get_col_names
import json
import os
#import torch
import jpype
import jpype.dbapi2
import time

jpype.startJVM(jpype.getDefaultJVMPath(), "-ea")
url = "jdbc:gs://127.0.0.1:20001/myCluster/public"
conn = jpype.dbapi2.connect(url, driver="com.toshiba.mwcloud.gs.sql.Driver", driver_args={"user": "admin", "password": "admin"})

#device = "cuda:0" if torch.cuda.is_available() else "cpu"
device= "cpu"
print("Using ",device)
#model = AutoModelForSeq2SeqLM.from_pretrained("model/").to(device)
#tokenizer = AutoTokenizer.from_pretrained("t5-small")

def translate_to_sql_select(context, question):
    prompt = f"""Tables:
{context}

Question:
{question}

Answer:
"""
 
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(input_ids, generation_config=GenerationConfig(max_new_tokens=300))
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query



app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

cors = CORS(app)

@app.route('/')
@cross_origin()
def root():
    return app.send_static_file('index.html')

@app.route('/query')
@cross_origin()
def query():
   start = time.time()
   question = request.args.get('question')
   context = request.args.get('context')
   query = translate_to_sql_select(context,question)
   print(context)
   print(question)
   print(time.time() - start, ":", query)
   return query



@app.route('/nlquery')
def nlquery():
   # question = request.args.get('question')
   # context = "CREATE TABLE IF NOT EXISTS LOG_foo (timestamp TIMESTAMP, statusCode INTEGER, bytesReceived INTEGER, bytesSent INTEGER, contentLength INTEGER, requestedURL STRING); CREATE TABLE IF NOT EXISTS LOG_bar (timestamp TIMESTAMP, statusCode INTEGER, bytesReceived INTEGER, bytesSent INTEGER, contentLength INTEGER, requestedURL STRING); CREATE TABLE IF NOT EXISTS LOG_baz (timestamp TIMESTAMP, statusCode INTEGER, bytesReceived INTEGER, bytesSent INTEGER, contentLength INTEGER, requestedURL STRING);"
    # lets hard code query 
    # query = translate_to_sql_select(context,question)
    query = "Select humidity,co,light from device;"
    curs = conn.cursor()
    #col_names = get_col_names('device')
   # print(col_names)
    try:
        curs.execute(query)
        rows = curs.fetchall()
        return json.dumps(rows, default=str)
    except Exception as e: 
        print(e)
        abort(400, 'Generated query was not successful')

#@app.route('/nlquery')
#def nlquery():
#    question = request.args.get('question')
#    context = get_local_context() 
#    query = translate_to_sql_select(context,question)
#    curs = conn.cursor()
#   try:
#        curs.execute(query)
#        rows = curs.fetchall()
#        return json.dumps(rows) 
#    except:
#        abort(400, 'Generated query was not successful') 

if __name__ == '__main__':
   app.run(port=2929, debug=True)
