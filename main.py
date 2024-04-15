from task1.total_salary import total_salary
from task2.cat_info import cats_info

path1 = "/Users/slavazabolotnyi/PycharmProjects/goit-algo-hw-04/task1/salary.txt"
print(total_salary(path1))


cats = cats_info("/Users/slavazabolotnyi/PycharmProjects/goit-algo-hw-04/task2/cat_info.txt")
for cat in cats:
    print(cat)