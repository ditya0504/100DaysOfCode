dictt={
     "name":"Vikram",
     "age":22,
     "vehicle":"Ford Endeavour",
     "DOB":"05-04-1999",
    "vehicle":"bike",
    "fruits":["oranges","pineapples","Blueberries"]

 }
print(len(dictt))
print(type(dictt))
x=dictt["vehicle"]
x=dictt.get("vehicle")
print(x)
dictt["color"]="balck"
print(dictt)
dictt.pop("vehicle")
print(dictt)