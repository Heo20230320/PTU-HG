# for문 활용
# 하나씩 꺼내면서 반복 작업을 수행

mixed = [1, "hello", 3.14, True]


# 기본 리스트 반복문
# for i in mixed:     # i => 변수 이름 자유롭게
#     print(i)
    
# # 1
# hello
# 3.14
# True
    
    
# enumerate 사용하기
for index, item in enumerate(mixed):
    # print(item)
    # print(index)
    print(f"index : {index}, item : {item}")