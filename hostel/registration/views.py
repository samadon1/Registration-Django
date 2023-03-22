from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterationForm


def index(request):
    message = ''
    form = RegisterationForm()

    if request.method == 'POST':
        form = RegisterationForm(request.POST)

        if form.is_valid():
            # register = form.save(commit=True)
            card_type = form.cleaned_data['id_card']
            card_id = form.cleaned_data['id_number']

            if card_type == "N" or card_type == "S":
                if len(card_id) == 8:
                    message = ''
                    form.save()
                    return redirect('https://www.myhostelapp.com/hosorhom')
                else:
                    message = "Incorrect ID Card number"
                    context = {
                    'form': form,
                    'message': message
                    }
                    
                    return render(request, 'registration/index.html', context)

            else:
                if len(card_id) == 10:
                    message = ''
                    form.save()
                    return redirect('https://www.myhostelapp.com/hosorhom')
                else:
                    message = "Incorrect ID Card number"
                    context = {
                    'form': form,
                    'message': message
                    }
                    
                    return render(request, 'registration/index.html', context)
            
            
        
    context = {
        'form': form,
        'message': message
    }
        

    return render(request, 'registration/index.html', context)

    
