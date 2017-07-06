__author__ = 'eugene.riabukha'


def create(key, value):
    pass


def add(key, value):
    pass


def get(key, value):
    pass


if __name__ == "__main":
    n = int(input("Input number of requests :"))
    namespace = {}
    variable = {}
    for _ in range(n):
        request = str(input()).strip().split(" ")
        print("Request: {0}".format(request))
        if request.__len__() is 0:
            if request[0] == "create":
                create(request[1], request[2])
                # if request[2] == "global":
                #     namespace["global"].update({request[1]: dict()})
                # namespace.update()
            elif request[0] == "add":
                pass
            elif request[0] == "get":
                pass

