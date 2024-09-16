#!/usr/bin/python3
import json
import datetime
from dateutil.relativedelta import relativedelta
import random
import re

TIME_PERIODS=["DAY", "MONTH", "YEAR"]
AGGREGATES=["MIN", "MAX", "AVG"]
HUMAN_AGGREGATES=["lowest", "highest", "average"]
STRINGS=["foo", "bar", "baz"]

def gen_time():
    RAND_TIME =  datetime.datetime.fromtimestamp(random.randrange(943920000, 1701302400))
    TIME_PERIOD = TIME_PERIODS[random.randrange(0,3)]
    time_fmt= None
    time_start =None
    time_end =None

    if TIME_PERIOD == "DAY":
        time_start = datetime.date(RAND_TIME.year, RAND_TIME.month, RAND_TIME.day)
        time_end = time_start + relativedelta(days=1)
        time_fmt = time_start.strftime("on %B %d, %Y")
    elif TIME_PERIOD == "MONTH":
        time_start = datetime.date(RAND_TIME.year, RAND_TIME.month, 1)
        time_end = time_start + relativedelta(months=1)
        time_fmt = time_start.strftime("in %B %Y")
    elif TIME_PERIOD == "YEAR":
        time_start = datetime.date(RAND_TIME.year, 1, 1)
        time_end = time_start + relativedelta(years=1)
        time_fmt = time_start.strftime("in %Y")
 
    return (time_fmt, time_start, time_end )

def gen_query(q):
    (time_fmt, time_start, time_end ) = gen_time()
    fmt_str = "%Y-%m-%dT%H:%M:%SZ"

    agg_rand = random.randrange(0,3)
    aggregate = AGGREGATES[agg_rand]
    aggregate_human = HUMAN_AGGREGATES[agg_rand]
    random_string = STRINGS[random.randrange(0, 3)]
    random_int = str(random.randrange(0, 100))
    column = None

    if 'columns' in q:
        column = q['columns'][random.randrange(0, len(q['columns']))]
        
    REPLACE_STRINGS = {
        "{HUMAN_TIME}" : time_fmt,
        "{TIME_START}" :  time_start.strftime(fmt_str),
        "{TIME_END}" : time_end.strftime(fmt_str),
        "{AGGREGATE}" : aggregate,
        "{HUMAN_AGGREGATE}" : aggregate_human,
        "{COLUMN}": column,
        "{RANDOM_INTEGER}" : random_int,
        "{RANDOM_STRING}" : random_string
    }

    sql = q['sql']
    human = q['human']
    for replace_string in REPLACE_STRINGS:
        sql = re.sub(replace_string, REPLACE_STRINGS[replace_string], sql)
        human = re.sub(replace_string, REPLACE_STRINGS[replace_string], human)
        
    return human, sql
output=[]
with open("queries.json") as f:
    queries = json.load(f)
    for qc in queries:
        for q in qc['queries']:
            for x in range(1, 2):
                    (human, sql) = gen_query(q)
                    print(json.dumps(({"context" : qc['context'], "question": human, "answer": sql })))

                
