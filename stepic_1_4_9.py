n = int(input("Input number of requests :"))
namespace = {"global": None}
var = {"global": []}
for _ in range(n):
    request = str(input()).strip().split(" ")
    if request[0] == "create":
        namespace[request[1]] = request[2]
        var[request[1]] = []
    elif request[0] == "add":
        if request[1] in var:
            var[request[1]].append(request[2])
    elif request[0] == "get":
        f = request[1]
        while True:
            if f not in namespace:
                f = None
            if f is None or request[2] in var[f]:
                print(f)
                break
            else:
                f = namespace[f]
