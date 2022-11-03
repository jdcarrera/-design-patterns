# Design Patterns:

# Singleton:
El patron de diseño Singleton (instancia única) está diseñado para restringir la creación de
objetos pertenecientes a una clase o el valor de un tipo a un único objeto.
Su intención consiste en garantizar que una clase solo tenga una instancia y proporcionar un punto de acceso global a ella.

# Factory:
Sirve para crear objetos sin tener que especificar su clase precisa.
Esto quiere decir que el objeto creado puede intercambiarse con flexibilidad y facilidad.
El objeto real creados es enmascarado detrás de una interface comun entre todos los objetos que pueden ser creado, 
con la finalidad de que estos pueden variar sin afectar la forma en que el cliente interactua con ellos. 

# Abstract factory:
Permite crear y producir familias de objetos relacionados sin necesidad de especificar sus clases concretas

# Prototype:
Permite la clonacion de objetos los cuales estan creados mediante un pool de prototipos
Este patrón es especialmente util cuando necesitamos crear objetos basados en otros ya existentes o cuando se necesita la creación de estructuras de objetos muy grandes, este patrón nos ayuda también a ocultar la estrategia utilizada para clonar un objeto.

# Facade:
El objeto real creados es enmascarado detras de una interface comun entre todos los objetos que pueden ser creado, con la finalidad de que estos pueden variar sin afectar la forma en que el cliente interactua con ellos.

# Decorator:
Permite estructurar la logica de negocio en capas, 
crear un decorador para cada capa y componer objetos con varias combinaciones de esta logica, durante el tiempo de ejecucion. El codigo cliente puede tratar a todos estos objetos de la misma forma, ya que todos siguen una interfaz comun.

# Proxy:
Nos permite realizar ciertas acciones antes y despues de realizar la accion deseada por el usuario.

# Command:
Funciona para convertir una solicitud en un objeto independiente que contiene toda la informacion sobre la solicitud. Esta transformacion te permite parametrizar los metodos con diferentes solicitudes, retrasar o 
poner en cola la ejecucion de una solicitud y soportar operaciones que no se pueden realizar.

# Memento:
Este patron captura el estado de un objeto en un momento determinado con la finalidad de retornar ese estado en cualquier momento.
es utilizado cuando tenemos objetos que cambian en el tiempo y por alguna razon necesitamos restaurar su estado en un momento determinado.

# Observer:
El patron Observer se basa en la idea de centralizar la tarea de informar en manos del sujeto.
Para conseguirlo, existe una lista en la que los observadores pueden registrarse. En caso de modificacion, el sujeto los informa uno tras otro, sin necesidad de que los observadores lo pidan activamente.

# Strategy:
permite establecer en tiempo de ejecucion el rol de comportamiento de una clase.
Stratagy se basa en el polimorfismo para implementar una serie de comportamientos que podrán ser intercambiados durante la ejecución del programa,
logrando con esto que un objeto se pueda comportar de forma distinta segun la estrategia establecida.

# Data Acces Object:
Independiza la aplicacion de la forma de acceder a la base de datos, o cualquier otro tipo de repositorio de datos.
es un componente de software que suministra una interfaz comun entre la aplicacion y uno o mas dispositivos de almacenamiento de datos, 
tales como una Base de datos o un archivo.

# Dependency Injection:
Tambien conocido como el patron del contenedor, tiene la funcion de proporcionar los objetosw necesarios para la creacion o elaboracion de un objeto mas complejo.

# Model View Controller:
Es una herramienta compuesta de modelo-vista-controlador, que permite la separacion adecuada de cada uno de los componentes en objetos,
y evita que estos se junten, por lo que no pueden estar dentro de una misma clase.
En pocas palabras, funciona para clasificar, la logica del sistema y la interfaz que el usuario ve.
