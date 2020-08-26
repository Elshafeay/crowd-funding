# signals and functions
from math import floor

from projects.utils import get_total_donations


def update_project_rate(sender, **kwargs):
	review = kwargs.get('instance')
	if review.rate:
		project = review.project
		reviews = project.review_set.filter(rate__gt=0)
		rates = [_.rate for _ in reviews]
		average = sum(rates) / len(rates)
		average = round(average, 1)  # to round to 1 decimal place
		project.rate = floor(average * 2) / 2
		project.save()


def update_project_status(sender, **kwargs):
	if kwargs.get('created', False):
		donation = kwargs.get('instance')
		project = donation.project
		if get_total_donations(project) > project.target:
			project.status = 1
			project.save()
