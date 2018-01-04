from django.shortcuts import render
from l2app.forms import NewUserForm

#from l2app.models import User
# Create your views here.

def index(request):
    return render(request,'l2app/index.html')

def users(request):
    
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("ERROR FORM INVALID")


    return render(request, 'l2app/users.html', {'form':form})


    #Info from previous exercise
    #user_list = User.objects.order_by('first_name')
    #user_dict = {'users':user_list}
    #return render(request,'l2app/users.html',context=user_dict)

