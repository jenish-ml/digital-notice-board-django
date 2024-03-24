from django.urls import path
from . import views

urlpatterns = [
    path('subject_add',views.add_subject),
    path('subject_view',views.view_subject),
    path('subject_delete/<int:id>',views.delete_subject),
    path('subject_edit/<int:id>',views.edit_subject),
    
]