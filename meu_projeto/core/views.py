from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        try:
            expression = request.POST.get('expression', '')
            result = eval(expression)
        except Exception as e:
            result = 'Error'
        return JsonResponse({'result': result})
    return render(request, 'index.html')
