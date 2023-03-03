from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
# Create your views here.
def index(request):
    return render(request, 'index.html')



class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)


@csrf_exempt
def suma(request):
    #NECESARIO PARA LOS JSON / CODIFICACIÓN DEL BODY
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)

    #Asignandole las instanceasiones de las clases fracciones con POST del usuario
    Fraccion1st = Fraccion(body['numerador1'],body['denominador1'])
    Fraccion2nd = Fraccion(body['numerador2'],body['denominador2'])

    num_resultado = Fraccion1st.num + Fraccion2nd.num
    den_resultado = Fraccion1st.den

    #Logica para la suma SÍ Y SOLO SÍ los denominadores no son iguales
    if Fraccion1st.den != Fraccion2nd.den:
        DummyNumerador1 = Fraccion1st.num * Fraccion2nd.den
        DummyDenominator = Fraccion1st.den * Fraccion2nd.den
        DummyNumerador2 = Fraccion2nd.num * Fraccion1st.den
        num_resultado = DummyNumerador1 + DummyNumerador2
        den_resultado = DummyDenominator

    #simple simplificacion de fracciones
    if num_resultado == den_resultado: num_resultado,den_resultado = 1,1
    if num_resultado == den_resultado/2: num_resultado,den_resultado = 1,2


    #regresar el resultado.
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")


@csrf_exempt
def multiplicacion(request):
    #NECESARIO PARA LOS JSON / CODIFICACIÓN DEL BODY
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    #Asignandole las instanceasiones de las clases fracciones con POST del usuario
    Fraccion1st = Fraccion(body['numerador1'],body['denominador1'])
    Fraccion2nd = Fraccion(body['numerador2'],body['denominador2'])

    num_resultado = Fraccion1st.num * Fraccion2nd.num 
    den_resultado = Fraccion1st.den * Fraccion2nd.den

    if num_resultado == den_resultado: num_resultado,den_resultado = 1,1
    if num_resultado == den_resultado/2: num_resultado,den_resultado = 1,2



    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")



@csrf_exempt
def resta(request):
    #NECESARIO PARA LOS JSON / CODIFICACIÓN DEL BODY
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    #Asignandole las instanceasiones de las clases fracciones con POST del usuario
    Fraccion1st = Fraccion(body['numerador1'],body['denominador1'])
    Fraccion2nd = Fraccion(body['numerador2'],body['denominador2'])

    num_resultado = Fraccion1st.num - Fraccion2nd.num
    den_resultado = Fraccion1st.den 
    if Fraccion1st.den != Fraccion2nd.den:
        DummyNumerador1 = Fraccion1st.num * Fraccion2nd.den
        DummyDenominator = Fraccion1st.den * Fraccion2nd.den
        DummyNumerador2 = Fraccion2nd.num * Fraccion1st.den
        num_resultado = DummyNumerador1 - DummyNumerador2
        den_resultado = DummyDenominator

    if num_resultado == den_resultado: num_resultado,den_resultado = 1,1
    if num_resultado == den_resultado/2: num_resultado,den_resultado = 1,2



    resultado = Fraccion(num_resultado,den_resultado)
    if Fraccion1st == 0 or Fraccion2nd ==0: return HttpResponse("No es posible!")
    return HttpResponse(resultado.toJSON(), content_type = "text/json-comment-filtered")



@csrf_exempt
def division(request):
    #NECESARIO PARA LOS JSON / CODIFICACIÓN DEL BODY
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    #Asignandole las instanceasiones de las clases fracciones con POST del usuario
    Fraccion1st = Fraccion(body['numerador1'],body['denominador1'])
    Fraccion2nd = Fraccion(body['numerador2'],body['denominador2'])

    num_resultado = Fraccion1st.num / Fraccion2nd.num
    den_resultado = Fraccion1st.den / Fraccion2nd.den

    if num_resultado == den_resultado: num_resultado,den_resultado = 1,1
    if num_resultado == den_resultado/2: num_resultado,den_resultado = 1,2


    resultado = Fraccion(num_resultado,den_resultado)
    return HttpResponse(resultado.toJSON(), content_type = "text/json-comment-filtered")








def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    if nombre == 'BIENVENIDA': return bienvenida(request)
    if nombre == 'MULTIPLICACION': return multiplicacion(request)
    return HttpResponse(f"Hola, como estás {nombre} ?")


def bienvenida(request):
    return HttpResponse(f"hola bienvenido")
