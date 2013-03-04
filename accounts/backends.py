import django.contrib.auth as auth

user_model = auth.get_user_model()

class CollventBackend(object):
    def authenticate(self, identifier, password=None):
        try:
            user = user_model.objects.get(email=identifier)
        except user_model.DoesNotExist:
            try:
                user = user_model.objects.get(phone=identifier)
            except user_model.DoesNotExist:
                return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None

# http://stackoverflow.com/questions/2787650/manually-logging-in-a-user-without-password
class HashModelBackend(object):
    def authenticate(self, hash=None):
        try:
            user = user_model.objects.get(uuid=hash)
        except user_model.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None