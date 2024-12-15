import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import App

@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            app = App.objects.create(
                app_name=data['app_name'],
                version=data['version'],
                description=data['description']
            )
            return JsonResponse({'id': app.id, 'message': 'App added successfully!'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data format'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def get_app(request, id):
    try:
        app = App.objects.get(id=id)
        return JsonResponse({
            'id': app.id,
            'app_name': app.app_name,
            'version': app.version,
            'description': app.description
        })
    except App.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)

@csrf_exempt
def delete_app(request, id):
    
    try:
        app = App.objects.get(id=id)
        app.delete()
        return JsonResponse({'message': 'App deleted successfully!'}, status=200)
    except App.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)
