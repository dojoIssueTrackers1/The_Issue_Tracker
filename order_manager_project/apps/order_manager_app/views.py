from django.shortcuts import render, redirect
from .models import User
from .models import Issue
from django.contrib import messages
import bcrypt

def index(request):

    return render(request, 'order_manager_app/index.html')

def dashboard(request):

    topPicks = User.objects.get(id=request.session['id']).issued_by.filter(priority=3)

    context = {
        'show': topPicks,
    }

    return render(request, 'order_manager_app/dashboard.html', context)

def create(request):

    return render(request, 'order_manager_app/create.html')

def show_all(request):

    context = {
        'all_issues': User.objects.get(id=request.session['id']).issued_by.order_by("-priority")
    }

    return render(request, 'order_manager_app/show_all.html', context)

def manage(request):

    context = {
        'all_issues': User.objects.get(id=request.session['id']).issued_by.order_by("-priority")
    }

    return render(request, 'order_manager_app/manage.html', context)

def view(request, issue_id):

    submittedIssues = Issue.objects.get(id=issue_id)

    context = {
        'show': submittedIssues,
    }

    return render(request, 'order_manager_app/view.html', context)

def edit(request, issue_id):

    context = {
        'edit': Issue.objects.filter(id=issue_id)
    }

    return render(request, 'order_manager_app/edit.html', context)

def register(request):
    if (request.method == "POST"):
        errors = User.objects.registration_validator(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            newFirst = request.POST['first_name']
            newLast = request.POST['last_name']
            newEmail = request.POST['email']
            newPw = request.POST['pw']
            if newPw == request.POST['cpw']:
                encryptedPW = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
                b = User(first_name=newFirst, last_name=newLast, email=newEmail, pw=encryptedPW)
                b.save()
            messages.success(request, "Successfully registered!")
            if "id" not in request.session:
                request.session["first_name"] = newFirst
                request.session['id'] = b.id
            return redirect('/dashboard')

def login(request):
    if (request.method == "POST"):
        errors = User.objects.login_validator(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        user = User.objects.filter(email=request.POST['LEmail'])
        if bcrypt.checkpw(request.POST['Lpw'].encode(), user[0].pw.encode()):
            # messages.success(request, "You're logged in!!")
            if 'id' not in request.session:
                request.session['id'] = User.objects.get(email=request.POST['LEmail']).id
                request.session['first_name'] = User.objects.get(email=request.POST['LEmail']).first_name
            return redirect('/dashboard')
        else:
            errors['pw'] = "That password or e-mail did not match"
            messages.error(request, errors['pw'])
            return redirect('/')

def createNew(request):

    me = User.objects.get(id=request.session['id'])
    trip = Issue.objects.create(
        order_number= request.POST['ord_num'],
        customer_id = request.POST['cust_id'],
        issue_type = request.POST['issueType'],
        description = request.POST['description'],
        priority = request.POST['priority'],
        creator=me
    )

    return redirect('/show_all')

def update(request):
    if request.method == "POST":
        update = Issue.objects.get(id=request.POST['id'])
        update.order_number = request.POST['ord_num']
        update.customer_id = request.POST['cust_id']
        update.issue_type = request.POST['issue']
        update.description = request.POST['description']
        update.priority = request.POST['priority']
        update.save()

    return redirect('/manage')

def logout(request):
    request.session.flush()
    return redirect('/')



