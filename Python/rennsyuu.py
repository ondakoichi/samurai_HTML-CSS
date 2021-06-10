even_num = []
odd_num = []

def sort_number(num):
    if num % 2 == 0:
        even_num.append(num)
        
    else:
       odd_num.append(num)
    
sort_number(5)
print(even_num)
print(odd_num)