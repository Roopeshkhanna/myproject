from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def accomodation(request):
    return render(request,'accomodation.html')
def contact(request):
    return render(request,'contact.html')
def countries(request):
    return render(request,'countries.html')
def part_time_job(request):
    return render(request,'part_time_job.html')
def interaction(request):
    return render(request,'interaction.html')
