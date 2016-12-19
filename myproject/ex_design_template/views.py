from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
# from django.shortcuts import render
#
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from ex_design_template.forms import TemplateForm
# from ex_design_template.models import design
from django.views import View

# Create your views here.
from ex_design_template.forms import TemplateForm


class ListTemplateView(View):
    template_name = "list_template.html"

    def get(self, request):
        ex = design.objects.all()
        paginator = Paginator(ex, 6)
        pageNumber = request.GET.get('page')
        try:
            list_ex = paginator.page(pageNumber)
        except PageNotAnInteger:
            list_ex = paginator.page(1)
        except EmptyPage:
            list_ex = paginator.page(paginator.num_pages)
        context = {
            'ex_templates': list_ex
        }
        return render(request, self.template_name, context)


#
#
class PostTemplateView(View):
    template_name = "add_template.html"
    form = TemplateForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        errors = ""
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['image']
            static_path = '/static/product/img/' + f.name
            default_storage.save('ex_design_template/' + static_path, ContentFile(f.read()))
            design(
                name=form.data.get("name"),
                subtitle=form.data.get("subtitle"),
                image=static_path,
                price=form.data.get("price"),
                hitcount=form.data.get("hitcount")
            ).save()
        else:
            errors = "Co loi xay ra"
        return render(request, self.template_name, {"form": self.form, "errors": errors})


# def templates(request):
#     ex = design.objects.all()
#     context = {
#         'ex_templates': ex
#     }
#     return render(request, "list_template.html", context)

class DetailTemplateView(View):
    name = "detail_template.html"

    def get(self, request, ex_id):
        ex_detail = design.objects.get(pk=ex_id)
        context = {
            'detail': ex_detail
        }
        return render(request, self.name, context)

        # def add(request):
        #     errors = ""
        #     if request.method == 'POST':
        #         form = TemplateForm(request.POST, request.FILES)
        #         if form.is_valid():
        #             f = request.FILES['image']
        #             static_path = '/static/product/img/' + f.name
        #             default_storage.save('ex_design_template/' + static_path, ContentFile(f.read()))
        #             design(
        #                 name=form.data.get("name"),
        #                 subtitle=form.data.get("subtitle"),
        #                 image=static_path,
        #                 price=form.data.get("price"),
        #                 hitcount=form.data.get("hitcount")
        #             ).save()
        #         else:
        #             errors = "Co loi xay ra"
        #
        #     return render(request, "add_template.html", {"form": TemplateForm(), "errors": errors})


class EditTemplateView(View):
    name = "edit_template.html"
    form = TemplateForm

    def get(self, request, ex_id):
        # self.form = TemplateForm(request.GET, request.FILES).data
        des = design.objects.get(pk=ex_id)
        self.form.data(des)
        context = {
            'design': des,
            'form': self.form
        }
        return render(request, self.name, context)

    def post(self, request, ex_id, static_path=None):
        global des
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            des = design.objects.get(pk=ex_id)
            if len(request.FILES) > 0:
                f = request.FILES['image']
                static_path = '/static/product/img/' + f.name
                default_storage.save('ex_design_template/' + static_path, ContentFile(f.read()))
                des.image = static_path
            des.name = self.form.data.get("name"),
            des.subtitle = self.form.data.get("subtitle"),
            des.price = self.form.data.get("price"),
            des.hitcount = self.form.data.get("hitcount")
            des.save()
        # des.name = request.POST["name"]
        # des.subtitle = request.POST["subtitle"]
        # des.image = static_path
        # des.price = request.POST["price"]
        # des.hitcount = request.POST["hitcount"]
        context = {
                    "design": des
                }
        return render(request, self.name, context)

#
class DeleteTemplateView(View):
    name = "list_template.html"

    def get(self, request, ex_id):
        des = design.objects.get(pk=ex_id)
        des.delete()
        ex = design.objects.all()
        context = {
            'ex_templates': ex
        }
        return render(request, self.name, context)


from django.http import HttpResponse
from django.shortcuts import render, render_to_response
#
# # Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
#
from ex_design_template.models import design
from ex_design_template.serializers import TemplateSerializer
#
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def template_list(request):
#     form = TemplateForm(request.POST, request.FILES)
#     if request.method == 'GET':
#         des = design.objects.all()
#         serializer = TemplateSerializer(des, many=True)
#         return JSONResponse(serializer.data,"add_template.html", {"form": TemplateForm()})
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TemplateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.data, status=400)
#
#
@csrf_exempt
def temlate_detail(request, ex_id):
    try:
        des = design.objects.get(pk=ex_id)
    except design.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TemplateSerializer(des)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TemplateSerializer(des, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        des.delete()
        return HttpResponse(status=204)

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ex_design_template.logics import TemplateLogic
# from ex_design_template.models import design
from ex_design_template.serializers import TemplateSerializer


# class TemplateListView(APIView):
#     template_name = "list_template.html"
#
#     def get(self, request, format=None):
#         form = TemplateForm(request.POST, request.FILES)
#         des = TemplateLogic.get_template_list(self)
#         context = {
#             'ex_templates': des
#         }
#         return render(request,self.template_name,context)
#         # return Response(des)
#
# class TemplatePost(APIView):
#     template_name="add_template.html"
#     form = TemplateForm
#     def get(self, request):
#         return render(request, self.template_name, {'form': self.form})
#
#     def post(self, request, format=None):
#         form = TemplateForm(request.POST, request.FILES)
#         des, status = TemplateLogic.post_template(self, request.data)
#         # Response(des)
#         return render_to_response(des,request, self.template_name, {"form": self.form})
#
#
# class TemplateDetail(APIView):
#     name = "detail_template.html"
#
#     def get(self, request, pk, format=None):
#         des = TemplateLogic.get_template_detail(self, ex_id=pk)
#         context = {
#             'detail': des
#         }
#         return render(request,self.name,context)
#
#     def put(self, request, pk, format=None):
#         des, status = TemplateLogic.put_template(self, ex_id=pk, data=request.data)
#         return Response(des, status)
#
#     def delete(self, request, pk, format=None):
#         status = TemplateLogic.delete_template(self, ex_id=pk)
#         return Response(status)
