from django.urls import path
from .views import list_usuario, create_usuario, update_usuario, delete_usuario

urlpatterns = [
    path('', list_usuario, name="list_usuario"),
    path("newUser", create_usuario, name='create_usuario'),
    path("update/<int:id>/", update_usuario, name="update_usuario"),
    path("delete/<int:id>/", delete_usuario, name="delete_usuario")
]