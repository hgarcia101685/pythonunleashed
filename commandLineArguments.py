import sys

print("Command line arguments have been passed: ")
i = 0
for arg in sys.argv:
    if i == 0:
        print("This one doesn't count " + str(sys.argv[i]))
    else:
        print(sys.argv[i])
    i += 1
