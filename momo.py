user_input = input("请输入两个数字，用空格分隔: ")
n, x_input = user_input.split()
n = int(n)
number = list(range(1, n+1))

combined_list = []
for a in number:
    b = list(str(a))
    combined_list.extend(b)
print(combined_list)
x = int(x_input)
x = str(x)
print("x(输入的第二个数字)的出现次数:", combined_list.count(x))