from django.shortcuts import render,HttpResponseRedirect
from .forms import AjoutEtudiant
from .models import User
from django.contrib import messages
# Create your views here.

#fonction ajouter et affichier les donneé des etudiant 
def add_show(request):
    if request.method == 'POST':
        fm = AjoutEtudiant(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['nom']
            pm=fm.cleaned_data['prenom']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg= User(nom = nm, prenom = pm,email = em,password = pw)
            reg.save()  
            messages.success(request,'etudiant ajouter avec succées')
            fm = AjoutEtudiant()

    else:
        fm = AjoutEtudiant()
    etud = User.objects.all()
    return render(request,'etudiant/addandshow.html',{'form':fm,'etud':etud})
#fonction modifier un etudiant
def update_data(request, id):
     if request.method == 'POST':
         pi = User.objects.get(pk=id)
         fm = AjoutEtudiant(request.POST, instance=pi)
         if fm.is_valid():
            fm.save()  
            etud = User.objects.all()
            messages.success(request,'etudiant update avec succées')
            return render(request,'etudiant/addandshow.html',{'form':fm,'etud':etud})
     else:
         pi = User.objects.get(pk=id) 
         fm = AjoutEtudiant(instance=pi)
     return render(request,'etudiant/updateetud.html',{'form':fm,'id':id})
#fonction supprimier un etudiant
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.success(request,'etudiant delete avec succées')
        return HttpResponseRedirect('/')
