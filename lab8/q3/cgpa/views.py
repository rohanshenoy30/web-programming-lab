from django.shortcuts import render, redirect

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        marks = request.POST.get('marks')

        error = None

        # Validation
        if not name:
            error = "Name is required"
        elif not marks:
            error = "Marks required"
        else:
            try:
                marks = float(marks)
                if marks < 0 or marks > 500:
                    error = "Marks must be between 0 and 500"
            except:
                error = "Enter valid number"

        if error:
            return render(request, 'home.html', {
                'error': error,
                'data': request.POST
            })

        # Calculate CGPA
        cgpa = round(marks / 50, 2)

        # Store in session
        request.session['name'] = name
        request.session['cgpa'] = cgpa

        return redirect('result')

    return render(request, 'home.html')


def result(request):
    return render(request, 'result.html', {
        'name': request.session.get('name'),
        'cgpa': request.session.get('cgpa'),
    })