from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def sample(request):
    return render(request, 'sample-inner-page.html')