print('hello world')

v1<-c(1,2,3,7,8)
v2<-c(3,6,7,4,2)
c<-v1+v2
c

sv1<-sum(v1)
sv1
mv1<-mean(v1)
mv1
pv1<-prod(v1)
pv1

a<-readline('enter the number:')
a

n<-10
b<-15
res<-paste(n,'x',1:b,'=',n*1:b)
print(res,sep='\n')

year<-as.numeric(readline(prompt = 'enter the year:'))
if(year%%4==0){
  paste(year,'is a leep year')
}else{
  cat(year,'not a leep year')
}

str <- "
ghgjh
ghbj
fhvhbv
kj"

print(str)
cat(str)

num<-as.numeric(readline(prompt = "enter the number:"))

if(num %% 2==0){
  cat(num,"even")
}else{
  cat(num,"odd")
}


#8
n<-as.numeric(readline(prompt = "enter the number:"))

if (n>0){
  print('positive')
}else if (n<0){
  print('negative')
}else{
  print('zero')
}




#9
a<-100
b<-200
m<-max(a,b)
m

#10
s<-as.numeric(readline(prompt = "enter the score of student(0-100):"))
if (s>=90){
  print('O')
}else if(s>=80){
  print('A')
}else if(s>=70){
  print('B')
}else if(s>=60){
  print('C')
}else if(s>=50){
  print('D')
}

#7
num<-as.numeric(readline(prompt = "enter the number:
                         "))
if(num%%2 == 0){
  cat(num,"is an even number")
}else{
  cat(num,"is an odd number")
}

#11
a<-10
n<-as.numeric(readline(prompt = "enter the number:"))
if(a%%n==0){
  cat(a,'is divisible by',n)
}else{
  cat(a,'is not divisible by',n)
}


#12
age<-as.numeric(readline(prompt = "enter the age:")) 
if(age<=12){
  print('child')
}else if(age<=19){
  print('teenager')
}else if(age<=30){
  print('young adults')
}else if(age<=50){
  print('adults')
}else if(age>50){
  print('senior citizen')
}


#13
s1<-readline(prompt = "enter the string:")
s2<-readline(prompt = "enter the substring:")
r<-grep(s2,s1)
r

#while loop question:

#1

i<-1
while(i<11){
  print(i)
  i<-i+1
}

#2

i<-1
sum<-0

while(i<11){
  
  sum<-sum+i
  i<-i+1
  
}
cat('sum of 10 naturel number',sum)

#3
i<-1
sum<-0
while(i<10){
  sum<-sum+(i^3)
  i<-i+1
}
cat('cube of 10 natural number',sum)

#4

i<-1
while(i<=10){
  print(paste(i,'=',i^2))
  i<-i+1
}


#5
n<-as.numeric(readline('enter the number:'))
v<-as.numeric(readline('enter the limits:'))
i<-1
while(i<=v){
  r<-i*n
  print(paste(i,'*',n,'=',r))
  i<-i+1
}


#6
num<-as.numeric(readline('enter the number:'))
fact=1
while(num>0){
  fact<-fact*num
  num<-num-1
}
fact


#7
n<-as.numeric(readline('enter the number:'))
rev<-0
while (n>0){
  rem<-n %% 10
  rev<-rev*10 +rem
  n<-n%/% 10
  print(rev)
}

#8
a<-as.numeric(readline('enter the number:'))
count=0
while (a>0) {
  count+=1
  a=a//10
  paste()
}

p<-sample(1:6,1)
p
q<-runif(1)
q
data<-read.csv

data
library('openxlsx')
install.packages('openxlsx')
search()

data1<-read.xlsx("demo_excel.xlsx")
data1
is.data.frame(data1)
ncol(data1)
nrow(data1)

library('dplyr')
install.packages('dplyr')
fiter_data1<-data1 %>% filter(Id > 6)
fiter_data1
arrange_data1<-arrange(data1,Student.name,Marks)
arrange_data1


sa_data<-filter(data,age>23)
sa_data