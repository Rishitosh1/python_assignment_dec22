def sort(s):
    s=sorted(s.split(","))
    s=",".join(s)
    return s

s=input("enter word strings seperated by comma")

print(sort(s))