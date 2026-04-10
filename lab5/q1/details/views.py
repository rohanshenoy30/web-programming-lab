from django.shortcuts import render

def index(request):
    context = {}
    if request.method == "POST":
        # Get basic details
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        
        # Get marks and calculate
        eng = float(request.POST.get('english', 0))
        phy = float(request.POST.get('physics', 0))
        chem = float(request.POST.get('chemistry', 0))
        
        total = eng + phy + chem
        percentage = (total / 300) * 100

        # Construct result string for textarea
        result_str = (f"Name: {name}\nDOB: {dob}\nAddress: {address}\n"
                      f"Contact: {contact}\nEmail: {email}\n"
                      f"Marks - Eng: {eng}, Phy: {phy}, Chem: {chem}")

        context = {'result': result_str, 'percentage': f"{percentage:.2f}%"}
        
    return render(request, 'details/index.html', context)
