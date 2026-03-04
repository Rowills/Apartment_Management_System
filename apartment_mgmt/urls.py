from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UserViewSet
from flats.views import FlatViewSet
from notices.views import NoticeViewSet
from payments.views import FeeInvoiceViewSet, PaymentViewSet
from tickets.views import TicketViewSet
from visitors.views import VisitorLogViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('flats', FlatViewSet, basename='flat')
router.register('tickets', TicketViewSet, basename='ticket')
router.register('visitors', VisitorLogViewSet, basename='visitor')
router.register('notices', NoticeViewSet, basename='notice')
router.register('fee-invoices', FeeInvoiceViewSet, basename='fee-invoice')
router.register('payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
