from django.shortcuts import render
from app.models import RegistrationModel 
from app.serializers import Regist_Serializer 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def reg_list(request):
    if request.method=='GET':
        reg_data = RegistrationModel.objects.all() 
        serializer=Regist_Serializer(reg_data,many=True)
        return Response(serializer.data) 
    elif request.method=='POST':
        serializer=Regist_Serializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)


@api_view(['GET', 'PUT','DELETE']) 
def details(request,pk):
    if request.method=='GET': 
        try: 
            reg_data=RegistrationModel.objects.get(pk=pk) 
        except RegistrationModel.DoesNotExist: 
            return Response({'error':'Detail not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = Regist_Serializer(reg_data) 
        return Response(serializer.data) 
    elif request.method=='PUT': 
        reg_data=RegistrationModel.objects.get(pk=pk) 
        serializer = Regist_Serializer(reg_data,data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors) 
    elif request.method=='DELETE': 
        reg_data=RegistrationModel.objects.get(pk=pk) 
        reg_data.delete() 
        return Response({'error':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



    
    
    