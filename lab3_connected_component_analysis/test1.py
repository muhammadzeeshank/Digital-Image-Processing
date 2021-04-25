table = [[1, 3], [2], [6, 7, 8]]
pre_element = 7
element = 8

check = False
if len(table) > 1:
    check = True
    for l in table:
        el = False
        prel = False
        for i in l:
            if i == element:
                el = True
            if i == pre_element:
                prel = True
            if el == True & prel == True:
                check = False
                break
if check:
    for l in table:
        for i in l:
            if i == element:
                val = table.pop(table.index(l))
    for l in table:
        for i in l:
            if i == pre_element:
                for x in val:
                    l.append(x)


print(table)
# print(val)
