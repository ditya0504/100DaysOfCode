num1 = 5
num2 = 6
print(num1)
a = num1 < num2
b = num1 <= num2
c = num1 > num2
d = num1 >= num2
e = num1 != num2

print("a=", a, "b=", b, "c=", c, "d=", d, "e=", e)

temp = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e
    }

for key, value in temp.items():
    if value:
        print(key)
    else:
        print("NOT TRUE", key)
