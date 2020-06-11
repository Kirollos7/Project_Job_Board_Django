from django.urls import path
from job import views

urlpatterns = [
    path('job',views.job_list),
    path('<int:id>',views.job_detail),
]