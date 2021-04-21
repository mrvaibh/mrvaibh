from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'home_page': 'active'}
    return render(request, 'home/index.html', context)


def about(request):
    context = {'about_page': 'active'}
    return render(request, 'home/about.html', context)


def team(request):
    context = {'team_page': 'active'}
    return render(request, 'home/team.html', context)


def testimonials(request):
    context = {'testimonials_page': 'active'}
    return render(request, 'home/testimonials.html', context)


def services(request):
    context = {'services_page': 'active'}
    return render(request, 'home/services.html', context)


def portfolio(request):
    context = {'portfolio_page': 'active'}
    return render(request, 'home/portfolio.html', context)


def pricing(request):
    context = {'pricing_page': 'active'}
    return render(request, 'home/pricing.html', context)


def blog(request):
    context = {'blog_page': 'active'}
    return render(request, 'home/blog.html', context)


def blog_single(request, pk):
    context = {
        "blog_single_page": "active",
        'blog_id': pk,
    }
    return render(request, 'home/blog-single.html', context)


def contact(request):
    context = {'contact_page': 'active'}
    return render(request, 'home/contact.html', context)
