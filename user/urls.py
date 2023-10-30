from django.contrib import admin
from django.urls import path
from .  import views as v

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('',v.index, name='index' ),
    #  path('/insert', v.insert, name='role_insert' ),
    #  path('/roleoutput', v.roleoutput, name='roleoutput' ),
    #  path('edit/<int:id>', v.role_edit, name='edit_role'),
    #  path('/updaterole', v.update, name='role_update'),
    #  path('roleoutput/<int:id>', v.delete_role, name='delete_role'),

]
