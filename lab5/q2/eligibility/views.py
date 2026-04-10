from django.shortcuts import render
from datetime import datetime, date

def check_promotion(request):
    emp_ids = ["E101", "E102", "E103", "E104", "E105"]  # Sample IDs
    status = ""
    
    if request.method == "POST":
        doj_str = request.POST.get('doj')
        if doj_str:
            # Parse the date from the textbox (YYYY-MM-DD format)
            doj = datetime.strptime(doj_str, "%Y-%m-%d").date()
            today = date.today()
            
            # Calculate experience
            experience = today.year - doj.year - ((today.month, today.day) < (doj.month, doj.day))
            
            status = "YES" if experience > 5 else "NO"

    return render(request, 'eligibility/index.html', {
        'emp_ids': emp_ids, 
        'status': status
    })
