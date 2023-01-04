n=int(input())
total=0
start_time=[]
end_time=[]
profit=[]
job=1

for i in range (0,n):
    s=int(input())
    start_time.append(s)
    e=int(input())
    end_time.append(e)
    x=int(input())
    profit.append(x)
    total+=x
max=max(profit)
for i in range(0,n):
    for j in range(i+1,n):
        if(end_time[i]<start_time[j]):
            job+=1
            max+=profit[j]

rem=total-max
task=n-job
print("The number of tasks and earnings available for others")
print(task)
print(rem)
