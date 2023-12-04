from django import forms

class CachorroForm(ModelForm):
    class Meta:
        model = Cachorro
        fields = '__all__'
    raca = forms.ModelChoiceField(
        queryset=Raca.objects.all(),
    )