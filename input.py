import Cats
print(Cats.make_a_list())
user_option_str = input("Please Enter a Number :")
user_option_int = int(user_option_str)
if (user_option_int==1):
    list = Cats.List()
    print(Cats.List())
if (user_option_int==2) :
    print(Cats.Add())
if (user_option_int==3) :
    print(Cats.Update())
if (user_option_int==4) :
    print(Cats.Delete())
if (user_option_int==5) :
    Cats.Exit()
