from django.shortcuts import render
from .models import User
from django.shortcuts import render, get_object_or_404

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def createUserView(request):
    return render(request, 'users/create.html')

def createUser(request):
    data = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            rfc = request.POST.get('rfc')
            photo = request.POST.get('photo')

            user = User(name=name, email=email, age=age, rfc=rfc, photo=photo)
            user.save()
            data["user"] = user
            data["message"] = "User Created"
            data["status"] = "success"
    except Exception as e:
            
        data["message"] = str(e)
        data["status"] = "error"

    return render(request, 'users/create.html', data)

def  userDetail(request, id):
    user = get_object_or_404(User, id=id) 
    return render(request, 'users/detail.html', {'user': user})