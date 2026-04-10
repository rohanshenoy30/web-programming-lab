import random
import string
from django.shortcuts import render

def captcha_view(request):
    # Initialize session state if new
    if 'captcha_text' not in request.session:
        request.session['captcha_text'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    message = ""
    disabled = False

    if request.method == "POST":
        user_input = request.POST.get('user_captcha')
        actual_captcha = request.session.get('captcha_text')

        if user_input == actual_captcha:
            message = "✅ Success! Captcha matched."
            request.session['attempts'] = 0  # Reset on success
            # Generate new for next time
            request.session['captcha_text'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        else:
            request.session['attempts'] += 1
            message = f"❌ Mismatch! Attempt {request.session['attempts']} of 3."

        # Disable logic if failed 3 or more times
        if request.session['attempts'] >= 3:
            message = "🚫 Input Disabled: Too many failed attempts."
            disabled = True

    return render(request, 'captcha.html', {
        'captcha': request.session['captcha_text'],
        'message': message,
        'disabled': disabled
    })
