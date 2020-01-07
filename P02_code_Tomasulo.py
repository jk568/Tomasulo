# coding=UTF-8
import math

# Lecture8 (11/21) & Project 2 ,# 5
# Lecture8 (11/21) & Project 2 ,# 6

Input_1Fx=''
Input_2II=''
Input_3Fx=''
Input_4Xz=''
Input_5Fx=''

RAT_F1=''
RAT_F2=''
RAT_F3=''
RAT_F4=''

REG_F1='3.14'
REG_F2='-1.00'
REG_F3='2.72'
REG_F4='0.71'

ADD_RS1=""
ADD_RS2=""
ADD_RS3=""
MULT_RS4=""
MULT_RS5=""

#RAT_F1_Out=""
#RAT_F2_Out=""
#RAT_F3_Out=""
#RAT_F4_Out=""




# --------------------------------------------------------------------------
# 根據輸入參數,尋找輸出 RAT, REG,
# --------------------------------------------------------------------------
def Search_RATREG(S_Fx):
    #print('^^^sss rat reg>>>')
    global RAT_F1
    global RAT_F2
    global RAT_F3
    global RAT_F4
    global REG_F1
    global REG_F2
    global REG_F3
    global REG_F4

    if S_Fx=='F1':
        if RAT_F1=='':
            return REG_F1
        else:
            return RAT_F1
    elif S_Fx=='F2':
        if RAT_F2=='':
            return REG_F2
        else:
            return RAT_F2
    elif S_Fx=='F3':
        if RAT_F3=='':
            return REG_F3
        else:
            return RAT_F3
    elif S_Fx=='F4':
        if RAT_F4=='':
            return REG_F4
        else:
            return RAT_F4
    #print('^^^sss rat reg<<<')

# --------------------------------------------------------------------------
# 填 RAT ,
# --------------------------------------------------------------------------
def Fill_RAT(RAT_Fx,RSx):
    #print('---fill rat>>>')
    global RAT_F1
    global RAT_F2
    global RAT_F3
    global RAT_F4

    #print(RAT_Fx)
    #print(RSx)
    if RAT_Fx=='F1':
        RAT_F1=RSx
    elif RAT_Fx=='F2':
        RAT_F2=RSx
    elif RAT_Fx=='F3':
        RAT_F3 = RSx
    elif RAT_Fx=='F4':
        RAT_F4 = RSx
    #print('---fill rat<<<')
  
# --------------------------------------------------------------------------  
# 尋找 RS 是否在 RAT ,    
# --------------------------------------------------------------------------      
def Search_RSinRAT(RSi):
    if RAT_F1 == RSi:
        return 1
    elif RAT_F2 == RSi:
        return 2
    elif RAT_F3 == RSi:
        return 3
    elif RAT_F4 == RSi:
        return 4
    else:
        return 0
  
# --------------------------------------------------------------------------  
# 將 RSx 以數值取代 ,        
# --------------------------------------------------------------------------     
def Replace_RS(RS_str1,RSv_float):
    global ADD_RS1
    global ADD_RS2
    global ADD_RS3
    global MULT_RS4
    global MULT_RS5
    str_r = str(RSv_float)
    ADD_RS1 = ADD_RS1.replace(RS_str1, str_r)
    ADD_RS2 = ADD_RS2.replace(RS_str1, str_r)
    ADD_RS3 = ADD_RS3.replace(RS_str1, str_r)
    MULT_RS4 = MULT_RS4.replace(RS_str1, str_r)
    MULT_RS5 = MULT_RS5.replace(RS_str1, str_r)
  
# --------------------------------------------------------------------------  
# 如果 RSx 都是數值, 計算出結果, 並更新 RSx RAT,  
# --------------------------------------------------------------------------      
def Clear_RS(ADDMULT_RSx,RSx):
    global ADD_RS1
    global ADD_RS2
    global ADD_RS3
    global MULT_RS4
    global MULT_RS5
    global RAT_F1
    global RAT_F2
    global RAT_F3
    global RAT_F4

    #if (ADD_RS1.find('RS')) < (0):
    #if (ADD_RSx.find('RS')) < (0):
    str_a=ADDMULT_RSx.split(",")
    A1_s = str_a[1]
    A1 = float(A1_s)
    A2_s = str_a[2]
    A2 = float(A2_s)
    #A3 = A2
    if str_a[0] == "+":
        A3 = (A1 + A2)
    elif str_a[0] == "-":
        A3 = (A1 - A2)
    elif str_a[0] == "*":
        A3 = (A1 * A2)
    elif str_a[0] == "/":
        A3 = (float)(A1 / A2)
    str_b = str(A3)

    Replace_RS(RSx, A3)
    while(Search_RSinRAT(RSx) != 0):
        RAT_iii = Search_RSinRAT(RSx)
        if RAT_iii == 1:
            Fill_RAT("F1", str_b)
        if RAT_iii == 2:
            Fill_RAT("F2", str_b)
        if RAT_iii == 3:
            Fill_RAT("F3", str_b)
        if RAT_iii == 4:
            Fill_RAT("F4", str_b)


    if ADDMULT_RSx == ADD_RS1:
        ADD_RS1=""
    elif ADDMULT_RSx == ADD_RS2:
        ADD_RS2 = ""
    elif ADDMULT_RSx == ADD_RS3:
        ADD_RS3 = ""
    elif ADDMULT_RSx == MULT_RS4:
        MULT_RS4 = ""
    elif ADDMULT_RSx == MULT_RS5:
        MULT_RS5 = ""

if __name__ == "__main__":
    # --------------------------------------------------------------------------
    # 取值 ,
    # --------------------------------------------------------------------------
    f = open('./Q02_input_IQ.in', 'r')
    lines = f.readlines()
    # --------------------------------------------------------------------------
    # 幾行指令迴圈運算 ,
    # --------------------------------------------------------------------------
    for line in lines:
        #num_list = line.split(' ')
        # Write your code here
        print('-----------------------------')
        print(line) # str
        Input_1Fx=line[0:2] # Fx
        Input_2II=line[2]   # =
        Input_3Fx=line[3:5] # Fx
        Input_4Xz=line[5]   # +-*/
        Input_5Fx=line[6:8] # Fx

        #IQ_I=line
        #print(IQ_I)  # list ,[0]=F ,[1]= ,[2]='=',[3]=F ,[4]= ,[5]=+-*/ ,[6]=F ,[7]= ,

        #print(Input_1Fx)
        #print(Input_2II)
        #print(Input_3Fx)
        #print(Input_4Xz)
        #print(Input_5Fx)
        # --------------------------------------------------------------------------
        # 要做 +-*/ 哪一種運算  ,填值到 RS, RAT,
        # --------------------------------------------------------------------------
        if Input_4Xz=='+' or Input_4Xz=='-':
            print('+-')
            if ADD_RS1 == '':
                ADD_RS1=Input_4Xz +','+ Search_RATREG(Input_3Fx) +','+ Search_RATREG(Input_5Fx)
                Fill_RAT(Input_1Fx,'RS1')
            elif ADD_RS2 == '':
                ADD_RS2=Input_4Xz +','+ Search_RATREG(Input_3Fx) +','+ Search_RATREG(Input_5Fx)
                Fill_RAT(Input_1Fx, 'RS2')
            elif ADD_RS3 == '':
                ADD_RS3=Input_4Xz +','+ Search_RATREG(Input_3Fx) +','+ Search_RATREG(Input_5Fx)
                Fill_RAT(Input_1Fx, 'RS3')
        elif Input_4Xz=='*' or Input_4Xz=='/':
            print('*/')
            if MULT_RS4 == '':
                MULT_RS4=Input_4Xz +','+ Search_RATREG(Input_3Fx) +','+ Search_RATREG(Input_5Fx)
                Fill_RAT(Input_1Fx, 'RS4')
            elif MULT_RS5 == '':
                MULT_RS5=Input_4Xz +','+ Search_RATREG(Input_3Fx) +','+ Search_RATREG(Input_5Fx)
                Fill_RAT(Input_1Fx, 'RS5')

        #print('RS1='+ADD_RS1+'  |  '+'RS4='+MULT_RS4)
        #print('RS2='+ADD_RS2+'  |  '+'RS5='+MULT_RS5)
        print('RS1='+ADD_RS1)
        print('RS2='+ADD_RS2)
        print('RS3='+ADD_RS3)
        print('RS4='+MULT_RS4)
        print('RS5='+MULT_RS5)
        print('')
        print('RAT1='+RAT_F1)
        print('RAT2='+RAT_F2)
        print('RAT3='+RAT_F3)
        print('RAT4='+RAT_F4)
    # --------------------------------------------------------------------------
    # Dispatch ,
    # --------------------------------------------------------------------------
    print('=============================')
    print('=============================')
    while ((ADD_RS1 != "") or (ADD_RS2 != "") or (ADD_RS3 != "") or (MULT_RS4 != "") or (MULT_RS5 != "")):
    #if 1:
        if ADD_RS1 != "" and ((ADD_RS1.find('RS')) < (0)) :
            Clear_RS(ADD_RS1,'RS1')
        elif ADD_RS2 != "" and ((ADD_RS2.find('RS')) < (0)) :
            Clear_RS(ADD_RS2,'RS2')
        elif ADD_RS3 != "" and ((ADD_RS3.find('RS')) < (0)) :
            Clear_RS(ADD_RS3,'RS3')
        elif MULT_RS4 != "" and ((MULT_RS4.find('RS')) < (0)) :
            Clear_RS(MULT_RS4,'RS4')
        elif MULT_RS5 != "" and ((MULT_RS5.find('RS')) < (0)) :
            Clear_RS(MULT_RS5,'RS5')

        #print('-')

        print('RS1='+ADD_RS1)
        print('RS2='+ADD_RS2)
        print('RS3='+ADD_RS3)
        print('RS4='+MULT_RS4)
        print('RS5='+MULT_RS5)
        print('')
        print('RAT1='+RAT_F1)
        print('RAT2='+RAT_F2)
        print('RAT3='+RAT_F3)
        print('RAT4='+RAT_F4)

        print('-----------------------------')
    #print(ADD_RS1.find('RS'))
    #print(ADD_RS2.find('RS'))
    print("End")

    f.close()
    print('=============================')
