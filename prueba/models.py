from django.db import models
from uuid import uuid4
from decimal import Decimal

class Categoria(models.Model):
    idCat = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    clase_css = models.CharField(max_length=50, blank=True, null=True)
    

class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)

class MetodoDePago(models.Model):
    idPago = models.IntegerField(primary_key=True)
    tipoMetPag = models.CharField(max_length=100, default=' ')
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, default=1)

class MetodoDeCobro(models.Model):
    idMetod = models.IntegerField(primary_key=True)
    tipoMet = models.CharField(max_length=100, default=1) 
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, default=1)




class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=70, default='default_value')
    desc=models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_precio_con_descuento(self):
        descuento = (self.desc / Decimal('100')) * self.precio
        precio_con_descuento = self.precio - descuento
        precio_con_descuento = precio_con_descuento.quantize(Decimal('0.00'))
        return precio_con_descuento

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}"
    
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion = models.TextField(max_length=299)
    icono_1 = models.CharField(max_length=50, default='fa-solid fa-star')
    icono_2 = models.CharField(max_length=50, default='fa-solid fa-heart')
    icono_3 = models.CharField(max_length=50, default='fa-solid fa-star')
    icono_4 = models.CharField(max_length=50, default='fa-solid fa-heart')
    icono_5 = models.CharField(max_length=50, default='fa-solid fa-circle')



class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idMetodoDePago = models.ForeignKey(MetodoDePago, on_delete=models.CASCADE)
    idMetodoDeCobro = models.ForeignKey(MetodoDeCobro, on_delete=models.CASCADE)

class Blog(models.Model):
    titulo=models.CharField(max_length=100)
    fecha=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
opciones_consultas=[
    [0, 'Consulta'],
    [1, 'Reclamo'],
    [2, 'Sugerencia']
]
class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

categoria=[
    [900, 'Diseño Web'],
    [901, 'Front End'], 
    [902, 'Back End'],
    [903, 'Logo & Marca'], 
    [904, 'Diseño de Apps'], 
    [905, 'Arte'], 
    [906, 'Ilustraciones'],
    [907, 'Diseño UX'],
    [908, 'Gaming' ],
    [909, 'Diseño 3D'],
    [910, 'Marketing Digital'], 
    [911, 'Soporte'], 
    [912, 'Programacion y Tecnologia'], 
    [913, 'Datos'],
    [914, 'Fotografia y Edicion' ],
    [915, 'Videos y Edición'] 

]
class ServicioB(models.Model):
    servicio = models.CharField(max_length=80, null=True)
    precio = models.IntegerField()
    categoria=models.IntegerField(choices=categoria)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion= models.TextField(max_length=300)

class AboutUs(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    imagen = models.ImageField(upload_to='imagenes/aboutus/', null=True, blank=True)
    rol = models.CharField(max_length=80, null=True)
    linkedIng = models.CharField(max_length=90, null=True)