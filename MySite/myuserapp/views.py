from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to myPage',
        'clist':['django','python','javascript '],
        'numbers':[], #if data inserted then printed inserted data
        'student_details':[
        {'name':'govinda','phone':9840292144},
        {'name':'testing','phone':45909945}
        ]
    }
    return render(request,"index.html",data)
def wish(request):
    return HttpResponse("Welcome to Django")
def index(request):
    return HttpResponse("Index Page")
def about(request):
    return HttpResponse("About Page")
def service(request):
    return HttpResponse("Service Page")
def test(request):
    return HttpResponse("Test view")
def contact(request):
    return HttpResponse("Contact info")
def courseDetails(request, courseid):
    return HttpResponse (courseid)