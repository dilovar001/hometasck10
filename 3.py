str_list=["Emma","Jon","", "Kelly",None,"Erik",""]
for i in str_list:
    if i==None or i=="":
        str_list.remove(i)
print(str_list)        

