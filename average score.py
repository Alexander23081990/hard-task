from statistics import mean

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
a1_ = mean(grades[0])
a2_ = mean(grades[1])
a3_ = mean(grades[2])
a4_ = mean(grades[3])
a5_ = mean(grades[4])
average = [a1_, a2_, a3_, a4_, a5_]
print(dict(zip(students, average)))
