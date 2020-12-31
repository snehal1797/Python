import subprocess


def get_cmd():
    cmd = input("Enter CMD or type 'b' to break: ")
    return cmd


def cmd_exec(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    status = 'Success'
    error = 'None'
    if len(output) == 0:
        output = ""
        status = "Failed"
        error = f"{cmd} is not recognized as an internal or external command,operable program or batch file."
    else:
        output = str(output)
    return output, error, status


res_li = []

while True:
    cmd = get_cmd()
    if cmd.lower() == 'b':
        break
    try:
        output, error, status = cmd_exec(cmd)
    except:
        output = ""
        status = "Failed"
        error = "None"
    res_dict = {
        cmd: {
            "output": output,
            "status": status,
            "error": error

        }
    }

    res_li.append(res_dict)
key_list = []
value_list = []
for i in res_li:
    for k, v in i.items():
        if k not in key_list:
            key_list.append(k)
            value_list.append(v)
dic = {}
for i in range(len(key_list)):
    dic[key_list[i]]=value_list[i]
print(dic)
