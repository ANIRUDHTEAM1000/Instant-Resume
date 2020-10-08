from django.shortcuts import render
from docxtpl import DocxTemplate
from django.conf import settings

import os


# Create your views here.
def index(request):
    # if get request
    if request.method == 'GET':
        return render(request, 'apply.html')
    # if post request
    else:
        # collect data from form using request
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        phone = request.POST['phone']
        mail = request.POST['mail']
        address = request.POST['address']
        # opening the template docx file of resume where we wanna insert these parameters
        tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'static\\res_original.docx'))
        # now insert or render the parameters
        tpl.render({'name': firstname + " " + secondname, 'address': address, 'phone': phone, 'gmail': mail})
        # now save the rendered template to static again
        tpl.save(os.path.join(settings.BASE_DIR, 'static\\res.docx'))
        return render(request, 'result.html')
