from django.db import models
from userauth.models import TeacherProfile,User

class CommentSection(models.Model):
	Teacher = models.ForeignKey(TeacherProfile,related_name='comments',on_delete = models.CASCADE)
	created_on = models.DateTimeField(auto_now_add = True)
	SCORE_CHOICES = zip( range(1,6), range(1,6) )
	stars = models.IntegerField(choices=SCORE_CHOICES, null = True)
	Comment = models.TextField(blank = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	class Meta:
		ordering = ['-created_on']
