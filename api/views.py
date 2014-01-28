
import django.http
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from forms import newApiUser
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper


def index(request):
    if request.method == 'POST':
        if 'sub' in request.POST:
            form = newApiUser(request.POST)
            if form.is_valid():
                form.save()
                
                
                filename="cajal3d_v1_0_0.zip"
                wrapper = FileWrapper(file(filename))
                response = HttpResponse(wrapper, content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=cajal3d.zip'                
                messages.success(request, 'Thank you for registering.')
                return response
                                
            else:
                return django.http.HttpResponse ("Invalid Form. Please enter the registeration information", mimetype='text/html')
    else:
        '''New API Form'''
        form = newApiUser()
        context = {'form': form}
        return render_to_response('index.html',context,context_instance=RequestContext(request))
        
        
    
    
