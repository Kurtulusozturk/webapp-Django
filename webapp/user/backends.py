from django.contrib.auth.backends import ModelBackend
from user.models import User
from django.contrib.auth.hashers import check_password


class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):

        email = kwargs.get('email')
        password = kwargs.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            User().set_password(password)

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
