import copy
old_list=[[1,2],[3,4]]
new_list=copy.copy(old_list)
old_list[0][0]=99
print(new_list[0][0])