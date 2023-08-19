from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sklearn.linear_model import LinearRegression 
from django.shortcuts import render



model = LinearRegression()

@csrf_exempt
def get_data(request):
    data = {"result": "your_processed_data"}
    return JsonResponse(data)

@csrf_exempt
def make_prediction(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_data = data.get('input_data')
            prediction = model.predict([[input_data]]) 
            return JsonResponse({"prediction": prediction[0]})
        except Exception as e:
            return JsonResponse({"error": str(e)})
def model_interaction(request):
    return render(request, 'index.html')