print(" 1)Добавити")
print(" 2)Мінус")
print(" 3)Помножити")
print(" 4)Поділити")
choose = input('Вибери 1,2,3,4: ')
num_1 = int (input ("Будь-ласка введи перше число: ")) 
num_2 = int (input ("Будь-ласка введи друге число: ")) 
if int(choose) == 1:
    print(str(num_1) + "+" + str(num_2) +"=" + str(num_1 + num_2)  )
elif int(choose) == 2:
    print(str(num_1) + "-" + str(num_2) +"=" + str(num_1 + num_2)  )
elif int(choose) == 3:
    print(str(num_1) + "*" + str(num_2) +"=" + str(num_1 * num_2)  )
elif int(choose) == 4:
    if num_2 == 0:
        print("На нуль ділити не можна")
    else:
        print(str(num_1) + "/" + str(num_2) +"=" + str(num_1 / num_2)  )
    print(str(num_1) + "/" + str(num_2) +"=" + str(num_1 / num_2)  )
 