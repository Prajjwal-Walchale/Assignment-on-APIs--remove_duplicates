#Sample Input                                                Expected Output
                                                             12345abz@#*
1122334455ababzzz@@@123#*#* 



=====================================================================Program==================================================================



def remove_duplicates(value):
    
    new_string=""
    for i in value:
        if(i in new_string):
            pass
        else:
            new_string+=i
    return new_string
            

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
