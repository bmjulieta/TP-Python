from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Categoria, Blog, ServicioB, AboutUs
from  .forms import ContactoForm, ServicioForm
# Create your views here.

    
def inicio(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    blogs= Blog.objects.all()
    data={
        'productos':productos,
        'categorias':categorias,
        'blogs':blogs,
        'contactanos': contactanos,
        'blog':blog,
        'about_us':about_us,
        'NuestrosTalentos': nt,
        'servicios':servicios,
        'shop': shop,
        
    }

    return render(request,"./paginas/index.html", data)
def login(request):
    return render(request,"./paginas/login-register.html")

def create(request):
    data={
        'form': ServicioForm()
    }
    if request.method=='POST':
        
        servicio = ServicioForm(data=request.POST, files=request.FILES)
        if servicio.is_valid():
            servicio.save()
            data['mensaje']='¡Tu servicio ha sido agregado correctamente!'
        else:
            data['form'] = servicio     

    return render(request,"./servicios/crear.html", data)

def edit(request, id):
    servicioB = get_object_or_404(ServicioB, id=id)
    data={
        'form': ServicioForm(instance=servicioB)
    }
    if request.method=='POST':
        
        servicio = ServicioForm(data=request.POST, files=request.FILES, instance=servicioB)
        if servicio.is_valid():
            servicio.save()
            return redirect(to='/servicios/')
        else:
            data['form'] = servicio  
    return render(request,"./servicios/editar.html", data)

def delete(request, id):
    servicioB = get_object_or_404(ServicioB, id=id)
    servicioB.delete()
    data={
        'form': ServicioForm(instance=servicioB)
    }
    
    return redirect('/servicios/')

def contactanos(request):
    data={
        'form': ContactoForm()
    }
    # Si el form tiene información, podemos llenar un formulario para ver desde el admin 
    if request.method=='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Su consulta ha sido realizada satisfactoriamente ¡Muchas gracias!'
        else:
            data['form'] = formulario     

    return render(request,"./paginas/contactanos.html", data)

def blog(request):
    blogs= Blog.objects.all()
    data={
        'blogs':blogs,
    }
    return render(request,"./paginas/blog.html", data)

def about_us(request):
    aboutUs= AboutUs.objects.all()
    data={
        'aboutus':aboutUs,
    }
    return render(request,"./servicios/about_us.html", data)

def nt(request):
    return render(request,"./paginas/nt.html")

def servicios(request):
    serviciosB= ServicioB.objects.all()
    data={
        'serviciosB':serviciosB
        }

    
    return render(request,"./paginas/servicios.html", data)

def shop (request):
    return render(request,"./paginas/shop.html")

def regi(request):

    return render(request,"./paginas/regi.html")

def regi(request):

    return render(request,"./paginas/regi.html")