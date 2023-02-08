class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print('    ', end=' ')
    for v in range(g.SIZE):
        print("{0:^4}".format(name_ary[v]), end=' ')
    print()
    for row in range(g.SIZE):
        print(name_ary[row], end=' ')
        for col in range(g.SIZE):
            print("%5d" % g.graph[row][col], end=' ')
        print()
    print()
    #받은 그래프를 정렬해서 보이게하는 역할을 하는 함수


def find_vertex(g, find_vtx): #그래프 안의 값을 찾는 함수
    stack = []
    visited_ary = []

    current = 0
    stack.append(current)
    visited_ary.append(current) #current 값 초기화후 stack와 visited_ary에 값을 넣는다.

    while (len(stack) != 0): #0이 아닐 경우
        next = None #next에 None 할당
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0: #속도가 0이 아닐 경우
                if vertex in visited_ary: #이미 visted_ary에 값이 있으면 패스
                    pass
                else: #없으면, next에 vertex 값 할당 후 반복문 중지.
                    next = vertex
                    break

        if next != None: #위에서 반복문이 끝나고 next 값이 존재할 경우
            current = next #current에 next 값 할당
            stack.append(current) #아까 받았던 vertex 를 stack와 visited_ary에 추가한다.
            visited_ary.append(current)
        else:
            current = stack.pop() #값이 존재하지 않을 경우 > stack의 마지막 값을 지운 것을 current에 할당한다.

    if find_vtx in visited_ary:
        return True #visited_ary에 find_vtx가 존재할 경우 함수 종료
    else:
        return False #아니면 다시 반복 시작.


G1 = None #G1의 초기값 할당
name_ary = ['서울', '뉴욕', '런던', '북경', '방콕', '파리'] #G1에 색인을 부여하기 위해서 색인값 추가.
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5 #각 도시에 숫자 할당


gSize = 6 #그래프 사이즈 설정
G1 = Graph(gSize)
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][런던] = 30; G1.graph[방콕][북경] = 50; G1.graph[방콕][파리] = 20
G1.graph[파리][런던] = 60; G1.graph[파리][방콕] = 20
#그래프에 각각 가중치 할당



print('## 해저 케이블 연결을 위한 전체 연결도 ##')
print_graph(G1)
#위에서 할당한 가중치를 그대로 출력.

edge_ary = [] #이제부터 가장 빠른 값을 남기기 위한 함수
for i in range(gSize):  #g의 크기만큼 반복
    for k in range(gSize):
        if G1.graph[i][k] != 0: #각각의 색인값이 0이 아니면 아래 실행
            edge_ary.append([G1.graph[i][k], i, k]) #ex.G1.graph[1][1]=20이면 edge_ary에 [20, 1, 1] 할당

from operator import itemgetter #오퍼레이터에 있는 아이템게터 참조

edge_ary = sorted(edge_ary, key=itemgetter(0), reverse=False)
#아까 받은 edge_ary 값을 0번([1][1]=20 이었으니 20,1,1 인 상태에서 값인 '20'을 기준으로 내림차순 정렬
#reverse를 Ture로 하면 오름차순이 된다.
#edge_ary를 정렬한다.

new_ary = [] #new_ary 생성
for i in range(0, len(edge_ary), 2): #0부터 edge_ary의 길이까지 2씩뛰어가면서 세서 그 값을 new_ary에 넣는다.
    new_ary.append(edge_ary[i]) #2씩 뛰어가면서 세는 이유는 (20,2,1) / (20,1,2) / (10,4,3)/(10,3,4) 등 같은 값이 정렬되는데.

index = 0
while (len(new_ary) > gSize - 1): #new_ary값이 gSize -1이 될때까지반복 (20,2,1)로 가정하고 대입
    start = new_ary[index][1] #start에 2
    end = new_ary[index][2] #end에 1
    saveCost = new_ary[index][0] #saveCost에는 20을 할당한다 (복구를 위한 예비용.)

    G1.graph[start][end] = 0 #그리고 g1.graph의 값을 모두 0으로 만든다(가장 높은값만을 남기기위함)
    G1.graph[end][start] = 0

    startYN = find_vertex(G1, start)#그리고 start와 end에 아까 그래프 안의 연결을 찾는 함수를 이용해서 값 추가
    endYN = find_vertex(G1, end) #g1 그래프에 start 값 2와 end 1을 넣은 걸 찾는다 (연결되어있는지를 찾기위함.)

    if startYN and endYN: #만약 두 값모두 연결이 존재한다면 해당 가중치를 지운다.
        del (new_ary[index])
    else:
        G1.graph[start][end] = saveCost #하나라도 연결이 존재하지 않는다면 각각의 2,1 /1,2에 다시 20을 저장한다.
        G1.graph[end][start] = saveCost
        index += 1 #그후 index에 1을 추가하고 g1의 길이-1(정점-1이 최소간선)만큼 반복한다

print('## 가장 효율적인 해저 케이블 연결도 ##')
print_graph(G1) #앞선 함수로 제거된 값을 다시 출력한다.
