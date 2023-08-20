from django.urls import path

from fruitapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prediction/', views.predictionCreation, name='prediction'),
    path('list_prediction/<str:id>/', views.PredictionListView.as_view(), name='listPrediction'),
    path('results/', views.resultsCreation, name='results'),
    path('list_results/<str:id>/', views.ResultsListView.as_view(), name='listResults'),
    path('results_uploaded/', views.resultsShower, name='resultShow'),
    path('real_time/', views.predict_real_time, name='predict-real-time'),
    path('load_image/', views.predictionCreation, name='loadImage'),
    path('dashboard/<str:id>/', views.DashboardView.as_view(), name='dashboard'),
    path('train/', views.predictionCreation, name='train'),
]
