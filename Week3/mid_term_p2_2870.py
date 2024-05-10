num = int(input())

result_list = []

for i in range(num):
    num_list = list(input().strip()+'a')
    iter_list = []
    for j in num_list:
        
        if 48 <= ord(j) <= 57:
            iter_list.append(str(j))
            
            
        else:
            if len(iter_list) != 0:
                
                if "".join(iter_list).strip("0") == "":
                    
                    result_list.append("0")
                else:

                    result_list.append("".join(iter_list).lstrip("0"))
            iter_list = []

result_int_list = list(map(int, result_list))
result_int_list.sort()
for k in result_int_list:
    print(k)
