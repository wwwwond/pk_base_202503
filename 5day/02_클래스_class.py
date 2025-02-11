#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


### 클래스
# - 클래스 이름은 대문자로 시작합니다.
# - 변수를 멤버 변수, 함수를 멤버 함수라고 칭합니다.
# - 함수를 정의할 때, 매개변수에는 무조건 self라는 단어를 처음에 제시해야합니다.
#  -- self는 클래스 내에서 전역변수로 사용하겠다는 의미를 가집니다.
#  -- self로 정의된 변수들은 모두 외부에서 접근이 가능합니다.
class Math : 
    ### 리스트 변수
    list_temp = []

    ### 리스트에 데이터 추가하는 함수 정의 
    def setAppendList(self, p_list,p_name) :
        p_list.append(p_name)

    ### 여러개의 문자열을 튜플 타입으로 반환
    def getTuple(self, *string) :
        return string

    ### 여러개의 key = value를 딕셔너리 타입을 반환
    def getDict(self, **info) :
        return info


# In[12]:


### class는 호출이 아닌 생성한다
# - 생성과 동시에 메모리가 만들어 집니다.

### 클래스 생성하기
math = Math()
a = math.setAppendList(math.list_temp,
                   math.getDict(name = "홍길동", age = 11, area = "부산"))

math.list_temp
# <__main__.Math at 0x264374ae6a0> == 클래스의 주소


# In[9]:


math.list_temp


# In[13]:


class Math : 
    ### 리스트 변수
    list_temp = [] ## 클래스 안에 있음 - 클래스 안에서 사용 가능 

    ### 리스트에 데이터 추가하는 함수 정의 
    def setAppendList(self, p_name) :    
        self.list_temp.append(p_name)   # self. 은 접근 가능한 리스트 템프와 셋어펜드리스트가 나옴

    ### 여러개의 문자열을 튜플 타입으로 반환
    def getTuple(self, *string) :
        return string

    ### 여러개의 key = value를 딕셔너리 타입을 반환
    def getDict(self, **info) :
        return info


# In[15]:


math1 = Math()
math1.setAppendList(math1.getDict(name = "홍길동", age = 11, area = "부산"))

math1.list_temp


# In[23]:


class Math : 
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


# In[24]:


### 클래스 생성하기
math2 = Math()
math2.setDict_AppList(name = "홍길동", age = 11, area = "부산")
math2.list_temp


# In[32]:


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


# In[33]:


### 클래스 생성하기
math3 = Math()
math3.setDict_AppList(name = "홍길동", age = 11, area = "부산")
math3.list_temp


# In[34]:


### 클래스 생성하기
math4 = Math(name = "홍길동", age = 11, area = "부산")
math4.setDict_AppList()
math4.list_temp


# #### 외부 모듈(라이브러리) 불러들이기

# In[3]:


### 외부의 .py 파일 불러들이기
# - 모듈 불러들이기 : import
# - 커널 리스타트 한 후 아래 진행
import math_class


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




