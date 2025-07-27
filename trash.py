values = [1, 2, 3 ,4, "vjhsuv", "sdbvsid", 10]

str_value = ""
counter = 0

while 1:
    if  len(values) != counter:
        str_value += "%s"
        if len(values) - 1 != counter:
            str_value += ", "
        
        counter += 1
    else:
        break

print(str_value)