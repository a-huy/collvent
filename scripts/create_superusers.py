from utils import djenv
import accounts.models as am

andy = am.User.objects.create_superuser(
    password = 'anguyen',
    email = 'anguyenhuy@gmail.com',
    phone = '7144019740',
)
andy.first_name = 'Andy'
andy.last_name = 'Nguyen'
andy.save()

ben = am.User.objects.create_superuser(
    password = 'bchow',
    email = 'benachow@gmail.com',
    phone = '1234567890',
)
ben.first_name = 'Benjamin'
ben.last_name = 'Chow'
ben.save()

mike = am.User.objects.create_superuser(
    password = 'mwilson',
    email = 'anguyenhuy@gmail.com',
    phone = '1357924680',
)
mike.first_name = 'Michael'
mike.last_name = 'Wilson'
mike.save()
