name = input("What's your name? ").upper()
for i in name:
    if i not in "AEOUI":
        print(i, end = "")
