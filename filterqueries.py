#!/usr/bin/python3

import jaydebeapi
import sys
import json
import re

multicast_address = "127.0.0.1"
port_no = "20001" 
cluster_name = "myCluster"
username = "admin"
password = "admin" 

url = "jdbc:gs://" + multicast_address + ":" + port_no + "/" + cluster_name
conn = jaydebeapi.connect("com.toshiba.mwcloud.gs.sql.Driver",
    url, [username, password], "./gridstore-jdbc.jar")

curs = conn.cursor()

if False:
    question_name = "question"
    context_name = "context"
    answer_name = "answer"
else:
    question_name = "instruction"
    context_name = "input"
    answer_name = "response"
   
good=0
bad=0

with open(sys.argv[1]) as fd:

    for line in fd.readlines():
        data = json.loads(line)
        data[answer_name] = re.sub('"', '\'', data[answer_name])
        try:
            for stmt in data[context_name].split(";"):
                stmt = stmt.strip()
                table = stmt.split(" ")[2]
                curs.execute("DROP TABLE IF EXISTS "+table)
                curs.execute(stmt)
        except:
            pass

        try:
            curs.execute(data[answer_name])
            good=good+1
            print(json.dumps({"question": data[question_name], "context": data[context_name], "answer": data[answer_name]}))

        except:
            bad=bad+1


print("good:",good,file=sys.stderr)
print("bad:",bad,file=sys.stderr)
