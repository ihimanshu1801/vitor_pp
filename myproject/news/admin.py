from django.contrib import admin

from .models import ParentInfograph , AppStatus, InfographCategory,AppSource, Infograph, MasterTopics,Topics,CustomMetaTags, Entity ,GeoPolitical,InfographAssociation,UserType, Users,AuditType ,UserTopic,UserEntity,UserCustomMetaTags,UserGeoPolitical,AssociationType,UserAssociations ,UserAudit,AppSettings


admin.site.register(ParentInfograph)
admin.site.register(AppStatus)
admin.site.register(InfographCategory)
admin.site.register(AppSource)
admin.site.register(Infograph)
admin.site.register(MasterTopics)
admin.site.register(Topics)
admin.site.register(CustomMetaTags)
admin.site.register(Entity)
admin.site.register(GeoPolitical)
#
admin.site.register(InfographAssociation)
admin.site.register(UserType)
admin.site.register(Users)
admin.site.register(AuditType)
admin.site.register(UserTopic)
admin.site.register(UserEntity)
admin.site.register(UserCustomMetaTags)
admin.site.register(UserGeoPolitical)
admin.site.register(AssociationType)
admin.site.register(UserAssociations)
admin.site.register(UserAudit)
admin.site.register(AppSettings)
