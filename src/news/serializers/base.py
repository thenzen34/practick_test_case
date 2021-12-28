from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    # def get_field_names(self, declared_fields, info):
    #     result = super().get_field_names(declared_fields, info)
    #     return result + ("trash", "updated")
    pass
