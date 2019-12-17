from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # #Check if the user has already made enquiry
        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_enquiry = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
        #     if has_enquiry:
        #         messages.error(request, 'Already made the enquiry for the listing')
        #         return redirect('/listings/'+listing_id)
            



        contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, phone = phone, message = message, user_id = user_id)
        contact.save()

        #Send Email
        # send_mail(
        #     'Property Listing Enquiry',
        #     'There has been a enquiry for '+ listing + 'Sign in to the admin panel for more info',
        #     'thesarozbhandari@gmail.com',
        #     [ realtor_email, 'mail2saroz@gmail.com'],
        #     fail_silently = False

        # )


        messages.success(request, 'Enquiry made successfully')
        return redirect('/listings/'+listing_id)
        


