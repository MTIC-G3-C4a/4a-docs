from rest_framework import serializers
from urgenciasApp.models.doctor import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'username', 'cedula', 'password',
                  'correo', 'especialidad', "nombre"]
