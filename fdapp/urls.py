from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_fd/', views.add_fd, name='add_fd'),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
    path('generate-report/', views.generate_report, name='generate_report'),
    path('export-excel/', views.export_to_excel, name='export_to_excel'),  # ✅ this line is required

    path('preview/', views.preview_uploaded_data, name='preview_uploaded_data'),
    path('edit-fd/<int:pk>/', views.edit_fd, name='edit_fd'),
    path('delete-fd/<int:pk>/', views.delete_fd, name='delete_fd'),

]
