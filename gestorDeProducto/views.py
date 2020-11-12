from django.shortcuts import render

# Create your views here.
def plantilla(request):
    return render(request, 'plantillabase.html' , {})

def login(request):
    return render(request, 'login.html' , {})

def registro(request):
    mensaje=""
    if request.method == "POST":
        usuario                 = request.POST["txtUsuario"]
        nombre                   = request.POST["txtNombre"]
        apellido               = request.POST["txtApellido"]
        correo                   = request.POST["txtCorreo"]
        clave                     = request.POST["txtClave"]
        confirmarclave   = request.POST["txtConfirmarclave"]