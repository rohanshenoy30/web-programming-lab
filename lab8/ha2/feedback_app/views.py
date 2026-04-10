# feedback_app/views.py
from django.shortcuts import render

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        sex = request.POST.get('sex')
        course = request.POST.get('course')
        
        # Determine Prefix
        prefix = "Mr." if sex == "Male" else "Ms."
        message = f"Thanks {prefix} {name} for your feedback"

        return render(request, 'feedback_app/result.html', {'message': message})
    
    return render(request, 'feedback_app/form.html')
