from django import forms
from django.core.exceptions import ValidationError
from .models import CommentSection

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentSection
		fields = ("Comment","stars")
		widgets = {'Comment (optional)': forms.Textarea(attrs={'rows': 3}),}
    


'''
from django import forms
from django.core.cache import cache
from django.core.exceptions import ValidationError
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
    
    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        
        if user.comment_set.count() >= 10:
		last_comment_time = cache.get(f'last_comment_time_{user.id}')
		if last_comment_time and (timezone.now() - last_comment_time).seconds < 3600:
		raise ValidationError("You have exceeded the maximum number of comments per hour.")
		else:
		cache.set(f'last_comment_time_{user.id}', timezone.now(), 3600)

		return cleaned_data


'''

