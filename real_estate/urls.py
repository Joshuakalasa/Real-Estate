


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views
from accounts.views import (
    registerPage,
    loginPage
)
from listings.views import (
        listing_list,
        listing_retrieve, 
        listing_create,
        listing_update,
        listing_delete
       )

#listing_list is a *view*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list, name="listings"), #'' are empty coz they will be a alanding view
    path('listings/<pk>/', listing_retrieve),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete),
    path('add-listing/',  listing_create),
    
    
    # this is for account
    #path('', include('accounts.urls')),
      
    path('accounts/register/',  views.registerPage, name='register'),
    path('accounts/login/',  views.loginPage, name='login' ),
    path('accounts/logout/',  views.logoutUser, name='logout' ),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from .views import RegisterAPI
from django.urls import path


    
