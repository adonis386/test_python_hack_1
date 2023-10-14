"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    lista2 = []
    index = 0
    
    while index < len(result):
        lista2.append(result[index])
        lista2.append("@")
        index +=1
    
    return lista2