import sys
import os


class Parser:
    def __init__(self):
        self.file_name = None
        self.lines = None
        self.filter_input = None
        self.n_lines_data = None
        self.filter_input_modified = []

    def read_file_data(self):
        with open(self.file_name, 'r', encoding="UTF-8") as file:
            data = [next(file) for x in range(self.lines)]
        self.n_lines_data = data

    def get_input(self):
        file_name = input("Enter log file name: ")
        if not os.path.exists(file_name):
            print("Enter Correct file-name")
            sys.exit()
        try:
            num_lines = int(input("Enter number of lines you want to read: "))
        except:
            num_lines = 10
        filter_input = (input("Types of log messages 'ERROR','DEBUG','INFO','WARNING': ") or "ERROR").split(",")

        for i in filter_input:
            i = i.upper().replace(" ", "")
            if i not in ['ERROR', 'DEBUG', 'INFO', 'WARNING']:
                print("invalid input: ", i)
                sys.exit()
            else:
                self.filter_input_modified.append('[' + i + ']')

        self.file_name = file_name
        self.lines = num_lines
        self.filter_input = filter_input
        # print(self.filter_input_modified)

    def filter_data_display(self):
        output_list = []

        for i in self.filter_input_modified:
            for j in self.n_lines_data:
                if i in j.split(" "):
                    output_list.append(j)

        return output_list


obj = Parser()
obj.get_input()
obj.read_file_data()
output_list = obj.filter_data_display()
print(output_list)
