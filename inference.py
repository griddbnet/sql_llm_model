#!/usr/bin/python3

# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
import os

model = AutoModelForSeq2SeqLM.from_pretrained("griddbcss_model_4_epoch")
tokenizer = AutoTokenizer.from_pretrained("t5-small")
new_tokens = ['<=', '<= ', ' <=', ' <', '<', '< ', '>= ', ' >=', '>=']
tokenizer.add_tokens(new_tokens)

def tokenize_function(context, question):
    start_prompt = "Tables:\n"
    middle_prompt = "\n\nQuestion:\n"
    end_prompt = "\n\nAnswer:\n"
    answer=""
    example={}
    data_zip = zip(context, question)
    prompt = [start_prompt + context + middle_prompt + question + end_prompt for context, question in data_zip]
    example['input_ids'] = tokenizer(prompt, padding="max_length", truncation=True, return_tensors="pt").input_ids
    example['labels'] = tokenizer(answer, padding="max_length", truncation=True, return_tensors="pt").input_ids

    return example

def translate_to_sql_select(context, question):
    prompt = f"""Tables:
{context}

Question:
{question}

Answer:
"""
 
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(input_ids, generation_config=GenerationConfig(max_new_tokens=1024))
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query

# Example usage

data = {"context": "CREATE TABLE IF NOT EXISTS devices (device_id INTEGER, ts TIMESTAMP, co DOUBLE, humidity DOUBLE,light BOOL,lpg DOUBLE,motion BOOL,smoke DOUBLE,temp DOUBLE);", "question": "What is the average lpg in December 2007 for all devices?", "answer": "SELECT AVG(lpg) FROM devices WHERE ts > TIMESTAMP('2007-12-01T00:00:00Z') and ts < TIMESTAMP('2008-01-01T00:00:00Z');"}
english_query = "Show all people older than 30"

#data = {"context": "CREATE TABLE IF NOT EXISTS iot_meter_foo (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_bar (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_baz (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE);", "question": "When is the lowest aqi for all meters at location baz?", "answer": "SELECT ts,MIN(aqi) FROM iot_meter_baz;"}

sql_query = translate_to_sql_select(data["context"],data["question"])
print("SQL Query:", sql_query)
