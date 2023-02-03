#IMPORTS
import sys
import struct

#DEFINES
ONE     = 1<<12

#VARIABLES
data         = []
vertex_count = 0

#DATA EXAMPLE
# { X, Y, Z, NX, NY, NZ, U, V }
# { F, F, F, F }

#####################
#    FUNCTIONS
#####################

def get_data(filename):
    global data, vertex_count

    eoh = False

    for line in open(filename, "r"):
        if "element vertex" in line:
            vertex_count = int(line.split(' ')[2])

        if "end_header" in line:
            eoh = True
            continue

        if eoh:
            line = line.split(' ')
            line[len(line)-1] = line[len(line)-1][:-1]
            data.append(line)


def export_data(filename):
    global data, vertex_count

    if ".mdl" not in filename:
        filename += ".mdl"

    for d in data:
        index = data.index(d)
        d = [float(x) for x in d]
        data[index] = d

    f = open(filename, "wb")
    f.write(struct.pack('<f', vertex_count))

    for d_arr in data:
        for d in d_arr:
            d = struct.pack('<f', d)
            f.write(d)



def print_data():
    pass

#####################
#    ENTRY POINT
#####################

if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_data(sys.argv[1])

        print_data()

        if len(sys.argv) > 2:
            export_data(sys.argv[2])
        else:
            export_data(sys.argv[1][:-4])