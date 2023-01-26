def reverse(str):  
    if len(str) == 0: # Checking the lenght of string 
        return str  
    else:  
        return reverse(str[1:]) + str[0]  
   
str = "95675"  
print ("Исходная строка: ", str)    
print ("Перевернутая строка: ", reverse(str))
