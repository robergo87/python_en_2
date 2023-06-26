def print2(*params, **named_params):
    for index, param in enumerate(params):
        print(index, ":", param)
    for k, v in named_params.items():
        print(k, ":", v)

print2("a", "b", "c", "d", "f", "h", manufacturer="ferrari")
