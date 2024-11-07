#На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #Список
students = {'Johnny','Bilbo','Steve','Kendrick','Aaron'} #Множество
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл.
#Вывод в консоль:
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Kendrick': 3.6666666666666665, 'Steve': 4.8}
students = sorted(students)
name0 = (students[0])
name1 = (students[1])
name2 = (students[2])
name3 = (students[3])
name4 = (students[4])
values0 = sum(grades[0])/len(grades[0])
values1 = sum(grades[1])/len(grades[1])
values2 = sum(grades[2])/len(grades[2])
values3 = sum(grades[3])/len(grades[3])
values4 = sum(grades[4])/len(grades[4])
a_={}
a_.update({name0:values0,name1:values1,name2:values2,name3:values3,name4:values4})
print(a_)