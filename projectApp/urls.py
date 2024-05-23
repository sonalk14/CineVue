from django.urls import path
from.import views
from.views import Specific

urlpatterns = [
    path('',views.base),
    
    path("Specific/<int:pk>",Specific.as_view(),name="Specific"),
    path("moviesDisplay/",views.moviesDisplay,name="moviesDisplay"),
    path("search/",views.search,name="search"),
    path("searchM/",views.searchM,name="searchM"),
    path("addWishlist/<int:movie_id>",views.addWishlist,name="addWishlist"),
    path("viewWishlist/",views.viewWishlist,name="viewWishlist"),
    path("deleteWishlist/<int:item_id>",views.deleteWishlist,name="deleteWishlist"),
    path("wish/",views.wish,name="wish"),
    path("register/",views.register,name="register"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("sub/",views.sub,name="sub"),
    path("sendMail/",views.sendMail,name="sendMail"),
    path("buy/<int:prod_id>",views.buy,name="buy"),
    path("horror",views.horror,name="horror"),
    path("comedy",views.comedy,name="comedy"),
    path("adventure",views.adventure,name="adventure")
    
    
    
]
