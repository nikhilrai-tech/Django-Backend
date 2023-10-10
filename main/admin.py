from django.contrib import admin
from .models import User, School, Student

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    search_fields = ('username', 'email')
    ordering = ('username',)
    def create_superuser(self, username, email, password, **extra_fields):
        user = super().create_superuser(username, email, password, **extra_fields)
        user.user_type = 'SU'
        user.save()
        return user

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'pin_code')
    search_fields = ('name', 'city')
    ordering = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'grade', 'school')
    search_fields = ('name', 'username')
    ordering = ('name',)

admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
