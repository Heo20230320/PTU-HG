# pyfiglet + termcolor를 활용한 텍스트 출력 함수
import pyfiglet
from termcolor import colored               
# 1. 함수 정의(독스트링, 타입힌트, 기본 값 설정)
def print_tuned_colored(sentence:str="Hello", 
                         font:str="slant", 
                         color:str="red", 
                         on_color:str="on_green", 
                         style:list=["bold"]):
    '''
    pyfiglet와 termcolor를 활용하여
    튜닝된 텍스트를 원하는 색상, 배경색, 스타일로 출력하는 함수
    
    매개변수:
    sentence(str) : 출력할 문자열
    font(str) : pyfiglet 폰트 종류
    color(str) : 글자색
    on_color : 배경색
    style : 스타일
    '''
    # 1. 튜닝
    py_sentence = pyfiglet.figlet_format(sentence, font=font)
    
    # 2. 색상
    color_py_sentence = colored(py_sentence, 
                                color, 
                                on_color, 
                                style
                                )
    print(color_py_sentence)
# 2. 함수 호출
print_tuned_colored("Hello, World!", "digital", "cyan", "on_magenta", ["bold", "underline"])
print_tuned_colored("Python is fun!", "bubble", "yellow", "on_blue", ["reverse"])
print_tuned_colored()  # 기본 값으로 호출   