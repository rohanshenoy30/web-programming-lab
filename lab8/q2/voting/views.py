from django.shortcuts import render, redirect
from .models import Vote

def vote(request):
    if request.method == "POST":
        choice = request.POST.get('choice')

        if choice:
            Vote.objects.create(choice=choice)
            return redirect('result')

    return render(request, 'vote.html')


def result(request):
    total = Vote.objects.count()

    good = Vote.objects.filter(choice='good').count()
    satisfactory = Vote.objects.filter(choice='satisfactory').count()
    bad = Vote.objects.filter(choice='bad').count()

    if total == 0:
        good_per = satisfactory_per = bad_per = 0
    else:
        good_per = round((good / total) * 100, 2)
        satisfactory_per = round((satisfactory / total) * 100, 2)
        bad_per = round((bad / total) * 100, 2)

    return render(request, 'result.html', {
        'good': good_per,
        'satisfactory': satisfactory_per,
        'bad': bad_per,
    })