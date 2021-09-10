from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import akun, paslon, votemasuk
from .forms import masuk, terakhir, masuk2
from django.db.models import F
import datetime
# Create your views here.
def index(request):
	return render(request, "testapp/index.html", {})
def pemilihan(request):
	if(request.method=="POST"):
		form=masuk2(request.POST)
		if(form.is_valid()):
			try:
				nama=akun.objects.get(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
				context={
					'namadb':nama,
					'username':form.cleaned_data['username'],
					'password':form.cleaned_data['password']
				}
				return render(request, "testapp/pemilihana.html", context)
			except akun.DoesNotExist:
				return render(request, "testapp/loginform.html", {'errormsg':"Username atau Pass salah!"})
		else:
			return render(request, "testapp/loginform.html", {'errormsg':"Invalid request. Try again."})
	else:
		return render(request, "testapp/loginform.html", {'errormsg':"Invalid request. Try again."})
def loginform(request):
	return render(request, "testapp/loginform.html", {})
def konfirmasi(request):
	form=terakhir(request.POST)
	if(form.is_valid()):
		paslon_id=form.cleaned_data['paslon']
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		if(paslon_id=='1'):
			choose="Achmad Za’im Mudzaki"
		elif(paslon_id=='2'):
			choose="Alicia Chandra"
		elif(paslon_id=='3'):
			choose="Bintang Afrillia Deviana L"
		nama=akun.objects.get(username=username,password=password)
		context={
			'data_nama':nama,
			'data_choose':choose,
			'username':username,
			'password':password,
			'paslon_id':paslon_id
		}
		return render(request, "testapp/konfirmasi.html", context)
	else:
		return render(request, "testapp/loginform.html", {'errormsg':"Invalid request. Try again."})
def donepage(request):
	form=terakhir(request.POST)
	if(form.is_valid()):
		paslon_id=form.cleaned_data['paslon']
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		account=akun.objects.get(username=username,password=password)
		if(account.voted):
			return render(request, "testapp/loginform.html", {'errormsg':"Akun ini sudah pernah vote!"})
		else:
			account.voted='True'
			account.save()
			if(paslon_id=='1'):
				calon=paslon.objects.get(nomorurut="1",isputra="True")
			elif(paslon_id=='2'):
				calon=paslon.objects.get(nomorurut="2",isputra="True")
			elif(paslon_id=='3'):
				calon=paslon.objects.get(nomorurut="3",isputra="True")
			calon.votecount=F('votecount')+1
			calon.save()
			timestamp=votemasuk(waktu=datetime.datetime.now(),pilihan=paslon_id,nama=account.nama)
			timestamp.save()
			return render(request, "testapp/votetelahmasuk.html", {})
	else:
		return render(request, "testapp/loginform.html", {'errormsg':"Invalid request. Try again."})
def resetakuns(request):
	return render(request, "testapp/reset.html")
def resetted(request):
	form=masuk2(request.POST)
	if(form.is_valid()):
		return render(request, "testapp/resetted.html")
	return render(request, "testapp/reset.html", {'errormsg':"Opo meneh. Try again mang."})