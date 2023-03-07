

def decorator_imprimir(func):
    
    
    def imprima(*args, **kwargs):
        
        capital, taxa, tempo = args        
       
        funcao = func(*args, **kwargs)
        
        
        print(capital, taxa, tempo, funcao)
        
      
        return funcao
    return imprima

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo