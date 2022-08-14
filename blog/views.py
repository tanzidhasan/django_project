from django.shortcuts import render


def home(request):
    return render(request, 'blog/Welcome_Page.html')

def about_us(request):
    return render(request, 'blog/About_Us_Page.html')

def blood_donation(request):
    return render(request, 'blog/Blood_Donation_Page.html')





