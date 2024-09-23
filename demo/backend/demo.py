from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
import json
import os
import torch
import jpype
import jpype.dbapi2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from context import *
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea")
url = "jdbc:gs://192.168.168.192:20001/myCluster/public"
conn = jpype.dbapi2.connect(url, driver="com.toshiba.mwcloud.gs.sql.Driver", driver_args={"user": "admin", "password": "admin"})

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("Using ",device)
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


def nlquery(question):
    context = get_local_context() 
    print("Question:", question)
    query = translate_to_sql_select(context,question)
    print("Query:", query)
    curs = conn.cursor()
    try:
        curs.execute(query)
        rows = curs.fetchall()
        print("Rows:",rows)
    except: 
        print("invalid query")
        

if __name__ == '__main__':
    nlquery("Show all logs from server foo")
    nlquery("What is the highest bytesSent for server baz?")
    nlquery("What is the average contentLength in March 9, 2009 for the server foo?")
    nlquery("How many status code 404 on server bar on April 4, 2010?")

