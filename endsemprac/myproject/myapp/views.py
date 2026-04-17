from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method=="POST":

        name=request.POST.get("name")
        age=request.POST.get("age")
        request.session["name"]=name
        request.session["age"]=age
        return redirect(second)

    return render(request,"index.html")



def second(request):

    return render(request,"second.html",{
        "name":request.session.get("name"),
        "age":request.session.get("age"),
    })

def third(request):
    return render(request,"third.html")


def fourth(request):
    return render(request,"fourth.html")