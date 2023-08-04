from django.db import models

class Windows10HomeActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows10HomeOEMActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows10ProActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows10ProOEMActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows11HomeActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows11HomeOEMActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows11ProActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Windows11ProOEMActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"



class Office2019ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Office2019BindActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Office2021ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Office2021BindActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Office2021MacBindActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class OfficeHomeBusinessWinActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class OfficeHomeBusinessMacActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class OfficeHomeStudentWinActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class OfficeHomeStudentMacActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class Office2021HomeBasicActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"



class ProjectProfessional2019ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class ProjectProfessional2021ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class VisioProfessional2019ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class VisioProfessional2021ActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"




class WindowsServer2016EssentialActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class WindowsServer2019StandardActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class WindowsServer2019DatacenterActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class WindowsServer2022DatacenterActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"



class MicrosoftSQLServer2019StandardActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class MicrosoftSQLServer2019EnterpriseActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class MicrosoftSQLServer2022StandardActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"

class MicrosoftSQLServer2022EnterpriseActivationRequest(models.Model):
    serial_key = models.CharField(max_length=100, null=True, blank=True)
    activation_key = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"Serial Key: {self.serial_key}, Activation Key: {self.activation_key}, Phone: {self.phone}, Request Date: {self.request_date}"



class ActivationKeys(models.Model):
    activation_key = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    expiry_date = models.DateField(null=True, blank=True)
    used=models.BooleanField(default=False)

    def __str__(self):
        return f"Activation Key : {self.activation_key}, category: {self.category}, Phone: {self.expiry_date}, Used: {self.used}"
