from __future__ import unicode_literals

from django.db import models


class Program(models.Model):
    CPLUSPLUS = 1
    CSHARP = 2
    PYTHON = 3
    ASPNET = 4
    JAVA = 5
    VBNET = 6
    VB = 7
    CODEBASE = (
        (CPLUSPLUS, 'C++'),
        (CSHARP, 'C#'),
        (PYTHON, 'Python'),
        (ASPNET, 'ASP.NET'),
        (JAVA, 'JAVA'),
        (VBNET, 'VB.NET'),
        (VB, 'VB'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    codebase = models.PositiveSmallIntegerField(choices=CODEBASE, blank=True, null=True)
    last_commit_time = models.DateTimeField(blank=True, null=True)
    last_commit_user = models.CharField(max_length=100, blank=True, null=True)
