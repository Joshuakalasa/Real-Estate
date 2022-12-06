from django.shortcuts import render, redirect
from .models import Listing #we are going to use listings fro models so lets import it
from .forms import ListingForm

from django.contrib.auth.decorators import login_required
# Create your views here.
#here is where we handle logic
#when you go to a certain page its these code that runs.
#could be any action, add something aod delete somthing
#****CRUD -creat, retrieve, update, delete, list

#to make view we can use classes or functions
@login_required(login_url='login')
def listing_list(request): #name of models and the action/argument is request coming from user or browser
    #fetch all the listings in the database using ORM
    #object is a property on models for operations on database
    listings =  Listing.objects.all() #list all listing and put it in variable listings
    #conext is pyhton dictionary
    context = {
        "listings": listings
    }
    #return to user as response
    return render(request, "listings.html", context) #context is data you want to inject into this template



#getting a specific listing
#use primary key on the model
@login_required(login_url='login')
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

#to creat and delete we use forms module
@login_required(login_url='login')
def listing_create(request):

    
    form = ListingForm()
    if request.method == "POST":
        #populating the form with request data
        form = ListingForm(request.POST, request.FILES)
   
        if form.is_valid():
            form.save() 
            return redirect("/") #after submitting go to
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context) 

    #update function
@login_required(login_url='login')    
def listing_update(request, pk):

    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        #populating the form with request data
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
   
        if form.is_valid():
            form.save() 
            return redirect("/") #after submitting go to
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context) 

   # delete
@login_required(login_url='login')
def listing_delete(request, pk):

    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")

    # form = ListingForm(instance=listing)

    # if request.method == "POST":
    #     #populating the form with request data
    #     form = ListingForm(request.POST, instance=listing)

    #     if form.is_valid():
    #         form.save() 
    #         return redirect("/") #after submitting go to
    # context = {
    #     "form": form
    # }
    # return render(request, "listing_delete.html", context) 