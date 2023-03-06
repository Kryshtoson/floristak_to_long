import pandas as pd

file=open("floristak_input",'r')

c=file.readlines()
for outer_i in range(0, len(c)):
    one_line = c[outer_i]
    one_sp = ''

    # get species name
    for i in one_line:
        if i != ':':
            one_sp = one_sp + i
        else:
            break
    print(one_sp)

    data = []
    one = ''
    remark_mode = False
    for i in range(len(one_sp), len(one_line)):
        #print(str(i) + ': ' + str(one_line[i]))
        if one_line[i] == '(':
            remark_mode = True

        if one_line[i] == ')':
            remark_mode = False

        if remark_mode == True:
            one = one + one_line[i]

        elif one_line[i] != ',':
            if one_line[i] != ' ':
                if one_line[i] != ':':
                    one = one + one_line[i]

        elif one_line[i] == ',':
            data.append(one)
            one = ''

        elif one_line[i] == '\n':
            data.append(one)
            one = ''

    if outer_i == 0:
        out_data = pd.DataFrame({'species': [one_sp] * len(data), 'data': data})

    else:
        out_data = pd.concat(out_data, pd.DataFrame({'species': [one_sp] * len(data), 'data': data}))
