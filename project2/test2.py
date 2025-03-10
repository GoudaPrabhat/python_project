def update_page(path, key, value):
    with open(path, 'r') as namefile:
        lines = namefile.readlines()
    with open(path, 'w') as namefile:
        for line in lines:
            if key in line:
                namefile.write(key + " = " + value + "\n")
            else:
                namefile.write(line)

mypath = 'name.txt'
mykey = "My_name"
myvalue = "Prabhat"

update_page(mypath,mykey, myvalue)