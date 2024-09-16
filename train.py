#!/usr/bin/python3

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

tok_model_name='t5-small'
model_name='filtered_model_4_epoch/'

tokenizer = AutoTokenizer.from_pretrained(tok_model_name)
tokenizer.pad_token = tokenizer.eos_token
new_tokens = ['<=', '<= ', ' <=', ' <', '<', '< ', '>= ', ' >=', '>=']

dataset_train = load_dataset("json", data_files="data/griddb.json", split='train[:80%]')
dataset_test = load_dataset("json", data_files="data/griddb.json", split='train[-20%:-10%]')
dataset_val = load_dataset("json", data_files="data/griddb.json", split='train[-10%:]')

dataset = DatasetDict({ 'train': dataset_train,
                    'test': dataset_test,
                    'validation': dataset_val})


def tokenize_function(example):
    
    start_prompt = "Tables:\n"
    middle_prompt = "\n\nQuestion:\n"
    end_prompt = "\n\nAnswer:\n"
  
    data_zip = zip(example['context'], example['question'])
    prompt = [start_prompt + context + middle_prompt + question + end_prompt for context, question in data_zip]
    example['input_ids'] = tokenizer(prompt, padding='max_length', truncation=True, return_tensors="pt").input_ids
    example['labels'] = tokenizer(example['answer'], padding='max_length', truncation=True, return_tensors="pt").input_ids
    
    return example



finetuned_model = AutoModelForSeq2SeqLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(tok_model_name)
tokenizer.add_tokens(new_tokens)
finetuned_model.resize_token_embeddings(len(tokenizer))

tokenized_datasets = dataset.map(tokenize_function, batched=True)

output_dir = f'./sql-training-{str(int(time.time()))}'

training_args = TrainingArguments(
    output_dir=output_dir,
    learning_rate=5e-3,
    num_train_epochs=2,
    per_device_train_batch_size=8,     # batch size per device during training
    per_device_eval_batch_size=8,      # batch size for evaluation
    weight_decay=0.01,
    logging_steps=50,
    evaluation_strategy='steps',        # evaluation strategy to adopt during training
    eval_steps=500,                     # number of steps between evaluation
)

trainer = Trainer(
    model=finetuned_model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
)

trainer.train()

finetuned_model.save_pretrained("griddb_model_4_epoch")
