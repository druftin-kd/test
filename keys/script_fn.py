import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import json
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

url_for_sending_sms = "https://sms.aakashsms.com/sms/v3/send"
auth_token = "794f18bc9e08b68c957b0c4437a0fb64464067b8524a436a362d33aec943f8a3"

def send_sms_via_api(text, to):
        
    data = {"auth_token": auth_token, "to": to, "text": text}

    try:
        response = requests.post(url_for_sending_sms, data=data)
        response = requests.Response()
        response.status_code = 200
        response._content = json.dumps(
            {"error": False, "message": "Mock SMS sent."}
        ).encode("utf-8")
        print("sms sent ", text)
    except requests.exceptions.RequestException as e:
        print("sms not sent ")
        return (False, str(e))
 

def contact_mail(sender, name, msz):
    message = MIMEMultipart()
    message["To"] = "originalsoftwareproduct@gmail.com"
    message["From"] = sender
    message["Subject"] = f'Contact from {name}'

    message_body = f'{msz}\n\nfrom:\n{name}\n{sender}'
    messageText = MIMEText(message_body, 'plain')
    message.attach(messageText)

    email = 'contactme.osp@gmail.com'
    password = 'qsxakbuqpmndbpsc'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email,password)
    fromaddr = 'contactme.osp@gmail.com'
    toaddrs  = 'originalsoftwareproduct@gmail.com'
    server.sendmail(fromaddr,toaddrs,message.as_string())
    server.quit()

def check_windows(serial_key):
    try:
        activation_request =Windows10HomeActivationRequest.objects.get(serial_key=serial_key)
        category="Windows 10 Home"
    except:
        try:
            activation_request=Windows10HomeOEMActivationRequest.objects.get(serial_key=serial_key)
            category="Windows 10 Home OEM"
        except:
            try:
                activation_request=Windows10ProActivationRequest.objects.get(serial_key=serial_key)
                category="Windows 10 Pro"
            except:
                try:
                    activation_request=Windows10ProOEMActivationRequest.objects.get(serial_key=serial_key)
                    category="Windows 10 Pro OEM"
                except:
                    try:
                        activation_request=Windows11HomeActivationRequest.objects.get(serial_key=serial_key)
                        category="Windows 11 Home"
                    except:
                        try:
                            activation_request=Windows11HomeOEMActivationRequest.objects.get(serial_key=serial_key)
                            category="Windows 11 Home OEM"
                        except:
                            try:
                                activation_request=Windows11ProActivationRequest.objects.get(serial_key=serial_key)
                                category="Windows 11 Pro"
                            except:
                                try:
                                    activation_request=Windows11ProOEMActivationRequest.objects.get(serial_key=serial_key)
                                    category="Windows 11 Pro OEM"
                                except:
                                    activation_request=None
                                    category="Office"
    return activation_request, category

def check_office(serial_key):
    try:
        activation_request=Office2019ActivationRequest.objects.get(serial_key=serial_key)
        category="Office 2019"
    except:
        try:
            activation_request=Office2019BindActivationRequest.objects.get(serial_key=serial_key)
            category="Office 2019 Bind"
        except:
            try:
                activation_request=Office2021ActivationRequest.objects.get(serial_key=serial_key)
                category="Office 2021"
            except:
                try:
                    activation_request=Office2021BindActivationRequest.objects.get(serial_key=serial_key)
                    category="Office 2021 Bind"
                except:
                    try:
                        activation_request=Office2021MacBindActivationRequest.objects.get(serial_key=serial_key)
                        category="Office 2021 Mac Bind"
                    except:
                        try:
                            activation_request=OfficeHomeBusinessWinActivationRequest.objects.get(serial_key=serial_key)
                            category="Office Home Business Windows"
                        except:
                            try:
                                activation_request=OfficeHomeBusinessMacActivationRequest.objects.get(serial_key=serial_key)
                                category="Office Home Business Mac"
                            except:
                                try:
                                    activation_request=OfficeHomeStudentWinActivationRequest.objects.get(serial_key=serial_key)
                                    category="Office Home Student Windows"
                                except:
                                    try:
                                        activation_request=OfficeHomeStudentMacActivationRequest.objects.get(serial_key=serial_key)
                                        category="Office Home Student Mac"
                                    except:
                                        try:
                                            activation_request=Office2021HomeBasicActivationRequest.objects.get(serial_key=serial_key)
                                            category="Office 2021 Home Basic"
                                        except:
                                            activation_request=None
                                            category="Professional"
    return activation_request, category

def check_professional(serial_key):
    try:
        activation_request=ProjectProfessional2019ActivationRequest.objects.get(serial_key=serial_key)
        category="Project Professional 2019"
    except:
        try:
            activation_request=ProjectProfessional2021ActivationRequest.objects.get(serial_key=serial_key)
            category="Project Professional 2021"
        except:
            try:
                activation_request=VisioProfessional2019ActivationRequest.objects.get(serial_key=serial_key)
                category="Visio Professional 2019"
            except:
                try:
                    activation_request=VisioProfessional2021ActivationRequest.objects.get(serial_key=serial_key)
                    category="Visio Professional 2021"
                except:
                    activation_request=None
                    category="Server" 
    return activation_request, category

def check_server(serial_key):
    try:
        activation_request=WindowsServer2016EssentialActivationRequest.objects.get(serial_key=serial_key)
        category="Windows Server 2016 Essential"
    except:
        try:
            activation_request=WindowsServer2019StandardActivationRequest.objects.get(serial_key=serial_key)
            category="Windows Server 2019 Standard"
        except:
            try:
                activation_request=WindowsServer2019DatacenterActivationRequest.objects.get(serial_key=serial_key)
                category="Windows Server 2019 Datacenter"
            except:
                try:
                    activation_request=WindowsServer2022DatacenterActivationRequest.objects.get(serial_key=serial_key)
                    category="Windows Server 2022 Datacenter"
                except:
                    category="SQL"
                    activation_request=None  
    return activation_request, category

def check_sql(serial_key):
    try:
        activation_request=MicrosoftSQLServer2019StandardActivationRequest.objects.get(serial_key=serial_key)
        category="Microsoft SQL Server 2019 Standard"
    except:
        try:
            activation_request=MicrosoftSQLServer2019EnterpriseActivationRequest.objects.get(serial_key=serial_key)
            category="Microsoft SQL Server 2019 Enterprise"
        except:
            try:
                activation_request=MicrosoftSQLServer2022StandardActivationRequest.objects.get(serial_key=serial_key)
                category="Microsoft SQL Server 2022 Standard"
            except:
                try:
                    activation_request=MicrosoftSQLServer2022EnterpriseActivationRequest.objects.get(serial_key=serial_key)
                    category="Microsoft SQL Server 2022 Enterprise"
                except:
                    return Response({'error': 'Incorrect serial key.'}, status=status.HTTP_404_NOT_FOUND)
    return activation_request, category

def update_serializer(activation_request, data, category):
    if category=="Windows 10 Home":
        serializer=Windows10HomeActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 10 Home OEM":
        serializer=Windows10HomeOEMActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 10 Pro":     
        serializer=Windows10ProActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 10 Pro OEM":
        serializer=Windows10ProOEMActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 11 Home":
        serializer=Windows11HomeActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 11 Home OEM":
        serializer=Windows11HomeOEMActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 11 Pro":
        serializer=Windows11ProActivationRequestSerializer(activation_request, data=data)

    elif category=="Windows 11 Pro OEM":
        serializer=Windows11ProOEMActivationRequestSerializer(activation_request, data=data)



                        
    elif category=="Office 2019":
        serializer=Office2019ActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office 2019 Bind":
        serializer=Office2019BindActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office 2021":
        serializer=Office2021ActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office 2021 Bind":
        serializer=Office2021BindActivationRequestSerializer(activation_request, data=data)

    elif category=="Office 2021 Mac Bind":
        serializer=Office2021MacBindActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office Home Business Windows":
        serializer=OfficeHomeBusinessWinActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office Home Business Mac":
        serializer=OfficeHomeBusinessMacActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office Home Student Windows":
        serializer=OfficeHomeStudentWinActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office Home Student Mac":
        serializer=OfficeHomeStudentMacActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Office 2021 Home Basic":
        serializer=Office2021HomeBasicActivationRequestSerializer(activation_request, data=data)


                        
    elif category=="Project Professional 2019":
        serializer=ProjectProfessional2019ActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Project Professional 2021":
        serializer=ProjectProfessional2021ActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Visio Professional 2019":
        serializer=VisioProfessional2019ActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Visio Professional 2021":
        serializer=VisioProfessional2021ActivationRequestSerializer(activation_request, data=data)




    elif category=="Windows Server 2016 Essential":
        serializer=WindowsServer2016EssentialActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Windows Server 2019 Standard":
        serializer=WindowsServer2019StandardActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Windows Server 2019 Datacenter":
        serializer=WindowsServer2019DatacenterActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Windows Server 2022 Datacenter":
        serializer=WindowsServer2022DatacenterActivationRequestSerializer(activation_request, data=data)



                        
    elif category=="Microsoft SQL Server 2019 Standard":
        serializer=MicrosoftSQLServer2019StandardActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Microsoft SQL Server 2019 Enterprise":
        serializer=MicrosoftSQLServer2019EnterpriseActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Microsoft SQL Server 2022 Standard":
        serializer=MicrosoftSQLServer2022StandardActivationRequestSerializer(activation_request, data=data)
                        
    elif category=="Microsoft SQL Server 2022 Enterprise":
        serializer=MicrosoftSQLServer2022EnterpriseActivationRequestSerializer(activation_request, data=data)
                   
    else:
        return Response({'error': 'Incorrect serial key for selected category.'}, status=status.HTTP_404_NOT_FOUND)

    return serializer