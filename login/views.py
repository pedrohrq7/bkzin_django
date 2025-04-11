from django.shortcuts import render

# Create your views here.

def login(request):
    contexto = {
        'titulo' : 'Login'
    }
    return render(request, 
                  'login/index.html',
                  contexto,
                  )
