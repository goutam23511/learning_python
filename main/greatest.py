#implementing modules for the first time 

def max_num(list):
    greatest=list[0]
    for i in list:
        if i>greatest:
            greatest=i
    return greatest

