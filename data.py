data = []

def getdata(data):
    globals()["data"].append(data)
    f = open("data.txt", "a")
    f.write("\n")
    f.write(str(data))

