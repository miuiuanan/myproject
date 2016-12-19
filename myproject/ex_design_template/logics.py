from rest_framework import status

from ex_design_template.repositorys import TemplateRepository
from ex_design_template.serializers import TemplateSerializer


class TemplateLogic:
    def get_template_list(self):
        des = TemplateRepository.get_template_list(self)
        serializer = TemplateSerializer(des, many=True)
        return serializer.data

    def get_template_detail(self, ex_id: int):
        return TemplateRepository.get_template_detail(self,ex_id=ex_id)

    def post_template(self, data: dict):
        serializer = TemplateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return TemplateRepository.post_template(self, data=data)
        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def put_template(self, ex_id: int, data: dict):
        des = TemplateRepository.get_template_detail(self, ex_id=ex_id)
        serializer = TemplateSerializer(des, data=data)
        if serializer.is_valid():
            serializer.save()
            return TemplateRepository.put_template(self, ex_id=ex_id, data=data)
        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_template(self, ex_id: int):
        return TemplateRepository.delete_template(self, ex_id=ex_id)
