# Tomasulo

Tomasulo

command:
使用 Python 3.6,pycharm 書寫,
輸入值:
Q02_input_IQ.in
如: (第1行開始)
F2=F4+F1
F1=F2/F3
F4=F1-F2
F1=F2-F3
執行主程式:
P02_code_Tomasulo.py

執行結果:
執行結果-01.jpg
執行結果-02.jpg
執行結果-03.jpg
執行結果-04.jpg

系統流程：
1.讀擋 ,Q02_input_IQ.in
2.迴圈,根據輸入,要做 +-*/ 哪一種運算 ,填值到 RS, RAT,
3.做 Dispatch

Function:
def Search_RATREG(S_Fx): # 根據輸入參數,尋找輸出 RAT, REG,
def Fill_RAT(RAT_Fx,RSx): # 填 RAT ,
def Search_RSinRAT(RSi): # 尋找 RS 是否在 RAT ,
def Replace_RS(RS_str1,RSv_float): # 將 RSx 以數值取代 ,
def Clear_RS(ADDMULT_RSx,RSx): # 如果 RSx 都是數值, 計算出結果, 並更新 RSx RAT,

程式註解:
在主程式P02_code_Tomasulo.py中,以
#-----------------------------------------------------------
#-註解
#-----------------------------------------------------------
表示註解,

參考:
Lecture8 (上課驗收日：1121) & Project 2
05-Issue example [Computer Arch - Tomasulo]
06-Dispatch [Computer Arch - Tomasulo]
