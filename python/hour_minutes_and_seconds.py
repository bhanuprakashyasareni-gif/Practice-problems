sec = int(input("Enter the seconds : "))

if sec < 60 :
    print(abs(sec))
else:
    print(f"hours : {abs(sec/3600)}")
    print(f"minates : {abs(sec/60)}")
