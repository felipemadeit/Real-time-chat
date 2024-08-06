from django.shortcuts import render

# Home view
def home_view (request):
    return render(request, 'home.html')
