num = int(input())
result_list = []
for i in range(num):
    inputs = int(input())
    if inputs == 0:
        result_list.pop()
    else:
        result_list.append(inputs)

print(sum(result_list))
