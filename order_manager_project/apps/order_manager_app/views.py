from django.shortcuts import render, redirect

def index(request):

    return render(request, 'order_manager_app/index.html')

def dashboard(request):

    return render(request, 'order_manager_app/dashboard.html')

def create(request):

    return render(request, 'order_manager_app/create.html')

def show_all(request):

    return render(request, 'order_manager_app/show_all.html')

def manage(request):

    return render(request, 'order_manager_app/manage.html')

def view(request):

    return render(request, 'order_manager_app/view.html')

def edit(request):

    return render(request, 'order_manager_app/edit.html')