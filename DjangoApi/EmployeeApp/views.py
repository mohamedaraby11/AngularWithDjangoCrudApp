from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments ,Employee
from EmployeeApp.serializers import DepartmentSerializer ,EmployeeSerializer 

from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def DepartmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully !!" , safe = False)
        return JsonResponse("FAiled To Added ", safe=False)
    
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully",safe =False)
        return JsonResponse("FaileTo Update.." , safe =False)
    
    elif request.method=='DELETE' :
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully !!" , safe= False)
    
    
    
    
    


@csrf_exempt
def EmployeeApi(request,id=0):
    if request.method=='GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    
    
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully !!" , safe = False)
        return JsonResponse("FAiled To Added ", safe=False)
    
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully",safe =False)
        return JsonResponse("FaileTo Update.." , safe =False)
    
    elif request.method=='DELETE' :
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully !!" , safe= False)    
    
    

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadFile']
    file_name = default_storage.save(file.name,file)   
    
    return JsonResponse(file_name,safe=False)