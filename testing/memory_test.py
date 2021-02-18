a = {"test1": "test", "test2": "test"}
b = {**a}

print(hex(id(a)))
print(hex(id(b)))

b["test3"] = "test"

print(a)
print(b)
