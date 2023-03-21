from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from contactmessages.models import ContactByMessage
from .models import About, About_team, Home, Contact
def home(request):
 homes = Home.objects.all()
 contacts = Contact.objects.all()
 context = {
  'homes': homes,
  'contacts': contacts
 }
 return render(request, 'pages/home.html', context)
def contact(request):
 if request.method == 'POST':
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  phone = request.POST['phone']
  message = request.POST['message']
  user_id = request.POST['user_id']

  # Check if user has messaged already
  if request.user.is_authenticated:
   user_id = request.user.id
   has_contacted = ContactByMessage.objects.all().filter(user_id=user_id)
   if has_contacted:
    messages.error(request, 'You have already messaged')
    return redirect('home')

  contactmessage = ContactByMessage(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message, user_id=user_id)
  contactmessage.save() 

  # Send Email
  send_mail(
   'Message from' + first_name,
   'There has been a message from costumer. Sign into the admin panel for more info',
   email,
   ['desie21mn@gmail.com'],
   fail_silently=False
  )



  messages.success(request, 'Your request has been submitted, we will get back to you soon.')
  return redirect('home')


 contacts = Contact.objects.all()
 context = {
  'contacts': contacts
 }
 return render(request, 'pages/contact.html', context)

#  About Section
def about(request):
 about = About.objects.all()
 teams = About_team.objects.all()
 context = {
  'about': about,
  'teams': teams,
 }
 return render(request, 'pages/about.html', context)

