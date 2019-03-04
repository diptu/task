from django.urls import path , include
from .views import SubscriptionListView, SubscriptionDetailView, JoinVSChannelView

urlpatterns = [
    path('', SubscriptionListView.as_view()),
    path('<pk>', SubscriptionDetailView.as_view()),
    # path('deshboard/join-vs-channel', JoinVSChannelView.as_view({'get': 'list'})),
    path('deshboard/join-vs-channel', JoinVSChannelView.as_view()),

]
