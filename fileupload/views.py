# encoding: utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView
from .models import Picture
from .response import JSONResponse, response_mimetype
from .serialize import serialize
#from . import fetch
from . import fetch_py3
import os, subprocess
import glob
from . import sample_call

class PictureCreateView(CreateView):
    model = Picture
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

def analyze(request):
    search_string = sample_call.main_1()#{0: 'jeans', 1: 'denim', 2: 'clothing', 3: 'trousers', 4: 'pocket'}
    print(search_string)
    #return HttpResponse(search_string)
    search_string = search_string.strip("[]").replace("'", "").replace(" ","-").split(",")
    print(search_string)
    #return HttpResponse(search_string)
    string = ""
    for x in search_string:
        if (x == '-clothing' or x == '-product'):
            continue
        string += x.replace(" ","-")
    print(string)
    #string = 'jeans-denim-clothing-trousers-pocket'
    dictionary = fetch_py3.fetch_from_amazon(string)
    return render(request, 'products.html', {'dict': dictionary, 'query': string})


    '''modified code

    search_string = sample_call.main_1()#{0: 'jeans', 1: 'denim', 2: 'clothing', 3: 'trousers', 4: 'pocket'}
    print(search_string)
    #return HttpResponse(search_string)
    search_string = search_string.strip("[]").replace("'", "").split(",")
    print(search_string)
    #return HttpResponse(search_string)
    string = ""
    for x in search_string:
        if (x == "clothing" or x == "cloth" or x == "clothes"):
            continue
        else:
            string += x.replace(" ","")
    print(string)
    #string = 'jeans-denim-clothing-trousers-pocket'
    dictionary = fetch_py3.fetch_from_amazon(string)
    return render(request, 'products.html', {'dict': dictionary, 'query': string})
    '''
    dictionary = fetch.fetch_from_amazon('green-shirt-men')
    return render(request, 'products.html', {'dict': dictionary})

class BasicVersionCreateView(PictureCreateView):
    template_name_suffix = '_basic_form'


class BasicPlusVersionCreateView(PictureCreateView):
    template_name_suffix = '_basicplus_form'


class AngularVersionCreateView(PictureCreateView):
    template_name_suffix = '_angular_form'


class jQueryVersionCreateView(PictureCreateView):
    template_name_suffix = '_jquery_form'


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureListView(ListView):
    model = Picture

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
