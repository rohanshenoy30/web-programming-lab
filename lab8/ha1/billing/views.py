# billing/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'billing/index.html')

def produce_bill(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        items = request.POST.getlist('items') # Handles multiple checkboxes
        quantity = int(request.POST.get('quantity', 0))

        # Dummy price logic
        prices = {'HP': 500, 'Nokia': 200, 'Samsung': 300, 'Motorola': 250, 'Apple:': 1000}
        item_type_prices = {'Mobile': 100, 'Laptop': 500}

        base_price = prices.get(brand, 0)
        type_price = sum([item_type_prices.get(i, 0) for i in items])
        
        total_amount = (base_price + type_price) * quantity

        context = {
            'brand': brand,
            'items': ", ".join(items),
            'quantity': quantity,
            'total': total_amount
        }
        return render(request, 'billing/bill.html', context)
