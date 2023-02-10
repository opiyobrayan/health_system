
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.home,name='home'),
    path('workplan', views.workplan,name='workplan'),
    path('pdf/<int:pk>', views.view_pdf, name='view_pdf'),
    path('excel', views.display_excel, name='excel'),
    path('activity', views.activity, name='activity'),
    path('add-activity', views.add_activity, name='add-activity'),
    path('partners', views.partners, name='partners'),

]
