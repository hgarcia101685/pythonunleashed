kitchen = True
garage = False
bedroom1 = False
bedroom2 = False
bedroom3 = False
bedroom4 = False
bedroom5 = False
bathroom1 = False
bathroom2 = False
bathroom3 = False
otherroom1 = False
otherroom2 = False
if kitchen:
        print("let the water flow in the kitchen!")
elif garage:
        print("let the water flow in the garage!")
elif bedroom1:
        print("let the water flow in the garage!")
elif bedroom2:
        print("let the water flow in the garage!")
elif bedroom3:
        print("let the water flow in the garage!")
elif bedroom4:
        print("let the water flow in the garage!")
elif bedroom5:
        print("let the water flow in the garage!")
elif bathroom1:
        print("let the water flow in the garage!")
elif bathroom2:
        print("let the water flow in the garage!")
elif bathroom3:
        print("let the water flow in the garage!")
else:
        print("this room has no water")

if kitchen and garage and bathroom1:
    print("Water flowing in kitchen, garage, and bathroom")
else:
    print("water flow if missing in one of these three rooms: kitchen, garage, bathroom")

string = "hello"
num1 = 10
num2 = 20
num3 = 10
if string is "hello":
print("string is hello")
else:
    print("string is not hello")
if num1 is num3:
    print("num1 is the same as num3")
else:
    print("num1 and num3 are different")
if num2 > num3:
    print("num2 is greater than num3")
else:
    print("num2 is not greater than num3")
