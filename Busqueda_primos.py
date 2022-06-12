def es_primo(numero):
    contador=1
    if numero == 1:
        return False
    for i in range(1, numero):
        contador = i*contador
    contador = contador+1
    
    if contador % numero == 0:
        return True
    else:
         return False
 
def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')    
    
if __name__ == '__main__':
    run()