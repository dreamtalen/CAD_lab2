import argparse
parser = argparse.ArgumentParser()
parser.add_argument('test_in')
args = parser.parse_args()
test_file = args.test_in

boolean_dict = {'-':[True, True], '0':[True, False], '1':[False, True]}
reversed_boolean_dict = {(True, True):'-', (True, False):'0', (False, True):'1'}

def DeMorgan_Laws(cubelist_f, var_num):
    result = []
    for index, boolean in enumerate(cubelist_f[0]):
        if boolean == [True, True]: pass
        elif boolean == [True, False]:
            result.append([[False, True] if i == index else [True, True] for i in range(var_num)])
        else:
            result.append([[True, False] if i == index else [True, True] for i in range(var_num)])
    return result

def Select_most_binate_var(cubelist_f, var_num):
    True_dict = {i:0 for i in range(var_num)}
    Complement_dict = {i:0 for i in range(var_num)}
    for cube in cubelist_f:
        for index, value in enumerate(cube):
            if value == [False, True]: True_dict[index] += 1
            elif value == [True, False]: Complement_dict[index] += 1
            else:   pass
    binate_list = [i for i in range(var_num) if True_dict[i] and Complement_dict[i]]
    if binate_list:
        # Pick the binate variable in the most cubes
        biggest_appearance = max(True_dict[i] + Complement_dict[i] for i in binate_list)
        binate_list_most_cubes = [i for i in binate_list if True_dict[i] + Complement_dict[i] == biggest_appearance]
        # Break ties with the smallest abs(T-C), and then with the smallest variable index
        return min(binate_list_most_cubes, key=lambda x: abs(True_dict[x] - Complement_dict[x]))
    else:
        # Pick the unate variable in the most cubes
        biggest_appearance = max(True_dict[i] + Complement_dict[i] for i in range(var_num))
        unate_list_most_cubes = [i for i in range(var_num) if True_dict[i] + Complement_dict[i] == biggest_appearance]
        # Break ties with smallest variable index
        return min(unate_list_most_cubes)

def positiveCofactor(cubelist_f, x):

def negativeCofactor(cubelist_f, x):

def Complement(cubelist_f, var_num):
    # Empty cube list
    if not cubelist_f:
        return [[True, True] for i in range(var_num)]
    # Cube list contains All-Don't-Cares Cube
    elif [[True, True] for i in range(var_num)] in cubelist_f:
        return []
    # Cube list contains just one cube
    elif len(cubelist_f) == 1:
        return DeMorgan_Laws(cubelist_f, var_num)
    else:
        # Do recursion
        x = Select_most_binate_var(cubelist_f, var_num)
        cubelist_p = Complement(positiveCofactor(cubelist_f, x), x)
        cubelist_N = Complement(cubelist_f, x)

    return cubelist_f

def main():
    input_f = []
    with open(test_file) as f:
        var_num = int(f.readline().strip())
        for line in f.readlines():
            input_f.append([boolean_dict[i] for i in line.strip()])
    output_f = Complement(input_f, var_num)
    print var_num
    for cube in output_f:
        print ''.join([reversed_boolean_dict[tuple(i)] for i in cube])

if __name__ == '__main__':
    main()
    # a = DeMorgan_Laws([[[True, True], [False, True], [True, False], [False, True]]], 4)
    # for cube in a:
    #     print ''.join([reversed_boolean_dict[tuple(i)] for i in cube])