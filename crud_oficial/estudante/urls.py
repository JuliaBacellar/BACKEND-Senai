from django.urls import path
from . import views
 
urlpatterns = [
    path('list', views.list_all),
    path('<int:pk>', views.aluno_by_id),
    path('post', views.create_aluno),
    path('update/<int:pk>', views.update_aluno),
    path('delete/<int:pk>', views.delete_aluno),
    path('print/<str:text>', views.print_text),
]