result = 10 + 15
text_result = "1) Результат = " + str(result)
print(text_result)

result2 = "10" + "15"
text_result2 = "2) Результат = " + result2
print(text_result2)

print(' 1) Hello \n 2) World \n 3) Bye')
choose = input('Choice: ')
if int(choose) == 1:
    print("HELLO")
elif int(choose) == 2 :
    print("WORLD")
elif int(choose) == 3 :
    print("BYE")
    