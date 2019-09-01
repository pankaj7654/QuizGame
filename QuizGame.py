question=["1.who is the priminister of india ?","2.who is the chif minister of bihar ?","3.national animal of india ?","4.what is capital of bihar ?","5.what is capital of india ?","6.first president of india ?"]
answer=["Narendra Modi","Nitish Kumar","Lion","Patna","New Delhi","Rajendra Prasad"]
right=0
wrong=0
for i in range(0,6):
    print('\n')
    print(question[i])
    print("input your answer=")
    guess=input()
    guess=guess.title()
    if guess==answer[i]:
        right=right+1
        print('right..next')
    else:
        guess!=answer[i]
        print('wrong!..right answer=',answer[i])
        wrong=wrong+1
print('\n')
print('total attempt question=',i+1)
print('your right count=',right,'congrates')
print('your wrong count=',wrong,'so sad')
print('thank you for plaing game...try again')
    
