
def get_values():
    f = open("football_values.txt", "r")
    values = (f.read())

    # conver to the list
    list = values.split (",")

    # convert each element as integers
    li = []
    for i in list:
	    li.append(float(i))

    return li

football_values = get_values()
