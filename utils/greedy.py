# greedy
gift_cards=[5, 4, 5, 4, 5]
wants=[1, 2, 3, 5, 4]

n=len(gift_cards)
occupied=[False]*(n+1)
for i in range(n):
    if wants[i]==gift_cards[i]:
        occupied[wants[i]]=True
for i in range(n):
    target=wants[i]
    if not occupied[target]:
        try:
            target_idx=gift_cards.index(target)
        except:
            continue
        if not occupied[target_idx+1]:
            occupied[target]=True
            gift_cards[i],gift_cards[target_idx]=gift_cards[target_idx],gift_cards[i]
ans=0
for i in range(n):
    if gift_cards[i]==wants[i]:
        ans+=1
print(n-ans)
