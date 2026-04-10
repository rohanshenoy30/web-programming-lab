from django.shortcuts import render, redirect
import re

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        errors = {}

        # Username validation
        if not username:
            errors['username'] = "Username is required"
        elif len(username) < 3:
            errors['username'] = "Minimum 3 characters required"

        # Password validation
        if not password:
            errors['password'] = "Password is required"
        elif len(password) < 6:
            errors['password'] = "Minimum 6 characters required"

        # Email validation
        if not email:
            errors['email'] = "Email is required"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors['email'] = "Invalid email"

        # Contact validation
        if not contact:
            errors['contact'] = "Contact is required"
        elif not contact.isdigit() or len(contact) != 10:
            errors['contact'] = "Must be 10 digits"

        # If errors → reload page
        if errors:
            return render(request, 'register.html', {
                'errors': errors,
                'data': request.POST
            })

        # Store in session
        request.session['username'] = username
        request.session['email'] = email
        request.session['contact'] = contact

        return redirect('success')

    return render(request, 'register.html')


def success(request):
    return render(request, 'success.html', {
        'username': request.session.get('username'),
        'email': request.session.get('email'),
        'contact': request.session.get('contact'),
    })