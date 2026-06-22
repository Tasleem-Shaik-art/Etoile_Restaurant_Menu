from django.shortcuts import render
from .models import MenuItem

# This function fetches all food items and sends them to your HTML
def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})

# menu_app/views.py
def place_order(request):
    if request.method == 'POST':
        # 1. Get the list of IDs from the form checkboxes
        selected_ids = request.POST.getlist('selected_items')
        
        # 2. Fetch the actual items from the database
        ordered_items = MenuItem.objects.filter(id__in=selected_ids)
        
        # 3. Calculate the total price
        total_price = sum(item.price for item in ordered_items)

        # 4. DEFINE THE CONTEXT (Mapping your DB results to template variables)
        context = {
            'items': ordered_items,
            'total': total_price,
        }

        # 5. Pass the context to the summary page
        return render(request, 'menu/order_summary.html', context)
    
    # Fallback for GET requests if someone visits /order/ directly
    return render(request, 'menu/order_form.html')