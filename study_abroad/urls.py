from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("accomodation/",views.accomodation,name="accomodation"),
    path("contact/",views.contact,name="contact"),
    path("countries/",views.countries,name="countries"),
    path("part_time_job/",views.part_time_job,name="part_time_job"),
    path("interaction/",views.interaction,name="interaction")
    
]
