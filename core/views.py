from django.shortcuts import render


def home_view(req):
    """
    Home page view
    """
    return render(req, "core/home.html")
