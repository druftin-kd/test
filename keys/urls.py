from django.urls import path
from .views import UploadCSV, UploadActivationKeys, GetActivationKey, contactView, manual_edit_serial_key
urlpatterns = [
    path('upload-csv/', UploadCSV.as_view(), name='upload_csv'),
    path('upload-activation-keys/', UploadActivationKeys.as_view(), name='upload_activation_keys'),
    path('get-activation-key/', GetActivationKey.as_view(), name='get_activation_keys'),
    path("contact/", contactView.as_view(), name="contact"),
    path("edit-key/", manual_edit_serial_key.as_view(), name="edit-key"),
]
