from django.shortcuts import render

def input_view(request):
    # Just displays the empty form
    return render(request, 'input.html')

def display_view(request):
    if request.method == "POST":
        # Capture parameters sent via the POST request
        manufacturer = request.POST.get('manufacturer')
        model_name = request.POST.get('model_name')
        
        context = {
            'manufacturer': manufacturer,
            'model_name': model_name
        }
        # Forward data to the result page
        return render(request, 'display.html', context)
