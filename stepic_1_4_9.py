__author__ = 'eugene.riabukha'


def create(key, value):
    if namespace.get(key) is True:
        namespace[key].append(value)
    else:
        namespace[key] = [value]


def add(key, value):
    if variable.get(key) is True:
        variable[key].append(value)
    else:
        variable[key] = [value]

def get(key, value):



if __name__ == "__main__":
    n = int(input("Input number of requests :"))
    namespace = {}
    variable = {}
    for _ in range(n):
        request = str(input()).strip().split(" ")
        print("Request: {0}".format(request))
        if request.__len__() is not 0:
            if request[0] == "create":
                create(request[2], request[1])
            elif request[0] == "add":
                add(request[1], request[2])
            elif request[0] == "get":
                get(request[1], request[2])
        print("="*40)
        print("namespace : {0}".format(namespace))
        print("variable : {0}".format(variable))
        print("="*40)
