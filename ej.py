from  __future__  import  anotations 
from  abc  import  ABC , abstractmethod class Creator ( ABC ) : """     La clase Creator declara el método de fábrica que se supone que devolverá un     objeto de una clase Product. Las subclases de Creator generalmente proporcionan la     implementación de este método     " . "" @ abstractmethod def factory_method ( self ) : """         Tenga en cuenta que el Creador también puede proporcionar alguna implementación predeterminada del         método de fábrica. 


 
    





    
     
        


        """ 
        pass 

    def  some_operation ( self ) - > str : """         También tenga en cuenta que, a pesar de su nombre, la responsabilidad principal del Creador         no es crear productos. Por lo general, contiene alguna lógica comercial central         que se basa en los objetos Producto, devueltos por el método de fábrica.         Las subclases pueden cambiar indirectamente esa lógica empresarial anulando el         método de fábrica y devolviendo un tipo diferente de producto.         """ # Llamar al método de fábrica para crear un objeto Product. product = self .  
        







        
          

        # Ahora, usa el producto. 
        result  =  f"Creator: El mismo código del creador acaba de funcionar con {product.operation()}" 

        return  result 


""" 
Concrete Creators anula el método de fábrica para cambiar el 
tipo de producto resultante. 
""" 


class  ConcreteCreator1 ( Creator ) : """     Tenga en cuenta que la firma del método todavía utiliza el tipo de producto abstracto,     aunque el método devuelve el producto concreto. De esta     manera, el Creador puede mantenerse independiente de las clases de productos concretos.     """
    

