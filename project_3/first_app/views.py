from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age': 15, 'lst' : ['I','Love','Myself'], 'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 1500
        },
        {
            'id' : 3,
            'name' : 'C++',
            'fee' : 4500
        }
    ]}
    return render(request,'home.html', context=d)