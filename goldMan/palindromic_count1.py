def chk_pal(a):
   if len(a)>0:
      if a[::-1]==a:
          return True

def create_sub(a):      

   ptr1=0
   ptr2=1
   count1=0
   while ptr1<len(a)+1 :
      while ptr2<len(a)+1:

         temp=a[ptr1:ptr2:]

         if chk_pal(temp) == True:
            count1=count1+1

         ptr2=ptr2+1

      ptr1=ptr1+1

      ptr2=ptr1

   total= count1

   return total

inpt="aaa"

print(create_sub(inpt))