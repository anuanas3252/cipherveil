from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactBook

# Create your views here.
def add_contact(request):
    error_message = None
    if request.method == 'POST':
        # Get data from the request
        tag = request.POST.get('tag')
        name = request.POST.get('name')

        # Create a new ContactBook instance
        new_contact = ContactBook(tag=tag, name=name)

        try:
            # Save the new contact to the database
            new_contact.save()
            return redirect('view_contact')  # Redirect to a view displaying the list of contacts
        except Exception as e:
            error_message = f"Error: {str(e)}"
            #return render(request, 'error_page.html', {'error_message': error_message})

    return render(request, 'contactapp/add_contact.html', {'error_message': error_message})


def view_contact(request):
    error_message = None
    contacts = ContactBook.objects.all()
    return render(request, 'contactapp/view_contact.html', {'contacts': contacts})


def edit_contact(request, pk):
    error_message = None
    contact = get_object_or_404(ContactBook, pk=pk)

    if request.method == 'POST':
        # Update the contact details with the submitted form data
        contact.tag = request.POST['tag']
        contact.name = request.POST['name']
        contact.save()

        try:
            # Save the new contact to the database
            contact.save()
            return redirect('view_contact')  # Redirect to a view displaying the list of contacts
        except Exception as e:
            error_message = f"Error: {str(e)}"

    return render(request, 'contactapp/edit_contact.html', {'contact': contact, 'error_message': error_message})

def delete_contact(request, pk):
    # Get the contact instance
    contact = get_object_or_404(ContactBook, pk=pk)

    if request.method == 'POST':
        # Delete the contact
        contact.delete()
        # Redirect to a success page or any other appropriate page
        return redirect('view_contact')

    return render(request, 'contactapp/delete_contact.html', {'contact': contact})