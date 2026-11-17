def bucle_for(token, i):
    if i < len(token) and token[i] == 10:
        i += 1
    else:
        return i, 'ERROR: Se esperaba for'
    if i < len(token) and token[i] == 1000:
        i += 1 # target_list
    else:
        return i, 'ERROR: Se esperaba variable'
    if i < len(token) and token[i] == 11:
        i += 1
    else:
        return i, 'ERROR: Se esperaba in'
    if i < len(token) and token[i] == 1000:
        i += 1 # expression_list
    else:
        return i, 'ERROR: Se esperaba expresion'
    if i < len(token) and token[i] == 55:
        i += 1
    else:
        return i, 'ERROR: Se esperaba :'
    if i < len(token) and token[i] != 230: 
        i += 1
    if i < len(token) and token[i] == 230:
        i += 1
        if i < len(token) and token[i] == 55:
            i += 1
        else:
            return i, 'ERROR: Se esperaba : en else'
        i += 1
    return i, ""

Def definicion_funcion(token, i):
    if i < len(token) and token[i] == 15: 
        i += 1
    else: 
        return i, ‘ERROR: Se esperaba def’   
    if i < len(token) and token[i] == 1000:
        i += 1
    else: 
        return i, ‘ERROR: Se esperaba nombre de funcion’
    if i < len(token) and token[i] == 80:
        i += 1 # (
    else: 
        return i, ‘ERROR: Se esperaba (‘
    if i < len(token) and token[i] == 1000:
        i += 1
        while i < len(token) and token[i] == 50:
            i += 1 
            if i < len(token) and token[i] == 1000:
                i += 1
            else: 
                return i, ‘ERROR: Se esperaba parametro’
    if i < len(token) and token[i] == 85:
         i += 1 
    else: 
        return i, ‘ERROR: Se esperaba )’
    if i < len(token) and token[i] == 55: 
        i += 1 
    else: return i, ‘ERROR: Se esperaba :’
    if i < len(token):
        i += 1
    else:
        return i, ‘ERROR: Se esperaba cuerpo de funcion’        
    return i, “”

Def expresion_logica(token, i):
    if i < len(token) and token[i] == 80:
        i += 1
        i, ERROR = termino(token, i)
        if ERROR ¡= “”: 
            return i, ERROR
        while i < len(token) and token[i] in (150, 151): 
            i += 1
            i, ERROR = termino(token, i)
            if ERROR ¡= “”: 
                return i, ERROR
        if i < len(token) and token[i] == 85: i += 1 # )
        else: 
            return i, ‘ERROR: Se esperaba )’
    else:
        i, ERROR = termino(token, i)
        if ERROR ¡= “”: 
            return i, ERROR
    Return i, “”

Def termino(token, i):
    i, ERROR = factor(token, i)
    if ERROR ¡= “”: return i, ERROR
    While i < len(token) and token[i] == 151: # and
        i += 1
        i, ERROR = factor(token, i)
        if ERROR ¡= “”: 
            return i, ERROR
    return i, “”
Def factor(token, i):
    if i < len(token) and token[i] == 152:
        i += 1
        i, ERROR = factor(token, i)
        if ERROR ¡= “”: 
            return i, ERROR
    elif i < len(token) and token[i] == 80: 
        i += 1
        i, ERROR = expresion_logica(token, i)
        if ERROR ¡= “”: 
            return i, ERROR
        if i < len(token) and token[i] == 85:
            i += 1
        else: 
            return i, ‘ERROR: Se esperaba )’
    elif i < len(token) and token[i] in (153, 154, 1000): # True, False, Variable
        i += 1
    else:
        return i, ‘ERROR: Se esperaba factor válido’
    return i, “”
