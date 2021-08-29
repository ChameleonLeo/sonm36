from django import forms
from django.forms.formsets import formset_factory


GENRES = [
    ('other', 'Other'),
    ('metal', 'Metal'),
    ('rock', 'Rock'),
    ('jazz', 'Jazz'),
    ('classical', 'Classical'),
    ('pop', 'Pop'),
    ('techno', 'Techno'),
]


class ArtistForm(forms.Form):
    name = forms.CharField(max_length=100, label="Artist name")
    band = forms.CharField(max_length=50, label="Band name")
    genre = forms.ChoiceField(
        required=False,
        choices=GENRES,)


ArtistFormSet = formset_factory(ArtistForm, extra=1)
