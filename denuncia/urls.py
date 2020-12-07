from django.urls import path
from .views import list_denuncia, create_denuncia, update_denuncia, delete_denuncia

urlpatterns = [
    path('', list_denuncia, name="list_denuncia"),
    path("new", create_denuncia, name='create_denuncia'),
    path("update/<int:id>/", update_denuncia, name="update_denuncia"),
    path("delete/<int:id>/", delete_denuncia, name="delete_denuncia")
]

