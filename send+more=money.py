def solve():
startTime = time.clock()
    for s in range(10):
        for e in range(10):
            if unique([s,e]):
                for n in range(10):
                    if unique([s,e,n]):
                        for d in range(10):
                            list1 = [s,e,n,d]
                            if unique(list1):
                                for m in range(1, 10):
                                    if unique([s,e,n,d,m]):
                                        for o in range(10):
                                            if unique([s,e,n,d,m,o]):
                                                for r in range(10):
                                                    if unique([s,e,n,d,m,o,r]):
                                                        for y in range(10):
                                                            newList = [s, e, n, d, m, o, r, y]
                                                            if unique(newList):
                                                                send = (s*1000)+(e*100)+(n*10)+d
                                                                more = (m*1000)+(o*100)+(r*10)+e
                                                                money = (m*10000)+(o*1000)+(n*100)+(e*10)+y
                                                                if send+more==money:
                                                                    print(send, more, money)
                                                                    print(time.clock()-startTime)
                                                                else:
                                                                    False
                                                            else:
                                                                False
