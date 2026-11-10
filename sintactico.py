tokens = [
    10, 1000, 55, 21, 65, 2000,
    12, 70, 2000, 76, 2000, 75, 13, 20
]

print(tokens) '''
constante_dec = "constante" identificador ":" tipo "=" expresion ";"
tipo_arreglo = "arreglo" "[" expresion ".." expresion "]" "de" tipo ";"
tipo = "entero" | "real"
expresion = numero
'''
# constante    10
# arreglo      12
# de           13
# entero       20
# real         21
# :            55
# ;            60
# =            65
# [            70
# ]            75
# ..           76
# VARIABLE     1000
# NUMERO       2000
def constante_dec(token, i):
    if i < len(token) and token[i] == 10:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba constante'
        
    if i < len(token) and token[i] == 1000:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba un identificador'
        
    if i < len(token) and token[i] == 55:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba :'
        
    i, error = tipo(token, i)
    if error != "": return i, error
    
    if i < len(token) and token[i] == 65:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ='
        
    i, error = expresion(token, i)
    if error != "": return i, error
    
    if i < len(token) and token[i] == 60:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ; al final'
    return i, ""

def tipo_arreglo(token, i):
    if i < len(token) and token[i] == 12:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba arreglo'
        
    if i < len(token) and token[i] == 70:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ['
        
    i, error = expresion(token, i)
    if error != "": return i, error
    
    if i < len(token) and token[i] == 76:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ..'
        
    i, error = expresion(token, i)
    if error != "": return i, error
    
    if i < len(token) and token[i] == 75:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ]'
        
    if i < len(token) and token[i] == 13:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba de'
        
    i, error = tipo(token, i)
    if error != "": return i, error
    
    if i < len(token) and token[i] == 60:
        i = i + 1
    else:
        return i, 'ERROR: Se esperaba ; al final'
    return i, ""
