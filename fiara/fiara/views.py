from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PersonneForm
from .models import Personne


def supprimer_personne(request, id):
    personne = Personne.objects.filter(id=id).first()
    if personne:
        personne.delete()
        return HttpResponse("Suppression réussie")
    else:
        return HttpResponse("Personne non trouvée")

def modifier_personne(request, id):
    personne = Personne.objects.get(id=id)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return redirect('personnes')
    else:
        form = PersonneForm(instance=personne)
    return render(request, 'modifier_personne.html', {'form': form, 'personne': personne})

def personnes(request):
    modifier_id = request.GET.get('modifier')
    if request.method == "POST":
        if modifier_id:
            personne = Personne.objects.get(id=modifier_id)
            form = PersonneForm(request.POST, instance=personne)
            if form.is_valid():
                form.save()
                return redirect('personnes')
        else:
            form = PersonneForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('personnes')
    else:
        form = PersonneForm()
        if modifier_id:
            personne = Personne.objects.get(id=modifier_id)
            form = PersonneForm(instance=personne)

    context = {
        "title": "personnes",
        "form": form,
        "personnes": Personne.objects.all(),
        "modifier_id": modifier_id
    }
    return render(request, "personnes.html", context)


def home(request):
    context = {"title": "home"}
    return render(request, "home.html", context)

# views.py

def voitures(request):
    context = {"title": "voitures", "form": VoitureForm()}
    return render(request, "voitures.html", context)
