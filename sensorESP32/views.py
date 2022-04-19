from rest_framework import status
from rest_framework.decorators import api_view
from sensorESP32.models import SensorReading, Recommadation
from sensorESP32.serializers import SensorDataSerializer, cropRecommandationSerializer
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

import os, pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier 



@api_view(['GET'])
def sensor_data_list(request):
    if request.method =='GET':
        reading_data = SensorReading.objects.all()
        serializer = SensorDataSerializer(reading_data, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'DELETE', 'POST'])
def sensor_data_detail(request, pk):
    try: 
        readings = SensorReading.objects.get(pk=pk) 
    except SensorReading.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'},\
             status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        sensor_data_serializer = SensorDataSerializer(readings) 
        return JsonResponse(sensor_data_serializer.data) 

    # elif request.method == 'PUT': 
    #     sensor_data = JSONParser().parse(request) 
    #     sensor_data_serializer = SensorDataSerializer(readings, data=sensor_data) 
    #     if sensor_data_serializer.is_valid(): 
    #         sensor_data_serializer.save() 
    #         return JsonResponse(sensor_data_serializer.data) 
    #     return JsonResponse(sensor_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        readings.delete() 
        return JsonResponse({'message': 'Sensor read data was deleted successfully!'},\
             status=status.HTTP_204_NO_CONTENT)
    
    elif request.method =="POST":
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'key': 'value'}, status=status.HTTP_200_OK)
        return Response({'key': 'value'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def crop_recommendation(request):
    if request.method =='GET':
        recommadation = Recommadation.objects.all()
        serializer = cropRecommandationSerializer(recommadation, many=True)
        reading_data = Recommadation.objects.all()
        reading_data_ph = SensorReading.objects.last().ph
        reading_data_moisture = SensorReading.objects.last().moisture
        reading_data_humidity = SensorReading.objects.last().humidity
        reading_data_temperature = SensorReading.objects.last().temperature
        
        excel_data = pd.read_excel(r'C:\Users\sakar\Desktop\Final year project\backend\fyp\sensorESP32\datset.xlsx', header = 0)
        print(excel_data)                                                              
        print(excel_data.shape)   

        labels = preprocessing.LabelEncoder()
        crop = labels.fit_transform(list(excel_data["CROP"]))

        PH = list(excel_data["PH"])
        MOISTURE = list(excel_data["MOISTURE"])
        HUMIDITY = list(excel_data["HUMIDITY"])
        TEMPERATURE =list(excel_data["TEMPERATURE"])

        features = list(zip(PH, MOISTURE, HUMIDITY, TEMPERATURE))
        features = np.array([PH, MOISTURE, HUMIDITY, TEMPERATURE])

        features = features.transpose()
        print(features.shape)                                                                                          # Printing the shape of the features after getting transposed.
        print(crop.shape)

        model = KNeighborsClassifier(n_neighbors=8)
        model.fit(features, crop)

        prediction = np.array([reading_data_ph,reading_data_moisture,reading_data_humidity,reading_data_temperature])
        print(prediction)
        prediction = prediction.reshape(1,-1)
        print(prediction)
        prediction = model.predict(prediction)
        print(prediction)


        crop_name = str()
        if prediction == 0:                                                                                          
            crop_name = 'Apple(सेब)'
        elif prediction == 1:
            crop_name = 'Banana(केला)'
        elif prediction == 2:
            crop_name = 'Blackgram(काला चना)'
        elif prediction == 3:
            crop_name = 'Chickpea(काबुली चना)'
        elif prediction == 4:
            crop_name = 'Coconut(नारियल)'
        elif prediction == 5:
            crop_name = 'Coffee(कॉफ़ी)'
        elif prediction == 6:
            crop_name = 'Cotton(कपास)'
        elif prediction == 7:
            crop_name = 'Grapes(अंगूर)'
        elif prediction == 8:
            crop_name = 'Jute(जूट)'
        elif prediction == 9:
            crop_name = 'Kidneybeans(राज़में)'
        elif prediction == 10: 
            crop_name = 'Lentil(मसूर की दाल)'
        elif prediction == 11:
            crop_name = 'Maize(मक्का)'
        elif prediction == 12:
            crop_name = 'Mango(आम)'
        elif prediction == 13:
            crop_name = 'Mothbeans(मोठबीन)'
        elif prediction == 14:
            crop_name = 'Mungbeans(मूंग)'
        elif prediction == 15:
            crop_name = 'Muskmelon(खरबूजा)'
        elif prediction == 16:
            crop_name = 'Orange(संतरा)'
        elif prediction == 17:
            crop_name = 'Papaya(पपीता)'
        elif prediction == 18:
            crop_name = 'Pigeonpeas(कबूतर के मटर)'
        elif prediction == 19:
            crop_name = 'Pomegranate(अनार)'
        elif prediction == 20:
            crop_name = 'Rice(चावल)'
        elif prediction == 21:
            crop_name = 'Watermelon(तरबूज)'
        from datetime import datetime
        print(crop_name)
        payload = {
            "recommadate_crop": crop_name
        }
        serializer = cropRecommandationSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)

@api_view(['GET'])
def recommadation_list(request):
    if request.method =='GET':
        reading_data = Recommadation.objects.all()
        serializer = cropRecommandationSerializer(reading_data, many=True)
        return Response(serializer.data)



        