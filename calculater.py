import tkinter as tk
root = tk.Tk()

text = "0"

def add_txt(val):
    global text
    num = ['1','2','3','4','5','6','7','8','9','0']
    opps = ['+','-','*','/']

    if val == '.'and text == '0':
        text = text + val
    elif val in num and text == "0":
        text = val
    elif val == '.' and text[-1] in num:
        text = text + val
    elif val in num and text[-1] in num:
        text = text + val
    elif val in opps and (text[-1] in num and text != '0'):
        text = text + val
    elif val in num and text[-1] == '.':
        text = text + val
    elif val in num and text[-1] in opps:
        text = text + val	
    
    label = tk.Label(root,text = text).grid(row = 0,column = 4)
    root.update()

def print_txt():
    global text
    print(text)

def calculate():
    global text
    val = ''
    for i in range(0,len(text)-1):
        val = val + text[i]
        if text[i+1] in ['+','-','*','/']:
            val = val + ' '
        if val[-1] in ['+','-','*','/']:
            val = val + ' '
    val = val + text[-1]
    text = val.split(' ')


    text = cal(text)

    label = tk.Label(root,text = text).grid(row = 0,column = 4)
    root.update()
    

def cal(text):
    try:
        for n in range(len(text)):
            if text[n] == '/':
                text[n-1] = str(float(text[n-1])/float(text[n+1]))
                text.pop(n)
                text.pop(n)
        for n in range(len(text)):
            if text[n] == '*':
                text[n-1] = str(float(text[n-1])*float(text[n+1]))
                text.pop(n)
                text.pop(n)
        for n in range(len(text)):
            if text[n] == '+':
                text[n-1] = str(float(text[n-1])+float(text[n+1]))
                text.pop(n)
                text.pop(n)
        for n in range(len(text)):
            if text[n] == '-':
                text[n-1] = str(float(text[n-1])-float(text[n+1]))
                text.pop(n)
                text.pop(n)
            
    except:
        if len(text) == 1:
            return text
        else:
            return cal(text)


    
label = tk.Label(root,text = text).grid(row = 0,column = 4)
button_1 = tk.Button(root,text="1",command = lambda : add_txt("1")).grid(row = 1, column = 0)
button_2 = tk.Button(root,text="2",command = lambda : add_txt("2")).grid(row = 1, column = 1)
button_3 = tk.Button(root,text="3",command = lambda : add_txt("3")).grid(row = 1, column = 2)
button_4 = tk.Button(root,text="4",command = lambda : add_txt("4")).grid(row = 2, column = 0)
button_5 = tk.Button(root,text="5",command = lambda : add_txt("5")).grid(row = 2, column = 1)
button_6 = tk.Button(root,text="6",command = lambda : add_txt("6")).grid(row = 2, column = 2)
button_7 = tk.Button(root,text="7",command = lambda : add_txt("7")).grid(row = 3, column = 0)
button_8 = tk.Button(root,text="8",command = lambda : add_txt("8")).grid(row = 3, column = 1)
button_9 = tk.Button(root,text="9",command = lambda : add_txt("9")).grid(row = 3, column = 2)
button_0 = tk.Button(root,text="0",command = lambda : add_txt("0")).grid(row = 4, column = 1)
button_point = tk.Button(root,text=".",command = lambda : add_txt(".")).grid(row = 4, column = 0)
button_enter = tk.Button(root,text="Enter",command = lambda : calculate()).grid(row = 4, column = 2)
button_add = tk.Button(root,text="+",command = lambda : add_txt("+")).grid(row = 1, column = 3)
button_substract = tk.Button(root,text="-",command = lambda : add_txt("-")).grid(row = 2, column = 3)
button_multiply = tk.Button(root,text="*",command = lambda : add_txt("*")).grid(row = 3, column = 3)
button_divide = tk.Button(root,text="/",command = lambda : add_txt("/")).grid(row = 4, column = 3)

