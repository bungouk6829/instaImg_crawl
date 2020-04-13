from django.urls.conf import path
from main import views


app_name= 'main'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('detail_img/',views.detail_img,name='detail_img'),
]
