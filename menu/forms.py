from menu.models import Category

from django import forms

from mptt.forms import TreeNodeChoiceFieldMixin, MPTTAdminForm


class CustomLabelChoiceField(TreeNodeChoiceFieldMixin, forms.ModelChoiceField):

    def label_from_instance(self, obj):
         label = super().label_from_instance(obj)
         return f'{obj.menu}: {label}'


class CategoryAdminForm(MPTTAdminForm):

    parent = CustomLabelChoiceField(queryset=Category.objects.all(), label='Родительская категория')

    class Meta:
        model = Category
        fields = '__all__'
