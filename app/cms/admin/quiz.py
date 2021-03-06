from django import forms

from emoji_picker.widgets import EmojiPickerTextInput, EmojiPickerTextarea

from .attachment import DisplayImageWidgetStackedInline


class QuizModelForm(forms.ModelForm):
    correct_option = forms.BooleanField(required=False, label='Richtige Antwort',
        help_text='Setze hier einen Haken, wenn diese Antwort-Option die richtige ist.')
    quiz_option = forms.CharField(
        required=True, label='Quiz Option', widget=EmojiPickerTextInput, max_length=20,
        help_text='Trage hier den Button-Text für eine Antwortmöglichkeit ein. '
                  'Um ein Quiz zu erstellen müssen mindestens 2, maximal 3 Buttons gegeben sein.')
    quiz_text = forms.CharField(
        required=True, label='Quiz Antwort', widget=EmojiPickerTextarea, max_length=640,
        help_text='Hier kannst du einen individuellen Text für diese Antwortmöglichkeit eingtragen')


class QuizAdminInline(DisplayImageWidgetStackedInline):
    image_display_fields = ['media']
    extra = 0
