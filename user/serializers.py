from prompt_toolkit.key_binding.bindings.named_commands import self_insert
from rest_framework import serializers
from .models import CustomUser
from shared.utility import check_email_or_phone
class SingUpSerializers(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    auth_status=serializers.CharField(read_only=True)
    verify_type=serializers.CharField(read_only=True)


    def __init__(self):
        super().__init__()
        self.fields['email_or_phone']=serializers
    class Meta:
        model=CustomUser
        fields=('id','auth_type','verify_type')



