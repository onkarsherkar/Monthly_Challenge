from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
   "january":"Eat no Meat be vegetarian",
   "february":"Walk at least 20 minutes Everyday !!!",
   "march":"Learn Django at least 20 minutes everyday",
   "april" : "Drink 3.7 liter Water daily",
   "may" : "Do yoga at least 30 min in day",
   "june" : "Solve puzzle game to increase efficiency",
   "july" : "Watch 1 documentry in a month",
   "august" : "Learn new technologies",
   "sepetember" : "Read one book at least in week",
   "october" : "Don't Drink and Drive",
   "november" : "Build Self confidence",
   "december" : "Stay safe be Happy"
}

def index(request):
   list_items=""
   months = list(monthly_challenges.keys())

   for month in months:
      capitalize_month = month.capitalize()
      month_path = reverse("month-challenge",args=[month])
      list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
   
   response_data = f"<ul>{list_items}</ul>"
   return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
   months = list(monthly_challenges.keys())
   if month > 0 and month <= len(months):
      forward_month = months[month-1]
   else:
      return HttpResponseNotFound("Invalid Month")
   redirect_path = reverse('month-challenge',args=[forward_month])   
   return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
   try:
      challenge_text = monthly_challenges[month]
      return HttpResponse(challenge_text)
   except:
      return HttpResponseNotFound("This month is not supported")
