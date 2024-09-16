#!/usr/bin/python3

import sys
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict, load_dataset, interleave_datasets, load_from_disk
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, TrainingArguments, Trainer
import torch
import time
import evaluate
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("Using ",device)

model_name='t5-small'

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
new_tokens = ['<=', '<= ', ' <=', ' <', '<', '< ', '>= ', ' >=', '>=']
tokenizer.add_tokens(new_tokens)

dataset_test = load_dataset("json", data_files=sys.argv[1])['train']

questions = dataset_test['question']
contexts = dataset_test['context']
human_baseline_answers = dataset_test['answer']

original_model_answers = []
model_answers = []

model = AutoModelForSeq2SeqLM.from_pretrained(sys.argv[2]).to(device)
#model = AutoModelForSeq2SeqLM.from_pretrained("griddb_model_2_epoch")
model.resize_token_embeddings(len(tokenizer))


for idx, question in enumerate(questions):
    
    prompt = f"""Tables:
{contexts[idx]}

Question:
{question}

Answer:
"""
      
    input_ids = tokenizer(prompt, return_tensors="pt").to(device).input_ids
    human_baseline_text_output = human_baseline_answers[idx]
    
    model_outputs = model.generate(input_ids=input_ids, generation_config=GenerationConfig(max_new_tokens=1024))
    model_text_output = tokenizer.decode(model_outputs[0], skip_special_tokens=True )
    model_answers.append(model_text_output)

zipped_summaries = list(zip(questions, human_baseline_answers, model_answers))
 
df = pd.DataFrame(zipped_summaries, columns = ['human_baseline_answers', 'original_model_answers', 'model_answers'])
df.to_csv(sys.argv[2]+'.csv', index=False)  

rouge = evaluate.load('rouge')
model_results = rouge.compute(
    predictions=model_answers,
    references=human_baseline_answers[0:len(model_answers)],
    use_aggregator=True,
    use_stemmer=True,
)

print(model_results)
