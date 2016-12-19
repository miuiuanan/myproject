from rest_framework import status
from ex_design_template.models import design
from ex_design_template.serializers import TemplateSerializer


class TemplateRepository:
    def get_template_list(self):
        return design.objects.all()

    def get_template_detail(self, ex_id: int):
        return design.objects.get(pk=ex_id)

    def post_template(self, data: dict):
        return data, status.HTTP_201_CREATED

    def put_template(self, ex_id: int, data: dict):
        return data, status.HTTP_200_OK

    def delete_template(self,ex_id:int):
        TemplateRepository.get_template_detail(self, ex_id=ex_id).delete()
        return status.HTTP_204_NO_CONTENT