from django.test import TestCase
from models import Model1

test1 = Model1(
    fullname="Abdusamad Abdulakhanov",
    age=18,
    email="pythondeveloper441@gmail.com",
    password="$enterpassword$",
    graduated=False,
    reason="I am python developer, junior developer... I wanna develop my skills that's why!",
    level="junior"
)
test1.save()
