
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.forms import Form, ModelForm

from django.contrib import messages

class UserTestForm(UserCreationForm):

    username = forms.CharField(min_length=5)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', ]

    def save(self, commit=True ):
        instance = super(UserTestForm, self).save(commit=False)
        instance.is_active = False
        instance.password
        instance.save()




    # username = forms.CharField()
    # email = forms.EmailField()
    # password = forms.PasswordInput

    # class Meta:
    #     model = CartProducts
    #     fields = ['Count']
    #
    # def save(self, commit=True ):
    #     instance = super(CartProductForm, self).save(commit=False)
    #     instance.ProductsId = Products.objects.get(pk=self.data['product'])
    #     instance.CartId = Cart.objects.get(pk=self.data['cart'])
    #     instance.save()


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'username', 'password1', 'password2']
#
#     def save(self, commit=True ):
#         instance = super(CreateUserForm, self).save(commit=False)
#         instance.is_active = False
#         instance.save()
#
#
# class EditProfilForm(UserChangeForm):
#     password = None
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']
#
#
#
#
# class CartProductForm(forms.ModelForm):
#     product = forms.IntegerField()
#     cart = forms.IntegerField()
#
#     class Meta:
#         model = CartProducts
#         fields = ['Count']
#
#     def save(self, commit=True ):
#         instance = super(CartProductForm, self).save(commit=False)
#         instance.ProductsId = Products.objects.get(pk=self.data['product'])
#         instance.CartId = Cart.objects.get(pk=self.data['cart'])
#         instance.save()
#
#
# class CartProductChangeCountForm(forms.ModelForm):
#     product = forms.IntegerField()
#
#     class Meta:
#         model = CartProducts
#         fields = ['Count']
#
#     def save(self, commit=True ):
#         instance = super(CartProductChangeCountForm, self).save(commit=False)
#         c = (self.data['Count'])
#         w = int(float(c))
#
#         instance.Count = w
#         instance.CartId = CartProducts.objects.get(pk=self.data['product']).CartId
#
#         instance.save()
#
#
#
#
#
#
