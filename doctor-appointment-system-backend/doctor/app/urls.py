from django.urls import path
from .views import DoctorView,PatientView,SlotView,AppointmentView,PatientSignUpView,PatientLoginView
urlpatterns = [
    path('doctors/',DoctorView.as_view()),
    path('patient/',PatientView.as_view()),
    path('slot/',SlotView.as_view()),
    path('appointment/',AppointmentView.as_view()),
    path('patient/signup',PatientSignUpView.as_view()),
    path('patient/login',PatientLoginView.as_view())
]