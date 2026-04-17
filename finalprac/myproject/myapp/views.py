from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        request.session["name"]=name
        request.session["age"]=age
        request.session["gender"]=gender
        return redirect(fourth)

    return render(request,"index.html")


def second(request):
    return render(request,"second.html")


def third(request):
    return render(request,"third.html")

def fourth(request):
    return render(request,"fourth.html",{
        "name":request.session.get("name"),
        "age":request.session.get("age"),
        "gender":request.session.get("gender"),
    })