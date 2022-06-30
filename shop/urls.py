from django.contrib import admin
from django.urls import path
from my_shop.views import index, by_rubric, ItemCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('my_shop/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', ItemCreateView.as_view(), name='add'),
]
