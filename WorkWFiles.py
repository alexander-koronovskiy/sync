def write_to_file(array, filename):
    f = open(filename, 'w')
    for index in array:
        f.write(str(index) + '\n')
    f.close()


def write_to_list(f):
    data_list = list()
    with open(f, "r") as file:
        for line in file:  # file.readlines()
            data_list = data_list + list(map(float, line.split()))
    return(data_list)
