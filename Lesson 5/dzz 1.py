def tru(a,b,c):
    return (a + b + c) / 3
result = tru(int(input("Enter number: ")),int(input("Enter number: ")),int(input("Enter number: ")))
print(result)
#
def mon(a):
    if a == 1:
        return "Січень"
    elif a == 2:
        return "Лютий"
    elif a == 3:
        return "Березень"
    elif a == 4:
        return "Квітень"
    elif a == 5:
        return "Травень"
    elif a == 6:
        return "Червень"
    elif a == 7:
        return "Липень"
    elif a == 8:
        return "Серпень"
    elif a == 9:
        return "Вересень"
    elif a == 10:
        return "Жовтень"
    elif a == 11:
        return "Листопад"
    elif a == 12:
        return "Грудень"
result = mon(int(input("Enter number from 1 to 12: ")))
print(result)
#1
def max(a,b):
    if a == b:
        return("Число a дорівнює числу b")
    if a > b:
        return("Число a більше за число b")
    else:
        return("Число b більше за число a")    
result = max(int(input("Enter number a: ")),int(input("Enter number b: ")))
print(result)
#
def length(a):
    return len(a)
result = length(str(input("Enter sentence: ")))
print(result)


    


