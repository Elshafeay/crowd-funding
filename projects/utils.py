from collections import Counter

from django.db.models import Sum


def get_the_most_similar_projects(project, tags):
    related_projects = [tag.projecttags_set.all() for tag in tags]
    related_projects = [
        rp.project for sub_query in related_projects for rp in sub_query
    ]
    counts = Counter(related_projects)
    related_projects = counts.most_common(11)
    return [_[0] for _ in related_projects[1:]]


# get total donations for a project
def get_total_donations(project):
    total_donations = project.donation_set.aggregate(
        Sum('donation')).get('donation__sum')
    return total_donations or 0


# get donations for a list of projects
def get_projects_donations(projects):
    donations_percentages = {}
    total_donations = {}
    for project in projects:
        total = get_total_donations(project)
        donations_percentages[project.id] = int((int(total) / project.target) * 100)
        total_donations[project.id] = total
    return donations_percentages, total_donations
