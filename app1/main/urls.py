from django.urls import path
from main.views import index, indexItem

app_name = "main"

urlpatterns = [
    path('home/', index ),
    path('home/<int:my_id>/', indexItem, name="detail_id"),

]