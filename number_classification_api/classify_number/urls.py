from django.urls import path
from classify_number.views import classify_number

urlpatterns = [
    path('classify-number/', classify_number),
]
