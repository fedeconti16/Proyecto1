from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Djangooooo")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola mundo!</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Leo" 
    apellido = "Messi"

    namelist = ["Gabriel", "Jimena", "Nacho", "Patricia", "Natalia"]
    
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    #miHtml = open("C:/Users/Federico/Documents/Python Scripts/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHtml.read())
    #miHtml.close()
    #miContext = Context(diccionario)
    #documento = plantilla.render(miContext)
    #todo lo comentado es el metodo para meter la ruta directamente ahi en el open
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

