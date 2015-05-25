from django.shortcuts import render

# Create your views here.
def home(request):
    volunteer = Volunteer.objects.get(id= request.user.id)
#    if volunteer is not None:
    if volunteer.is_active:
        info = {} 
        for field, value in volunteer:
            info[field] = value
        return render(request, "home.html", {'volunteer' : volunteer} )
    else:
        return HttpResponse("This account has been disabled. Please email Volunteer@sdyoutopia.com for more information.")
