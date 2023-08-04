from .script_fn import *
from datetime import datetime, date
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from django.http import JsonResponse


class UploadCSV(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        category = request.data.get('category').upper()
        if not file or not file.name.endswith('.csv'):
            return Response({'error': 'Please upload a valid CSV file.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            csv_reader = csv.DictReader(file.read().decode('utf-8').splitlines())

            created_records = []
            for row in csv_reader:
                serial_key = row.get('serial_key', None)
                activation_key = row.get('activation_key', None)
                if category=="A":
                    serializer = Windows10HomeActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="B":
                    serializer = Windows10HomeOEMActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="C":
                    serializer = Windows10ProActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="D":
                    serializer = Windows10ProOEMActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="E":
                    serializer = Windows11HomeActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="F":
                    serializer = Windows11HomeOEMActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="G":
                    serializer = Windows11ProActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="H":
                    serializer = Windows11ProOEMActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="I":
                    serializer = Office2019ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="J":
                    serializer = Office2019BindActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="K":
                    serializer = Office2021ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="L":
                    serializer = Office2021BindActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="M":
                    serializer = Office2021MacBindActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="N":
                    serializer = OfficeHomeBusinessWinActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="O":
                    serializer = OfficeHomeBusinessMacActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="P":
                    serializer = OfficeHomeStudentWinActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="Q":
                    serializer = OfficeHomeStudentMacActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="R":
                    serializer = Office2021HomeBasicActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="S":
                    serializer = ProjectProfessional2019ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="T":
                    serializer = ProjectProfessional2021ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="U":
                    serializer = VisioProfessional2019ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="V":
                    serializer = VisioProfessional2021ActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="W":
                    serializer = WindowsServer2016EssentialActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="X":
                    serializer = WindowsServer2019StandardActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="Y":
                    serializer = WindowsServer2019DatacenterActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="Z":
                    serializer = WindowsServer2022DatacenterActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="AA":
                    serializer = MicrosoftSQLServer2019StandardActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="AB":
                    serializer = MicrosoftSQLServer2019EnterpriseActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                elif category=="AC":
                    serializer = MicrosoftSQLServer2022StandardActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })
                
                elif category=="AD":
                    serializer = MicrosoftSQLServer2022EnterpriseActivationRequestSerializer(data={
                        'serial_key': serial_key,
                        'activation_key': activation_key,
                    })


                if serializer.is_valid():
                    serializer.save()
                    created_records.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': f'{len(created_records)} records created successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class UploadActivationKeys(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({'error': 'Please upload a valid CSV file.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            csv_reader = csv.DictReader(file.read().decode('utf-8').splitlines())

            created_records = []
            for row in csv_reader:
                activation_key = row.get('activation_key')
                category=row.get('category').upper()
                expiry_date= row.get('expiry_date', None)

                serializer = ActivationKeySerializer(data={
                    'activation_key': activation_key,
                    'category': category,
                    'expiry_date': expiry_date

                })

                if serializer.is_valid():
                    serializer.save()
                    created_records.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': f'{len(created_records)} records created successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetActivationKey(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        serial_key = data.get('serial_key')
        phone = data.get('phone')
        category=data.get('category', None)
        date_now=date.today()

        if not category:
            category= "Windows"

        if not serial_key or not phone:
            return Response({'error': 'Please provide both serial_key and phone.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if category=="Windows":
            activation_request, category = check_windows()

        if category=="Office":                                
            activation_request, category = check_office()

        if category=="Professional":
            activation_request, category = check_professional() 

        if category=="Server":
            activation_request, category = check_server() 

        if category=="SQL":
            activation_request, category = check_sql()

            if activation_request.activation_key=='None':
                print("activation key not found")
                try:
                    activation_keys = ActivationKeys.objects.filter(category=category, used=False)
                    print(activation_keys)
                    for key in activation_keys:
                        if key.expiry_date > date_now and key.used== False:
                            pass_key=key.activation_key
                            print(key)
                            activation_request.activation_key=pass_key
                            activation_request.request_date=datetime.now()
                            activation_request.is_available=False
                            activation_request.save()
                            key.used=True
                            key.save()
                            break
                        
                        activation_request.phone = phone
                        activation_request.save()
                    print(activation_request.activation_key)
                    
                    if category in ['Microsoft SQL Server 2022 Enterprise', 'Microsoft SQL Server 2022 Standard', 'Microsoft SQL Server 2019 Enterprise', 'Microsoft SQL Server 2019 Standard']:
                        activation_request, category = check_sql()
                    if category in ['Windows Server 2022 Datacenter', 'Windows Server 2019 Datacenter', 'Windows Server 2019 Standard', 'Microsoft SQL Server 2019 Standard']:
                        activation_request, category = check_server()
                    if category in ['Visio Professional 2021', 'Visio Professional 2019', 'Project Professional 2021', 'Project Professional 2019']:
                        activation_request, category = check_professional()
                    if category in ["Office 2021 Home Basic", "Office Home Student Mac", "Office Home Student Windows", "Office Home Business Mac", "Office Home Business Windows", "Office 2021 Mac Bind", "Office 2021 Bind", "Office 2019 Bind", "Office 2021", "Office 2019"]:
                        activation_request, category = check_office()
                    if category in ["Windows 11 Pro OEM", "Windows 11 Pro", "Windows 11 Home OEM", "Windows 10 Home", "Windows 10 Pro OEM", "Windows 10 Pro", "Windows 10 Home OEM", "Windows 10 Home"]:
                        activation_request, category = check_windows()
                    
                    send_text=f'Your {category} activation key is: {activation_request.activation_key} via: Original Software Products'
                    send_sms_via_api(send_text, phone)
                    return Response({'serial key': activation_request.serial_key,'activation_key': activation_request.activation_key}, status=status.HTTP_200_OK)
                except:
                    alt_msz_admin = f"New request for {category} from {phone}.\nPlease process the request as soon as possible and update the database from website"
                    send_sms_via_api(alt_msz_admin, '9819115285')
                    send_sms_via_api(alt_msz_admin, '9862906626')

                    alt_msz_user = f"We are processing your request for {category}.\nThank you for your patience."
                    send_sms_via_api(alt_msz_user, '9842271260')
                    return Response({'message': alt_msz_user}, status=status.HTTP_201_CREATED)

        return Response({'serial key': activation_request.serial_key, 'activation_key': activation_request.activation_key, 'First Requested': activation_request.request_date, 'Requested from': activation_request.phone, 'Category': category}, status=status.HTTP_200_OK)

class contactView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        sender_email = data.get('sender_email')
        msz = data.get('msz')
        try:
            contact_mail(sender_email, name, msz)
            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'message': f'Invalid email data: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'Failed to send email: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class manual_edit_serial_key(APIView):
    def put(self, request):
        data=request.data
        serial_key=data.get('serial_key')
        activation_key=data.get('activation_key')
        date_now=date.today()
        phone = data.get('phone')
        category=data.get('category')
        if not serial_key or not phone or not category or not activation_key:
            return Response({'error': 'Please provide all serial_key, phone, category and activation key.'}, status=status.HTTP_400_BAD_REQUEST)

        data={
            'serial_key': serial_key,
            'activation_key':activation_key,
            'request_date': date_now,
            'phone': phone,
            'is_available': False    
        }
        print(date_now)
        try:
            if category=="Windows":
                activation_request, category = check_windows(serial_key)
                print("1")

            if category=="Office":                                
                activation_request, category = check_office(serial_key)
                print("1")

            if category=="Professional":
                activation_request, category = check_professional(serial_key) 
                print("1")

            if category=="Server":
                activation_request, category = check_server(serial_key) 
                print("1")

            if category=="SQL":
                activation_request, category = check_sql(serial_key)
                print("1")

            activation_request.request_date=date_now
            activation_request.phone=phone
            activation_request.is_available=False
            activation_request.save
            serializer = update_serializer(activation_request, data, category)


            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Upadated as','serial key': activation_request.serial_key, 'activation_key': activation_request.activation_key, 'First Requested': activation_request.request_date, 'Requested from': activation_request.phone, 'Category': category}, status=status.HTTP_200_OK)
                # return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except:
            return Response({'error': 'Serial key not found in database'}, status=status.HTTP_400_BAD_REQUEST)
