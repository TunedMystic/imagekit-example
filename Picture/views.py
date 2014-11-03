from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Picture.models import ProfilePic

# Create your views here.
def formview(request):
  if request.method == 'POST':
    p = request.FILES['avatarpic']
    myprofile = ProfilePic(avatar = p)
    myprofile.save()
    return HttpResponseRedirect("/Picture/viewall")
  else:
    return render(request, "Picture/form.html")

def viewall(request):
  pics = ProfilePic.objects.all()
  return render(request, "Picture/viewall.html", {"pics": pics})
    