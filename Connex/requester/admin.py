from django.contrib import admin
from requester.models import Requester, Challenge, Category, Comment, Dates

class RequesterAdmin(admin.ModelAdmin):
    list_display = ('username', 'company', 'email_address')
    list_filter = ('company', 'email_address', 'telephone')
    search_fields = ('username', 'company')

admin.site.register(Requester, RequesterAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('author', 'status', 'title', 'closing')
    list_filter = ('title', 'status', 'author', 'closing')
    search_fields = ('title', 'author')

admin.site.register(Challenge, ChallengeAdmin)

admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('by', 'created_at', 'challenge', 'options', 'comment')
    list_filter = ('created_at', 'options', 'by', 'comment', 'challenge')
    search_fields = ('challenge', 'by')

admin.site.register(Comment, CommentAdmin)

class DatesAdmin(admin.ModelAdmin):
    list_display = ('challenge', 'entry', 'entry_validation', 'scoring', 'faciliated_judging', 'announce_finalists', 'presentation', 'winners_announcement')
    list_filter = ('entry', 'scoring', 'announce_finalists', 'winners_announcement')
    search_fields = ('entry', 'winners_announcement')

admin.site.register(Dates, DatesAdmin)