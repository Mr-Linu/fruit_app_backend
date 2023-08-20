from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from fruitapp.models import Prediction, Results

from fruitapp.serializer import ImageSerializer, PredictionSerializer, ResultsSerializer
from user.models import AppUser
from . import utils

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({"Message": "Welcome"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def predictionCreation(request):

    if request.method == "POST":
        try:
            data=request.data  
            serializer = PredictionSerializer(data=data)
            
            if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data,
                        status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return e

class PredictionListView(APIView):
    
    def get(self, request, id, format=None):
        try:
            user = AppUser.objects.get(id=id)
            predictions = Prediction.objects.filter(user=user)
        except (AppUser.DoesNotExist, Prediction.DoesNotExist):
            return Response({'Message': "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def resultsCreation(request):

    if request.method == "POST":
        try:
            data=request.data  
            serializer = ResultsSerializer(data=data)
            
            if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data,
                        status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return e

class ResultsListView(APIView):
    
    def get(self, request, id, format=None):
        try:
            user = AppUser.objects.get(id=id)
            result = Results.objects.filter(user=user)
        except (AppUser.DoesNotExist, Results.DoesNotExist):
            return Response({'Message': "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResultsSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class DashboardView(APIView):
    
#     def get(self, request, id, format=None):
#         try:
#             user = AppUser.objects.get(id=id)
#             predictions = Prediction.objects.filter(user=user)
#             results = Results.objects.filter(user=user)
            
#         except (AppUser.DoesNotExist, Results.DoesNotExist,Prediction.DoesNotExist):
#             return Response({'Message': "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
#         print(1)
#         result = ResultsSerializer(results, many=True)
#         predicts = PredictionSerializer(predictions, many=True)
#         data = {'results':result, 'prediction': predicts, 'total_results': results.count(), "total_predictions": predictions.count()}
#         print(2)
#         return Response({"dashboard_data":data}, status=status.HTTP_200_OK)
    


@api_view(['POST'])
def resultsCreation(request):
    if request.method == "POST":
        try:
            data = request.data
            test_image_path = "/home/ltabari/Desktop/FInal year/project trials/one/dataset/fruit_test_data/banana/rot.webp"
            image = 'media/nanana.jpg'
            # Call the utility function to predict the fruit
            # model_results = utils.predict_fruit(image)
            # Open and read the image file as binary
            with open(image, "rb") as img_file:
                # Call the utility function to predict the fruit
                model_results = utils.predict_fruit(img_file)

            # Print the model results
            print(model_results)
            
            serializer = ImageSerializer(data=data)
            
            if serializer.is_valid():
                # serial_data = serializer.save()
                
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def resultsShower(request):
    if request.method == "GET":
        try:
            data = request.data
            test_image_path = "/home/ltabari/Desktop/FInal year/project trials/one/dataset/fruit_test_data/banana/rot.webp"
            # image = 'media/nanana.jpg'
            # Call the utility function to predict the fruit
            # model_results = utils.predict_fruit(image)
            # Open and read the image file as binary

            image = request.query_params.get('image')
            with open(image, "rb") as img_file:
                # Call the utility function to predict the fruit
                model_results = utils.predict_fruit(img_file)

            # Print the model results
            model_results
            
            
            return Response(model_results, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def predict_real_time(request):
    if request.method == "POST":
        try:
            image = request.FILES.get('image')  # Get the uploaded image from the request
            if not image:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Call the utility function to predict the fruit
            model_results = utils.predict_fruit(image)
            
            return Response(model_results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DashboardView(APIView):
    
    def get(self, request, id, format=None):
        try:
            user = AppUser.objects.get(id=id)
            predictions = Prediction.objects.filter(user=user)
            results = Results.objects.filter(user=user)
            
        except (AppUser.DoesNotExist, Results.DoesNotExist, Prediction.DoesNotExist):
            return Response({'Message': "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the queryset objects
        result_serializer = ResultsSerializer(results, many=True)
        prediction_serializer = PredictionSerializer(predictions, many=True)
        
        # Create a data dictionary containing the serialized results
        data = {
            'results': result_serializer.data,
            'predictions': prediction_serializer.data,
            'total_results': results.count(),
            'total_predictions': predictions.count()
        }
        
        return Response({"dashboard_data": data}, status=status.HTTP_200_OK)
