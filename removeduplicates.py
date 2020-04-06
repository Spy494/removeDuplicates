def removeDuplicates(a_list): 
    final_list = [] 
    for num in a_list: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
a_list = [30, 28, 28, 16, 14, 14, 12, 10]
a_list.sort()
print(removeDuplicates(a_list)) 