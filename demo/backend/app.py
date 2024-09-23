from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
#from context import get_col_names
import json
import os
import torch
import jpype
import jpype.dbapi2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
import time
from context import *

jpype.startJVM(jpype.getDefaultJVMPath(), "-ea")
url = "jdbc:gs://127.0.0.1:20001/myCluster/public"
conn = jpype.dbapi2.connect(url, driver="com.toshiba.mwcloud.gs.sql.Driver", driver_args={"user": "admin", "password": "admin"})

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = AutoModelForSeq2SeqLM.from_pretrained("griddbnet/griddb_sql_llm").to(device)
tokenizer = AutoTokenizer.from_pretrained("t5-small")
new_tokens = ['<=', '<= ', ' <=', ' <', '<', '< ', '>= ', ' >=', '>=']
tokenizer.add_tokens(new_tokens)

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
    question = request.args.get('question')
    context = get_local_context() 
    print("Question:", question)

    model_start = time.time()
    query = translate_to_sql_select(context,question)
    model_end = time.time()
    print("Query:", query)

    query_start = time.time()
    curs = conn.cursor()
    try:
        curs.execute(query)
        rows = curs.fetchall()
        query_end = time.time()
        return json.dumps({ 'model_time' : model_end - model_start, 
                            'query_time' : query_end - query_start, 
                            'query': query , 'results': rows })
    except Exception as e: 
        print(e)
        abort(400, 'Generated query was not successful')

if __name__ == '__main__':
   app.run(port=2929, debug=True)
