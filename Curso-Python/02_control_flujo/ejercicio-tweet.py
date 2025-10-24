tweet = input("Ingrese su tweet: ")
if not tweet:    
    print("No se puede publicar un tweet vacío.")
elif len(tweet) > 20:    
    print("Ha sobrepasado el límite de su publicación.")
else:    
    print("Su tweet ha sido publicado.")