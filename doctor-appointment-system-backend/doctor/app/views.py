from sys import api_version
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .service import GetDoctors,CreateDoctors,CreatePatient,CreateSlot\
    ,GetSlot,CreateAppointment\
    ,GetAppointment, PatientLogin
# Create your views here.
from rest_framework import serializers

class DoctorSerializers(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        speciality = serializers.CharField(max_length=50)

class DoctorView(APIView):
    def get(self,request):
        doctors = GetDoctors()
        serializer = DoctorSerializers(doctors,many=True)
        return Response(serializer.data)
        # return Response(data)
    
    def post(self,request):
        serializer = DoctorSerializers(request.data)
        data = serializer.data
        CreateDoctors(data)
        return Response({'msg':'Doctor Created'})

class PatientView(APIView):
    # def get(self,request):
    #     data = GetPatient()
    #     return Response(data)

    def post(self,request):
        CreatePatient(request.data)
        return Response({'msg':"patient created"})

class SlotSerializers(serializers.Serializer):
    doctor_id=serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

class OutputSlotSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    doctor_id=serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    available = serializers.BooleanField()

class SlotView(APIView):
    def get(self,request):
        slots = GetSlot()
        serializer = OutputSlotSerializers(slots,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SlotSerializers(request.data)
        data = serializer.data
        data = CreateSlot(data)
        return Response(data)
        # return Response({"msg":"slot created"})


class AppointmentSeralizer(serializers.Serializer):
    slot_id=serializers.IntegerField()


class AppointmentView1(APIView):
    def get(self,request):
        appointments = GetAppointment(request.data)
        serializer = AppointmentSeralizer(appointments,many=True)
        return Response(serializer.data)

class AppointmentView(APIView):
    def get(self,request):
        slots = GetSlot()
        serializer = OutputSlotSerializers(slots,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializers=AppointmentSeralizer(request.data)
        data=serializers.data
        data = CreateAppointment(request,data)

        return Response(data)

class CreatePatientSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    
class PatientSignUpView(APIView):
    def post(self,request):
        serializer = CreatePatientSerializer(request.data)
        msg,new_patient = CreatePatient(
                                        serializer["username"].value,
                                        serializer["email"].value,
                                        serializer["password"].value
        )
        return Response(msg)

class PatientLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class PatientLoginView(APIView):
    def post(self, request):
        serializer = PatientLoginSerializer(request.data)
        username = serializer['username'].value
        password = serializer['password'].value
        msg = PatientLogin(request,username,password)
        return Response(msg)