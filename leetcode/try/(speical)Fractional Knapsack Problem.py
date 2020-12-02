cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2),
]

# (가치, 무게) => 15kg까지 무게 담을 수 있고, 가치를 최대로 만들려면?. 단, 무게는 '쪼갤' 수 있다.

def fractional_knapsack():
    capacity = 15
    total_value = 0
    _cargo = []
    # 무게는 줄이고, 가치는 높여야. 우선순위는 가치/무게 로 줄 수 있음. (==단가계산)
    for c in cargo:
        _cargo.append([c[0]/c[1],c[0],c[1]])
    _cargo.sort(reverse=True)

    weight=0
    for c in _cargo:
        weight += c[2]
        if weight >capacity:
            # fraction
            subweight = c[2]-(weight - capacity)
            total_value+=c[1]*(subweight/c[2])
            break
        total_value += c[1]
    return total_value

print(fractional_knapsack())

