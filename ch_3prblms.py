a=input("enter yo name:")
print(f"good afternoon {a}")  #fstring

#find double space
a=input("enter a string:")
print("double space is at index",a.find("  "))

a="im   going  out today"
print(a.find("  "))

#replace double space with single space
a="im  going  out today"
print(a.replace("  "," "))