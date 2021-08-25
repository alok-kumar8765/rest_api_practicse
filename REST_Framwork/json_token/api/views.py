
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
'''
super user-super
      pass-super
user's user-user1
       pass- admin@123

json token db me koi token store nhi krta, user apne username pass se generate krata hai,
jo 5 min default time tak accessable hai, 
terminal pe type kre:- http POST http://127.0.0.1:8000/gettoken/ username="super" password="super"
to check wethere working:- http POST http://127.0.0.1:8000/verifytoken/ token="jo token gen ho wo quotes ke andar" 
token ke sath ek refresh yoken bhi gen hota h, jb token timeout ho jae to ya to 
fir naya token gem kr skte h ya, refresh wale ki help se ek aur gen kr skte h.

refresh token 1 day valid hota.

new access token with refresh token help:-http POST http://127.0.0.1:8000/refreshtoken/ refresh="jo token gen ho wo quotes ke andar"

ye to token ki bat thi, ab api acess krne ke liye:-
http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer acess_token_jo_gen_hoa'
POST:- http -f POST http://127.0.0.1:8000/studentapi/ name=luck roll=8 city=nagpur 'Authorization:Bearer access_key'
PUT :- http PUT http://127.0.0.1:8000/studentapi/3/ name=luck roll=8 city=nagpur 'Authorization:Bearer access_key'
DELETE :- http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Bearer access_key'
'''   