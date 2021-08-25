from rest_framework.throttling import UserRateThrottle

class SetThrottle(UserRateThrottle):
    scope = 'set'