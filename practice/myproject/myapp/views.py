from django.shortcuts import render,redirect


def index(request):
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        gender=request.POST.get("gender")

        request.session['name']=name
        request.session['password']=password
        request.session['gender']=gender


        return redirect('page2')   # redirect only after submit

    return render(request, "index.html")  # show page first

def page2(request):
    if request.method=="POST":
        return redirect("index")
    return render(request, "page2.html",{
        "name": request.session.get("name"),
        "password": request.session.get("password"),
        "gender": request.session.get("gender"),
    })