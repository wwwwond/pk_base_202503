#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Math : 
    ### 생성자 함수 정의하기
    # - 외부에서 클래스 생성시에 미리 값을 정의하고자 할 때 넘겨받을 값을 처리함
    def __init__(self, **data) :    ### 생성자 함수 (없어도 호출되는 디폴트 값)
        print("생성자가 호출되었습니다.")
        self.setAppendList(data)
    
    ### 리스트 변수
    list_temp = [] ## 클래스 안에 있음 - 클래스 안에서 사용 가능 

    ### setTuple_AppList()
    # - 딕셔너리 타입을 리스트에 추가하는 함수 정의
    def setDict_AppList(self, **data) :
        self.setAppendList(data)
    
    ### 리스트에 데이터 추가하는 함수 정의 
    def setAppendList(self, p_name) :    
        self.list_temp.append(p_name)   # self. 은 접근 가능한 리스트 템프와 셋어펜드리스트가 나옴

    ### 여러개의 문자열을 튜플 타입으로 반환
    def getTuple(self, *string) :
        return string

    ### 여러개의 key = value를 딕셔너리 타입을 반환
    def getDict(self, **info) :
        return info

