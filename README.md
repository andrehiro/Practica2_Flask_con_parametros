# Practica2_Flask_con_parametros
Andre Alexander Hidrogo Rocha 26/10/2023 Codigos en python utilizando flask

### Paso 1
En este paso simplemente creamos la ruta, la funcion y lo que regresa la misma.

### Paso 2
Modificamos la ruta para que contenga "wellcome", esto significa que al usar la liga anterior ya no podemos acceder a la pagina y le tenemos que agregar "wellcome" al final de la URL.

### Paso 3
Modificamos la ruta otra vez pero esta vez le agregamos "/<name>", esto lo que hace es agregar un parametro en este caso string ya que no lo especificamos y usa el que esta por defecto. Ademas se lo agregamos como parametro a la funcion y al return para que lo muestre.

### Paso 4
En este paso se ven 4 tipos de datos que son int,float,path y string. Aqui lo unico que cambia es que si queremos mostrar un int debemos hacerlo un string en el return con la funcion str().

### Paso 5
Utilizamos el formato f, el cual nos sirve para agregar texto estatico a valores variables.

### Paso 6
En la URL ahora ponemos 2 parametros, lo unico diferente a solo tener un parametro es que los separas con un "/" en la URL y con una "," en la funcion.

### Paso 7
En este paso tenemos 4 rutas las cuales tienen diferentes parametros, estas seran utilizadas dependiendo de cuantos valores introduzca el usuario, por ejemplo si solo pone wellcome se mostrara el mensaje "bienvenido" pero si aparte de eso pone un nombre y matricula se mostrarael mensaje "Bienvenido {name} tu numero de control es: {ncontrol}"



