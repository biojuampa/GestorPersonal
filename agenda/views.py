from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import Q

from .models import Contact, ZipCode
from .forms import ContactForm, ContactDetailForm, ZipCodeForm


def set_labels2urls(form, fields):
    for field in fields:
        field_path = field.replace('_', '')
        
        if field_path.endswith('s'):
            field_path = field.rstrip('s')
        
        path = reverse(f'{field_path}_new')
        name = form[field].label.title()
        url = format_html(f'<a href="{path}">{name}</a>')
        form[field].label = url

    return None


def get_contact_list(ordered=True, ascendent=True):
    if ordered and ascendent:
        contact_list = Contact.objects.order_by('last_name', 'names')
    elif ordered and not ascendent:
        contact_list = Contact.objects.order_by('-last_name', '-names')
    elif not ordered:
        contact_list = Contact.objects.all()

    return contact_list


def agenda_index(request):
    contact_list = get_contact_list()
    return render(request, 'agenda/agenda_index.html', {'contact_list': contact_list})


def contact_new(request):
    contact_list = get_contact_list()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        if not contact_form.is_valid():
            set_labels2urls(contact_form, ('location',
                                           'zip_code',
                                           'groups',
                                           'jobs',
                                           )
                            )
            return render(request, 'agenda/contact_new.html', {'contact_form': contact_form,
                                                               'contact_list': contact_list,
                                                               }
                          )

        contact_form.save()        
        return redirect('agenda_index')

    contact_form = ContactForm()
    set_labels2urls(contact_form, ('location',
                                   'zip_code',
                                   'groups',
                                   'jobs',
                                   )
                    )    
    return render(request, 'agenda/contact_new.html', {'contact_form': contact_form,
                                                       'contact_list': contact_list,
                                                  }
                  )


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact_form = ContactDetailForm(instance=contact)
    contact_list = get_contact_list()

    return render(request, 'agenda/contact_detail.html', {'contact': contact,
                                                          'contact_form': contact_form,
                                                          'contact_list': contact_list,
                                                          }
                  )

######################################################################################

def contact_edit(request, pk):
    contact_list = get_contact_list()
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        if not contact_form.is_valid():
            set_labels2urls(contact_form, ('location',
                                           'zip_code',
                                           'groups',
                                           'jobs',
                                           )
                            )
            return render(request, 'agenda/contact_edit.html', {'contact_form': contact_form,
                                                                'contact_list': contact_list,
                                                                }
                          )

        contact_form.save()        
        return redirect('agenda_index')

    contact_form = ContactForm(instance=contact)
    set_labels2urls(contact_form, ('location',
                                   'zip_code',
                                   'groups',
                                   'jobs',
                                   )
                    )

    return render(request, 'agenda/contact_edit.html', {'contact': contact,
                                                        'contact_form': contact_form,
                                                        'contact_list': contact_list,
                                                        }
                  )

######################################################################################

def contact_remove(request, pk):
    contact = Contact.objects.get(pk=pk)
    if not contact.photo.name.endswith('nobody.png'):
        contact.photo.delete()
    contact.delete()

    return redirect('agenda_index')


def contact_search(request):
    search = request.GET['search'].strip()
    q1 = Q(names__contains=search)
    q2 = Q(last_name__contains=search)
    contact_match = Contact.objects.filter(q1 | q2).order_by('last_name', 'names')

    return render(request, 'agenda/agenda_index.html', {'contact_list': contact_match})

######################################################################################
######################################################################################
######################################################################################

def zipcode_new(request):
    if request.method == 'POST':
        zipcode_form = ZipCodeForm(request.POST)
        if not zipcode_form.is_valid():
            return render(request, 'agenda/zipcode.html', {'zipcode_form': zipcode_form})

        zipcode_form.save()
        return redirect('contact_new')

    zipcode_form = ZipCodeForm()
    return render(request, 'agenda/zipcode.html', {'zipcode_form': zipcode_form})


def zipcode_detail(request, pk):
    pass


def zipcode_edit(request, pk):
    pass


from django.http import HttpResponse

def location_new(request):
    return HttpResponse('<h1>En construcción ...</h1>')

def job_new(request):
    return HttpResponse('<h1>En construcción ...</h1>')

def group_new(request):
    return HttpResponse('<h1>En construcción ...</h1>')

