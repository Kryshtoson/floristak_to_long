import pandas as pd

file = open("floristak_input", 'r', encoding="utf8")

c = file.readlines()

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
    remarks = []
    one = ''
    remark = ''
    remark_mode = False

    for i in range(len(one_sp), len(one_line)):
        print(str(i) + ': ' + str(one_line[i]))
        if one_line[i] == '(':
            remark_mode = True

        if one_line[i] == ')':
            remark_mode = False

        if remark_mode:
            if one_line[i] != '(':
                remark = remark + one_line[i]

        elif one_line[i] != ',':
            if one_line[i] != ' ':
                if one_line[i] != ':':
                    if one_line[i] != ')':
                        if one_line[i] != '\n':
                            one = one + one_line[i]

        elif one_line[i] == ',':
            data.append(one)
            remarks.append(remark)
            one = ''
            remark = ''

        if one_line[i] == '\n':
            data.append(one)
            remarks.append(remark)
            one = ''
            remark = ''

    if outer_i == 0:
        out_data = pd.DataFrame({'species': [one_sp] * len(data), 'data': data, 'remarks': remarks})

    else:
        out_data = pd.concat([out_data, pd.DataFrame({
            'species': [one_sp] * len(data),
            'data': data,
            'remarks': remarks
        })])

out_data['data'] = [int(i) for i in out_data['data']]
out_data.to_excel('floristak_out.xlsx', index=False)
