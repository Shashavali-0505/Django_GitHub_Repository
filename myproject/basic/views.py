from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def http1(request):
    # print(request)
    qp1 = request.GET.get('name')
    if qp1:
        return HttpResponse(f'heloo...iam {qp1} and i came from http response')
    else:
        return HttpResponse(f'heloo...i came from http response')

def json1(request):
    person_info = {"data":[{"name":"shasha","city":"knl"},{"name":"arun","city":"ndl"},{"name":"pallavi","city":"vizag"},{"name":"raghu","city":"kadapa"}]}
    return JsonResponse(person_info)