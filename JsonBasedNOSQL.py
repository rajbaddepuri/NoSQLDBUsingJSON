import sys,os
import json
from json import JSONDecodeError


def menu():
    _raw_data = {}
    mode = "r+"
    if not os.path.exists("records.json"):
        mode = 'w+'
    with open("records.json", mode) as f:
        try:
            _raw_data = json.load(f)
        except JSONDecodeError as e:
            print("json file may not be existed, expected behaviour..")
            _raw_data = {}
        if not _raw_data:
            _fields = input(""""
            Since there is no data, please add field (Column names in DB) names first using comma seperated.
            Note that Un ique ID is already included
            For example: Name,Age,address : """)
            if _fields.strip():
                _keys = _fields.strip().split(",")
                _keys.append("ID")
                _raw_data["keys"] = _keys
                _raw_data["actual_values"] = {}
                _raw_data["max_id"] = 0
    print("************MAIN MENU**************")
    # time.sleep(1)
    while True:
        choice = input("""
                          1: Add a record
                          2: Delete a record
                          3: Find record(s)
                          4: Save
                          5: Quit
                          Please enter your choice: """)

        choice = choice.strip()
        updated_data = _raw_data
        if choice == "1":
            updated_data = add_record(_raw_data)
        elif choice == "2":
            updated_data = delete_record(_raw_data)
        elif choice == "3":
            find_record(_raw_data)
        elif choice == "4":
            print("Updating JSON file with the latest content")
            _raw_data = save_records(updated_data)
        elif choice == "5":
            print("Updating JSON file with the latest content")
            with open("records.json", 'w+') as f:
                json.dump(updated_data, f)
            print("==================Thanks for using, Bye====================")
            sys.exit()
        else:
            print("You must only select either 1,2,3,4 or 5, Please try again")

def save_records(raw_data):
    _raw_data = raw_data
    with open("records.json", 'w+') as f:
        json.dump(_raw_data, f)
    print("Updated new records")
    with open("records.json", 'r+') as f:
        _raw_data = json.load(f)
    return _raw_data

def add_record(raw_data):
    _local_dict = {}
    for key in raw_data["keys"]:
        if key == "ID":
            _val = raw_data["max_id"] + 1
            raw_data["max_id"] = _val
        else:
            _str = "Enter value for key: %s : " %key
            _val = input(_str)
        while True:
            if len(str(_val).strip()) == 0:
                _val = input("Empty values can not be accepted, please try again : ")
            else:
                break
        _local_dict[key] = str(_val).strip()
    raw_data["actual_values"][raw_data["max_id"]] = _local_dict
    print("Updated data with provided records, Please choose menu option")
    return raw_data


def delete_record(raw_data):
    validations(raw_data)
    _key_to_delete = ''
    _val_to_delete = ''
    while True:
        print("Available KEYS are: "+",".join(raw_data['keys']))
        _key_to_delete = input("""
            Enter KEY to delete a record or Q for go back to main menu : """)
        if _key_to_delete.strip() == 'Q':
            return
        if not _key_to_delete.strip() or _key_to_delete.strip() not in raw_data['keys']:
            print("Given KEY is not a valid key, please provide a KEY name from a list above\n\n")
        else:
            break

    while True:
        _val_to_delete = input("""
                    Enter VALUE to delete a record or Q for go back to main menu : """)
        if _val_to_delete.strip() == 'Q':
            return
        if not _val_to_delete.strip():
            print("Given VALUE is not a valid value, please provide a valid value")
        else:
            break
    _delete_val_lst = []
    for key,val in raw_data['actual_values'].items():
        if _key_to_delete in val.keys():
            if(val[_key_to_delete] == _val_to_delete):
                _delete_val_lst.append(key)

    for key in _delete_val_lst:
        _tmp = raw_data['actual_values'][str(key)]
        del (raw_data['actual_values'][str(key)])
        print("Deleted record: %s" % _tmp)
    if not _delete_val_lst:
        print("No Data found\n")

def find_record(raw_data):
    validations(raw_data)
    _fields = []
    _where_clause = []
    print("Available KEYS are: "+",".join(raw_data['keys']))
    _fields = input("""
        Enter Field names to disaplay values (comma saparated if multiple).
        Ex: ID,Name,Age 
        Q for go back to home
        A to display all fields""")

    if _fields.strip() == 'Q':
        return
    elif len(_fields.strip()) == 0 or _fields.strip() == 'A':
        print("Empty value given, Considering all fields")
        _fields = raw_data['keys']
    else:
        _fields = _fields.strip().split(',')
        _check = [key for key in _fields if key not in raw_data['keys']]
        if _check:
            print("Invalid field name found. Considering all fields")
            _fields = raw_data['keys']

    print("Available KEYS are: " + ",".join(raw_data['keys']))
    _where_clause = input("""
            Enter Field names(like where clause) to disaplay values (comma saparated if multiple).
            Ex: ID,Name,Age 
            Q for go back to home
            N for no where clause""")
    if _where_clause.strip() == 'Q':
        return
    elif len(_where_clause.strip()) == 0 or _where_clause.strip() == 'N':
        print("Empty value given or N selected, Considering all fields without any where clause")
        _where_clause = []
    else:
        _where_clause = _where_clause.strip().split(',')
        _check = [key for key in _where_clause if key not in raw_data['keys']]
        if _check:
            print("Invalid field name found. Considering no where clause")
            _where_clause = []

    _res_raw_data = {}
    if _where_clause:
        _wh_dict = {}
        for _where_clause_item in _where_clause:
            _val = ''
            while True:
                _val = input("Enter value for field(acts like WHERE AGE='<some>') "+_where_clause_item+": ")
                if len(_val.strip()) == 0:
                    print("Given invalid value for field %s" %_where_clause_item)
                else:
                    break
            for key,v in raw_data['actual_values'].items():
                if v[_where_clause_item] ==_val:
                    if not key in _res_raw_data.keys():
                        _res_raw_data[key] = v
    else:
        _res_raw_data = raw_data['actual_values']

    _del_fields = [field for field in list((list(_res_raw_data.values())[0]).keys()) if field not in _fields]
    for k, v in _res_raw_data.items():
        for del_field in _del_fields:
            del(v[del_field])

    _print_keys = list(_res_raw_data.keys())
    _print_vals = list(_res_raw_data.values())
    _max_id_len = max([len(i) for i in _print_vals[0].keys()])
    _str = " "+"\t".join(_print_vals[0].keys())
    print(_str)
    print(((len(_str))+5)*"=")
    for val in _print_vals:
        print("\t".join(val.values()))


def view_by_field(raw_data):
    validations(raw_data)
    print("student details by field")

def validations(_json_raw_data):
    if not _json_raw_data:
        print("There are no data to perform operation, please add some records before you proceed")
    if type(_json_raw_data) is not dict:
        print("Given data is not in expected format")

if __name__ == "__main__":
    menu()



