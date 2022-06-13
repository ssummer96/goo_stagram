from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import *

from .models import Photo4

# photo테이블에 있는 전체 리스트 정보 검색
def photo_list(request):
    photos = Photo4.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})



class PhotoUploadView(CreateView):
    model = Photo4
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(DeleteView):
    model = Photo4
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo4
    fields = ['photo', 'text']
    template_name = 'photo/update.html'








