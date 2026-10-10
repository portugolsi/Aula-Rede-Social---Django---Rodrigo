from django import forms
from .models import Post

class PostForm (forms.ModelForm):

    class Meta:

        model = Post
        fields = ["legenda","imagem"]

        widgets = {

            "legenda" : forms.Textarea(

                attrs={
                    "placeholder":"Digite a sua legenda aqui",
                    "rows":5
                }

            )

        }