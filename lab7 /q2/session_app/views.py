from django.shortcuts import render, redirect

def first_page(request):
    if request.method == "POST":
        # Save data from TextBoxes and DropDown into sessions
        request.session['name'] = request.POST.get('name')
        request.session['roll'] = request.POST.get('roll')
        request.session['subject'] = request.POST.get('subject')
        return redirect('second_page')
    return render(request, 'firstPage.html')

def second_page(request):
    # Retrieve the data from the session
    context = {
        'name': request.session.get('name', 'N/A'),
        'roll': request.session.get('roll', 'N/A'),
        'subject': request.session.get('subject', 'None')
    }
    return render(request, 'secondPage.html', context)
