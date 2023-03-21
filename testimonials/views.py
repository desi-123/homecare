from django.shortcuts import render
from .models import Testimonials

def testimonial(request):
 testimonials = Testimonials.objects.all()
 context = {
  'testimonials': testimonials,
 }
 return render(request, 'pages/testimonial.html', context)