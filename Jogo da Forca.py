
palavra= "melancia"
letras_usuario = []
chances = 5
ganhou = False

while True:
        #criar a nossa logica 
        for letra in palavra:
                if letra in letras_usuario:
                        print(letra, end=" ")
                else:
                        print("_", end=" ") 
        print (f"você tem {chances} chances")
        tentativa = input("escolha uma letra para advinhar: ")
        letras_usuario.append(tentativa.lower())
        if tentativa.lower() not in palavra.lower():
               chances -= 1
        
        ganhou = True
        for letra in palavra :
              if letra.lower() not in letras_usuario:
                    ganhou = False
        
        if chances == 0:

         break
   
if ganhou:
        print(f" parabens, voce ganhou. a palavra era:{palavra}") 
    
else:
        print (f" voce perdeu! A palavra era {palavra}") 



