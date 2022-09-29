from django.views import View
from django.utils.decorators import method_decorator
from .models import Departamento
from .models import Empleado
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.

# Vistas basadas en una clase

class CompaniaView(View):

    # metodo para evitar el error en get de la cookie CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Peticion en GET
    def get(self, request, id=0):
        if (id > 0):
            empleados = list(Empleado.objects.filter(id=id).values())
            if len(empleados) > 0:
                unicoreg = empleados[0]
                datos = {'message': "Consulta Realizada con Exito!", 'empleado': unicoreg}
            else:
                datos = {'message': "Empleados no encontrados"}
            return JsonResponse(datos)
        else:
            empleados = list(Empleado.objects.values())
            if len(empleados) > 0:
                #unicoEmpleado = empleados[0]
                datos = {'message': "Consulta Realizada con Exito!", 'empleado': empleados}
            else:
                datos = {'message': "Empleados no encontrados"}
            return JsonResponse(datos)

        #Codigo para devolver el valor get de la tabla departamentos
        #departamentos = list(Departamento.objects.values())
        #if len(departamentos) > 0:
            # unicoEmpleado = empleados[0]
        #    datos = {'message': "Exito!", 'departamento': departamentos}
        #else:
        #    datos = {'message': "Departamentos no encontrados"}
        #return JsonResponse(datos)

    # Peticion en POST
    def post(self, request):
        # print(request.body)
        jsonData = json.loads(request.body)
        # print(jsonData)
        Empleado.objects.create(codigo=jsonData['codigo'], nif=jsonData['nif'],nombre=jsonData['nombre'],
                                apellido1=jsonData['apellido1'],apellido2=jsonData['apellido2'],
                                codigoDepartamento_id=jsonData['codigoDepartamento_id'])
        datos = {'message': "Consulta Realizada con Exito!"}
        return JsonResponse(datos)

        # Peticion en PUT
    def put(self, request, id):
        jsonData = json.loads(request.body)
        empleados = list(Empleado.objects.filter(id=id).values())
        if len(empleados) > 0:
            unicoReg = Empleado.objects.get(id=id)
            unicoReg.codigo = jsonData['codigo']
            unicoReg.nif = jsonData['nif']
            unicoReg.nombre = jsonData['nombre']
            unicoReg.apellido1 = jsonData['apellido1']
            unicoReg.apellido2 = jsonData['apellido2']
            unicoReg.codigoDepartamento_id = jsonData['codigoDepartamento_id']
            unicoReg.save()
            datos = {'message': "Consulta Realizada con Exito!"}
        else:
            datos = {'message': "Empleados no encontrados"}
        return JsonResponse(datos)


    def delete(self, request, id):
        empresas = list(Empleado.objects.filter(id=id).values())
        if len(empresas) > 0:
            Empleado.objects.filter(id=id).delete()
            datos={'message': "Consulta Realizada con Exito!"}
        else:
            datos = {'message': "Empleados no encontrados"}
        return JsonResponse(datos)

