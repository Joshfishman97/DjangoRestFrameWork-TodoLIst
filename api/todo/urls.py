from rest_framework import routers
from .views import TodiViewset

router = routers.DefaultRouter()
router.register('todo', TodiViewset)