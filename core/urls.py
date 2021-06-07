from django.urls import path

from .views import index, TestApi1, TestApi2

urlpatterns = [
    path('', index, name='index'),
    path('test-api1/', TestApi1.as_view(), name='TestApi1'),
    path('test-api1/<int:pk>/', TestApi1.as_view(), name='TestApi1WithPk'),
    path('test-api2/', TestApi2.as_view(), name='TestApi2'),
    path('test-api2/<int:pk>/', TestApi2.as_view(), name='TestApi2WithPk'),
]