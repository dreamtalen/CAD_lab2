import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test_in')

args = parser.parse_args()

test_file = args.test_in

boolean_dict = {'-':[True, True], '0':[False, False], '1':[False, True]}
reversed_boolean_dict = {(True, True):'-', (False, False):'0', (False, True):'1'}

def complement(cubelist_f, var_num):
    return  cubelist_f
    # if empty_cubelist(cubelist_f):
    #     return

def main():
    input_f = []
    with open(test_file) as f:
        var_num = int(f.readline().strip())
        for line in f.readlines():
            input_f.append([boolean_dict[i] for i in line.strip()])
    output_f = complement(input_f, var_num)
    print var_num
    for cube in output_f:
        print ''.join([reversed_boolean_dict[tuple(i)] for i in cube])


if __name__ == '__main__':
    main()