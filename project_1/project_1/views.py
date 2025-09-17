from django.http import HttpResponse

def home(request):
    return HttpResponse("Ajk amr mon bhalo Alhamdulillah")

def contact(request):
    return HttpResponse("This is contact List")
