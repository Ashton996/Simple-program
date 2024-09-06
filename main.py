#!/user/bin/env python3
times1=0
number=input("Enter a number:")
while times1<15:
  if int(number) >=10:
    print("Thats a big number!")
    times1+=5
  else:
    print(number)
    times1+=3