import django.contrib.auth as auth

user_model = auth.get_user_model()

class CollventBackend(object):
    def authenticate(self, user=None, email=None, phone=None):
        if not email and not phone:
            return None
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            try:
                user = user_model.objects.get(phone=phone)
            except user_model.DoesNotExist:
                return None
        return user

    def get_user(self, user_id):
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
