# contacts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

# Home page displaying all contacts
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})

    query = request.GET.get('search', '')  # Get the search query from the URL (GET method)
    
    if query:
        contacts = Contact.objects.filter(
            first_name__icontains=query
        ) | Contact.objects.filter(
            last_name__icontains=query
        ) | Contact.objects.filter(
            phone__icontains=query
        ) | Contact.objects.filter(
            email__icontains=query
        )
    else:
        contacts = Contact.objects.all()
    
    return render(request, 'contacts/home.html', {'contacts': contacts, 'query': query})

def search_contact(request):
    query = request.GET.get('search', '')  # Get the search query from the URL (GET method)
    contacts = Contact.objects.filter(
        first_name__icontains=query
    ) | Contact.objects.filter(
        last_name__icontains=query
    ) | Contact.objects.filter(
        phone__icontains=query
    ) | Contact.objects.filter(
        email__icontains=query
    )

    return render(request, 'contacts/search_contact.html', {'contacts': contacts, 'query': query})
    
# Add new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ContactForm()

    return render(request, 'contacts/add_contact.html', {'form': form})

# Update an existing contact
def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/update_contact.html', {'form': form, 'contact': contact})

# Delete a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return render(request, 'contacts/delete_confirmation.html', {'contact': contact})
