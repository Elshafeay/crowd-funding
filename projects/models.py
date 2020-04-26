from django.db import models
from users.models import UserModel


# Category Model
class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	image = models.ImageField(upload_to='categories', null=True)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


# Project Model
class Project(models.Model):
	STATUS_CODES = (
		(-1, 'cancelled'),
		(0, 'running'),
		(1, 'finished'),
	)
	title = models.CharField(max_length=50)
	details = models.TextField()
	target = models.IntegerField()
	rate = models.FloatField(default=0)
	cover = models.ImageField(upload_to='projects/covers')
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.IntegerField(choices=STATUS_CODES, default=0)
	category = models.ForeignKey(
		Category,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def __repr__(self):
		return  \
			f"project("\
			f"title={self.title}, " \
			f"target={self.target}, " \
			f"rate={self.rate}, " \
			f"owner={self.owner.get_full_name()})"


# Tag Model
class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


# Project-Tag relation Model
class ProjectTags(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Project Tag"
		verbose_name_plural = "Project Tags"
		unique_together = ('tag', 'project')

	def __str__(self):
		return f"{self.project.title} => {self.tag.name}"


# Project-Images Model
class ProjectImages(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='projects/images')

	class Meta:
		verbose_name = "Project Image"
		verbose_name_plural = "Project Images"

	def __str__(self):
		return self.project.title


# Saved_Projects Model
class SavedProject(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	saved_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Saved Project"
		verbose_name_plural = "Saved Projects"
		unique_together = ('user', 'project')

	def __str__(self):
		return f"{self.user.get_full_name()} => {self.project.title}"


# Donation Model
class Donation(models.Model):
	project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
	donation = models.IntegerField()
	donated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return \
			f"{self.user.get_full_name()} " \
			f"=donated=> {self.donation} " \
			f"=to=> {self.project.title}"


# Review Model
class Review(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	rate = models.IntegerField(null=True, blank=True)
	liked = models.BooleanField(default=False)
	reported = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'project')

	def __str__(self):
		return f"{self.user.get_full_name()} => {self.project.title}"


# Comment Model
class Comment(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.get_full_name()} => {self.project.title}"


# Replies Model
class Reply(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	reply = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Replies"

	def __str__(self):
		return self.reply


# CommentReports Model
class CommentReports(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('user', 'comment')
		verbose_name = "Comment Report"
		verbose_name_plural = "Comment Reports"


# Featured Project Model
class FeaturedProject(models.Model):
	project = models.OneToOneField(
		Project,
		on_delete=models.CASCADE,
		unique=True
	)
	featured_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-featured_at']
		verbose_name = "Featured Project"
		verbose_name_plural = "Featured Projects"

	def __str__(self):
		return self.project.title

