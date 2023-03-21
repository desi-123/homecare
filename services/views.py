from django.shortcuts import render
from .models import Service_list,Service_text, Service_photos
def service(request):
 servicePhotos = Service_photos.objects.all()
 serviceLists = Service_list.objects.all()
 ServiceTexts = Service_text.objects.all()
 context = {
  'servicePhotos': servicePhotos,
  'serviceLists': serviceLists,
  'serviceTexts': ServiceTexts
 }
 return render(request, 'pages/service.html', context)
