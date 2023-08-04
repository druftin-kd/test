from rest_framework import serializers
from .models import *

class Windows10HomeActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows10HomeActivationRequest
        fields = ['serial_key', 'activation_key']
        
class Windows10HomeOEMActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows10HomeOEMActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows10ProActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows10ProActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows10ProOEMActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows10ProOEMActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows11HomeActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows11HomeActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows11HomeOEMActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows11HomeOEMActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows11ProActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows11ProActivationRequest
        fields = ['serial_key', 'activation_key']

class Windows11ProOEMActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows11ProOEMActivationRequest
        fields = ['serial_key', 'activation_key']




class Office2019ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2019ActivationRequest
        fields = ['serial_key', 'activation_key']

class Office2019BindActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2019BindActivationRequest
        fields = ['serial_key', 'activation_key']

class Office2021ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2021ActivationRequest
        fields = ['serial_key', 'activation_key']

class Office2021BindActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2021BindActivationRequest
        fields = ['serial_key', 'activation_key']

class Office2021MacBindActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2021MacBindActivationRequest
        fields = ['serial_key', 'activation_key']

class OfficeHomeBusinessWinActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHomeBusinessWinActivationRequest
        fields = ['serial_key', 'activation_key']

class OfficeHomeBusinessMacActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHomeBusinessMacActivationRequest
        fields = ['serial_key', 'activation_key']

class OfficeHomeStudentWinActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHomeStudentWinActivationRequest
        fields = ['serial_key', 'activation_key']

class OfficeHomeStudentMacActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHomeStudentMacActivationRequest
        fields = ['serial_key', 'activation_key']

class Office2021HomeBasicActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office2021HomeBasicActivationRequest
        fields = ['serial_key', 'activation_key']




class ProjectProfessional2019ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProfessional2019ActivationRequest
        fields = ['serial_key', 'activation_key']

class ProjectProfessional2021ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProfessional2021ActivationRequest
        fields = ['serial_key', 'activation_key']




class VisioProfessional2019ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisioProfessional2019ActivationRequest
        fields = ['serial_key', 'activation_key']

class VisioProfessional2021ActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisioProfessional2021ActivationRequest
        fields = ['serial_key', 'activation_key']




class WindowsServer2016EssentialActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsServer2016EssentialActivationRequest
        fields = ['serial_key', 'activation_key']

class WindowsServer2019StandardActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsServer2019StandardActivationRequest
        fields = ['serial_key', 'activation_key']

class WindowsServer2019DatacenterActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsServer2019DatacenterActivationRequest
        fields = ['serial_key', 'activation_key']

class WindowsServer2022DatacenterActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsServer2022DatacenterActivationRequest
        fields = ['serial_key', 'activation_key']




class MicrosoftSQLServer2019StandardActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicrosoftSQLServer2019StandardActivationRequest
        fields = ['serial_key', 'activation_key']

class MicrosoftSQLServer2019EnterpriseActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicrosoftSQLServer2019EnterpriseActivationRequest
        fields = ['serial_key', 'activation_key']

class MicrosoftSQLServer2022StandardActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicrosoftSQLServer2022StandardActivationRequest
        fields = ['serial_key', 'activation_key']

class MicrosoftSQLServer2022EnterpriseActivationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicrosoftSQLServer2022EnterpriseActivationRequest
        fields = ['serial_key', 'activation_key']



class ActivationKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivationKeys
        fields = ['activation_key', 'category', 'expiry_date']
