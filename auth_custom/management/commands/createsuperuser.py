from django.contrib.auth.management.commands.createsuperuser import Command as SuperUserCommand


class Command(SuperUserCommand):
    def handle(self, *args, **options):
        # i'm trying to override "python3 manage.py createsuperuser" command
        # the purpose is whenever super user created by that command,
        # i'll create record in table quiz_administrator as well.

        # i'm using alternative way, which is create admin by "fixtures" file
        # so we can ignore this way until we find a way to do this
        a = 1
