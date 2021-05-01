from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))


generate_token = TokenGenerator()


def send_email(subject, adress, massage):

        msg = EmailMultiAlternatives(
            # subject
            subject,
            # content
            # to
            to=[adress],
            # from
            from_email='',
        )
        msg.attach_alternative(massage, "text/html")
        msg.send()
