from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == "POST":
        try:
            # Take two integer inputs
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operation = request.POST.get('operation')

            # Perform operation based on dropdown selection
            if operation == 'add':
                result = num1 + num2
            elif operation == 'sub':
                result = num1 - num2
            elif operation == 'mul':
                result = num1 * num2
            elif operation == 'div':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by Zero"
        except (ValueError, TypeError):
            result = "Error: Please enter valid integers"

    return render(request, 'calculator.html', {'result': result})
