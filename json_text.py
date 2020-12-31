import json


def get_input():
    inp = input("Enter Memory/CPU/Linux/windows: ").upper()

    pattern = ['MEMORY', 'CPU', 'LINUX', 'WINDOWS']

    if inp not in pattern:
        print("Exception: Invalid Choice")

    return inp


def get_sys_memory_cpu(inp):
    inp = inp.lower()
    with open('inventory.json', 'r', encoding='UTF-8') as file:
        data = file.read()
    data_list=[]
    data_dict = json.loads(data)
    for i in data_dict["inventory"]:
        (data_list.append(i))









def get_win_linux(inp):
    inp = inp.lower().capitalize()
    with open('inventory.json', 'r', encoding='UTF-8') as file:
        data = file.read()
    data_dict = json.loads(data)
    all_sys = []
    for key, val in data_dict.items():
        for ind, dict_ele in enumerate(val):
            if (ind + 1) % 2 == 0:
                win_linux = dict_ele.get('os')
                if inp == win_linux:
                    all_sys.append(dict_ele)
    return all_sys


inp = get_input()

if inp in ['MEMORY']:
    data_dict = get_sys_memory_cpu(inp)
    print(data_dict)

if inp in ['LINUX', 'WINDOWS']:
    all_sys = get_win_linux(inp)
    print(all_sys)
