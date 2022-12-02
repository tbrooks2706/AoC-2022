#this is a set of reusable functions

#opening input file and putting it in a list
def read_file(file_path):
    with open(file_path) as txt_file:
        init_list = []
        for line in txt_file:
            init_list.append(line.replace("\n", ""))
    return init_list