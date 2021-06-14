x=input()
no_of_tweets=int(x.split(' ')[0])
no_of_ops=int(x.split(' ')[1])
ops=[]
for i in range(no_of_ops):
    x=input()
    ops.append(x)
tweets_state=[]
for i in range(no_of_tweets):
    tweets_state.append(0)
for op in ops:
    if op=="CLICKALL":
        for i in range(len(tweets_state)):
            tweets_state[i]=0
        print(0)
    else:
        op=int(op.split(' ')[1])
        if tweets_state[op-1]==0:
            tweets_state[op-1]=1
        else:
            tweets_state[op-1]=0
        print(tweets_state.count(1))    


