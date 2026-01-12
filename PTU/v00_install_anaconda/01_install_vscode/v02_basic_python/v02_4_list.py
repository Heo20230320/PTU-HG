# 리스트 값 변경과 조작
# 특징 : 순서, 수정, 중복 허용

colors = ["red", "green", "blue"]

# 1. 인덱싱
# print(colors[0])
# print(colors[-1])       # -1은 맨마지막값을 의미


# 2. 슬라이싱
# print(colors[0:2])      # 맨 뒤에서 앞에 것 까지만 불러옴
# print(colors[0:-1])
# print(colors[1:2])
# 주석 처리하다가 안먹을 때는 한/영 -> 한글 입력 상태에서


# 3. 값 변경(수정)
# print(colors[-1]) #blue
colors[-1] = "pupple"
# print(colors[-1]) #pupple


# 4. 값 추가1
colors.append("pink")
# print(colors)


# 5. 값 추가2
# colors.insert(위치, 값)
colors.insert(0, "white")
# print(colors)
# ['white', 'red', 'green', 'pupple', 'pink']


# 6. 값 제거
colors.remove("white")
# print(colors)
# ['red', 'green', 'pupple', 'pink']


numbers = [4, 3, 2, 3, 1, 1, 5]
# 7. 정렬
numbers.sort()  # 오름차순 정렬
# print(numbers)
# [1, 1, 2, 3, 3, 4, 5]
# numbers.sort(reverse=True) 
# print(numbers)

# 8. 뒤집기
numbers.reverse()
# print(numbers)

# 9. 리스트 요소 포함 여부 확인
# print(10 in numbers) #False
print(2 in numbers) #True
