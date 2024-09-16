#!/usr/bin/python3

import pandas as pd
import sys

pd.options.display.max_colwidth = 100

df = pd.read_csv(sys.argv[1])
df['original_model_answers'] = df['original_model_answers'].str.lower()
df['model_answers'] = df['model_answers'].str.lower()

match = df[df['original_model_answers'] == df['model_answers']]
print(match.shape)
print(match['model_answers'])
