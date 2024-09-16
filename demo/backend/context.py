#!/usr/bin/python3

import griddb_python as griddb
import json

factory = griddb.StoreFactory.get_instance()
DB_HOST = "127.0.0.1:10001"
DB_CLUSTER = "myCluster"
DB_USER = "admin"
DB_PASS = "admin"
gridstore = factory.get_store(
            notification_member=DB_HOST, cluster_name=DB_CLUSTER, username=DB_USER, password=DB_PASS)
 
list_of_statements = []

def type_mapping(type_num):
    type = ""
    if type_num ==  0:
        type = "STRING"
    elif type_num ==  1:
        type = "BOOL"
    elif type_num ==  4:
        type = "INTEGER"
    elif type_num ==  6:
        type = "FLOAT"
    elif type_num ==  8:
        type = "TIMESTAMP"
    else:
        type = "STRING"
    return type

def create_table_statement(cont_name, schema):
    schema_str = col_name_and_type(schema)
    str = "CREATE TABLE IF NOT EXISTS "
    str = str+cont_name + " ("
    str = str + schema_str
   # print("Adding '" + str + "' to list")
    list_of_statements.append(str)
    
def col_name_and_type(schema):
    str = ""
    for key in schema:
        str = str+ " " + key+ " " + schema[key] + ","
    str = str[:-1] #remove trailing comma
    str = str+");"
    return str

def get_select_statements():
    try:
        containers = []
        x = 0
        while x < gridstore.partition_info.partition_count:
            containers.extend(gridstore.partition_info.get_container_names(x, 0))
            x=x+1
        
        conts_and_schemas = {}
        for cont in containers:
            col_list = gridstore.get_container_info(cont).column_info_list
            schema = {}
            for row in col_list:
                schema[row[0]] = type_mapping(row[1])
            conts_and_schemas[cont] = schema
        for key in conts_and_schemas:
            select_statement = create_table_statement(key, conts_and_schemas[key])

        return list_of_statements

    except griddb.GSException as e:
        for i in range(e.get_error_stack_size()):
            print("[", i, "]")
            print(e.get_error_code(i))
            print(e.get_location(i))
            print(e.get_message(i))

def main():
    print(get_select_statements())

if __name__=="__main__":
    main()
