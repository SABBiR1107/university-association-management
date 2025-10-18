from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=0, help_text="Higher number means higher priority")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-priority', 'name']
    
    def __str__(self):
        return self.name

class Position(models.Model):
    POSITION_PRIORITY = {
        'President': 100,
        'Vice President': 90,
        'General Secretary': 80,
        'Secretary': 80,
        'Joint Secretary': 70,
        'Deputy Secretary': 70,
        'Treasurer': 85,
        'Deputy Treasurer': 75,
        'Office Secretary': 60,
        'Deputy Office Secretary': 50,
        'Management Secretary': 65,
        'Deputy Management Secretary': 55,
        'Event Management Secretary': 40,
        'Organizing Secretary': 35,
        'Deputy Organizing Secretary': 30,
        'Communications Secretary': 45,
        'Deputy Communication Secretary': 35,
        'Public Relations Secretary': 40,
        'Praise and Public Relations Secretary': 40,
        'Deputy Public Relations Secretary': 30,
        'Creative Secretary': 25,
        'Creative Designer': 20,
        'Official Photographer': 15,
        'IT Secretary': 40,
        'Deputy IT Secretary': 30,
        'Cultural Secretary': 35,
        'Deputy Cultural Secretary': 25,
        'Sports Secretary': 30,
        'Women\'s welfare Secretary': 35,
        'Deputy Women\'s welfare Secretary': 25,
    }
    
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='positions')
    hierarchy_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['division__priority', '-hierarchy_order', 'name']
    
    def save(self, *args, **kwargs):
        # Auto-set hierarchy order based on position name
        if not self.hierarchy_order:
            self.hierarchy_order = self.POSITION_PRIORITY.get(self.name, 0)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.division.name}"

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='members')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='members/', blank=True, null=True)
    bio = models.TextField(blank=True)
    academic_year = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['position__division__priority', '-position__hierarchy_order', '-display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position.name}"