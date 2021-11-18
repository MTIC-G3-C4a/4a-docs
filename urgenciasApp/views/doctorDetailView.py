from rest_framework import generics
from urgenciasApp.models.doctor import Doctor
from urgenciasApp.serializers.doctorSerializer import DoctorSerializer

class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
