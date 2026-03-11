from django.urls import path
from . import views

urlpatterns = [

    path("employees/", views.list_employees),
    path("employees/add/", views.add_employee),
    path("employees/delete/<int:id>/", views.delete_employee),

    path("attendance/", views.get_attendance),
    path("attendance/mark/", views.mark_attendance),

]