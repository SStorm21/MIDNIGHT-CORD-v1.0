from customtkinter import *
from PIL import Image
import time
import pyautogui
import pyperclip
import requests

def defalut(): 
    hyper   = check.get()
    message = entry1.get()
    pyperclip.copy(message)
    time.sleep(1)
    if hyper ==0:
        time.sleep(1)
        pyautogui.write(message,interval=0.020)
        pyautogui.hotkey('enter',interval=1)#send
        pyautogui.hotkey('tab') #delete
        pyautogui.hotkey('up')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('delete','enter')
        pyautogui.hotkey('down','enter')
    else:
        pass
    if hyper ==1:
        fast=0.4
        time.sleep(fast)
        pyautogui.write(message,interval=0.002)
        pyautogui.hotkey('enter',interval=fast)#send
        pyautogui.hotkey('tab') #delete
        pyautogui.hotkey('up')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('delete','enter')
        pyautogui.hotkey('down','enter')
    else:
        pass
def wait():               # - wait    
    def kill():
        ask.destroy()
        root.destroy()
        quit()
    def kill1():
        ask.destroy()
        root.state('normal')
    root.state('withdrawn')
    ask = CTk()
    ask.geometry("227x152+800+350"),ask.resizable(0,0),ask.configure(fg_color="black"),ask.title("Exit"),ask.iconbitmap('logo-icon.ico')
    frame = CTkFrame(ask,fg_color="black",border_width=2,border_color="blue",bg_color="black")
    frame.pack(fill=X,expand=1)
    label = CTkLabel(frame,text="Wait..")
    label.place(x=15,y=25)
    label2 = CTkLabel(frame,text="Are You Sure u want to exit?")
    label2.place(x=25,y=50)
    label2 = CTkLabel(frame,text_color="blue",font=('Aptos',12,"bold"),text="_______________________________")
    label2.place(x=4,y=85)    
    button = CTkButton(frame,text=" yes ",command=kill,width=10,hover_color="darkred",text_color="red",fg_color="black",border_width=2,border_color="red")
    button.place(x=25,y=115)
    button = CTkButton(frame,text="  no  ",command=kill1,width=10,hover_color="darkgreen",text_color="lime",fg_color="black",border_width=2,border_color="lime")
    button.place(x=80,y=115)
    ask.mainloop()
def settings():
    def troubleshoot():
        os.system("pip uninstall pyautogui -y")
        os.system("pip install pyautogui")
        os.system("pip uninstall tk -y")
        os.system("pip install tk")
        os.system("pip uninstall customtkinter -y")
        os.system("pip install customtkinter")
        def org():
            button.configure(text="   troubleshoot   ",text_color="blue")
        button.configure(text="       Done       ",text_color="lime")
        button.after(2000,org)

    window = CTk()
    window.geometry("280x100+700+300"),window.resizable(0,0),window.title("settings"),window.iconbitmap('logo-icon.ico')
    frame = CTkFrame(window,fg_color="black",corner_radius=3,bg_color="black",border_width=1,border_color="blue")
    frame.pack(expand=TRUE,fill=BOTH)
    button = CTkButton(frame,command=troubleshoot,text="   troubleshoot   ",width=10,hover_color="lime",text_color="blue",fg_color="black",border_width=2,border_color="blue")
    button.place(x=91,y=20)
    label = CTkLabel(frame,font=('Aptos',10,"bold"),text="StormTools\nMIDNIGHT2024\nInsta:6._g Discord:.6_g YouTube: @storm01138",text_color="blue")
    label.place(x=28,y=60)
    window.mainloop()
def AutoDelete():
    global is_on
    def start():
        time2delete = combo.get()
        if time2delete == "5 -sec":
            time2delete=5
        else:time2delete == "3 -sec"
        time2delete=3
        if time2delete == "2 -sec":
            time2delete=2 
        else:
            pass         
        print(time2delete)
        time.sleep(time2delete)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('up')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('delete','enter')
        pyautogui.hotkey('down','enter')
    if is_on:
        button = CTkButton(label,command=start,hover_color="darkblue",text_color="blue",text="Start",width=20,height=10,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=5)
        button.place(x=393,y=85)
        vals = ["5 -sec","3 -sec","2 -sec"]
        combo = CTkComboBox(label,font=('Helvetica',12),button_hover_color="darkblue",button_color="blue",values=vals,text_color="darkblue",width=90,text_color_disabled="red",height=12,fg_color="black",bg_color="black",border_width=2,border_color="blue",corner_radius=12,dropdown_text_color="white",dropdown_hover_color="blue",dropdown_fg_color='darkblue')
        combo.place(x=210,y=85)
        label2= CTkLabel(label,font=('Helvetica',12),text_color="blue",text="set timer",fg_color="black",bg_color="black")
        label2.place(x=150,y=82) 
        is_on = False
    else:
        label2= CTkLabel(label,font=('Helvetica',0),text_color="black",width=300,fg_color="black",bg_color="black")
        label2.place(x=150,y=82) 
        is_on = True

    pass
def bulk():
    def D():
        label2.configure(text=" ")
        slider.configure(label,width=-100,button_color="black")
        button3.configure(command=bulk,text_color="blue")
        button.configure(border_color="black",text_color="black")
    def bulking():
        times = slider.get()
        label2.configure(text="    1                                                                       "+str(times)+" ")
        time.sleep(2)
        for x in range(int(times)): 
            print("deleted!"+str(x))
            time.sleep(1)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('up')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('delete','enter')
            pyautogui.hotkey('down','enter')
    
    button = CTkButton(label,command=bulking,hover_color="darkblue",text_color="blue",text="Start",width=20,height=10,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=5)
    label2 = CTkLabel(label,text_color="blue",text="    1                                                                       100 ")
    slider = CTkSlider(label, from_=0, to=101,progress_color="lime",button_hover_color="darkblue",button_corner_radius=12,button_color="blue",border_width=2,corner_radius=25,border_color="blue",fg_color="black")
    #packs-places
    button3.configure(command=D,text_color="lime")
    button.place(x=393,y=132)
    label2.place(x=130,y=125) 
    slider.place(x=155,y=132)

is_on = True
root = CTk()
root.geometry("460x330+700+300"),root.configure(bg_color="black"),root.resizable(0,0),root.title("MIDNIGHT-Beta 1.0"),root.iconbitmap('logo-icon.ico')
root.protocol("WM_DELETE_WINDOW", wait )
image = CTkImage(light_image=Image.open('logo.png'),size=(368,95))
labelmg =CTkLabel(root,image=image,bg_color="black",text=" ")
labelmg.pack(fill=X)
frame = CTkFrame(root,fg_color="black",bg_color="black")
frame.pack(expand=TRUE,fill=BOTH)

tabview = CTkTabview(frame,bg_color="black",
                     fg_color="blue",
                     segmented_button_fg_color="black",
                     segmented_button_unselected_color="black",
                     segmented_button_selected_color="blue",
                     text_color="white",
                     segmented_button_selected_hover_color="blue",
                     segmented_button_unselected_hover_color="darkblue")
tabview.add("Automate")
#AUTOMATED
label = CTkFrame(tabview.tab("Automate"),height=200,fg_color="black",bg_color="black")
entry1 = CTkEntry(label,text_color="darkblue",placeholder_text_color="blue",placeholder_text="Type message . . .",width=260,height=50,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=16)
check = CTkCheckBox(label,hover_color='darkblue',checkmark_color="lime",text_color="blue",text="hyper",fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=20)
button2 = CTkButton(label,command=defalut,hover_color="darkblue",text_color="blue",text="Send",width=20,height=40,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=16)
button5 = CTkButton(root,hover_color="darkblue",command=settings,text_color="blue",text="settings",width=23,height=21,fg_color="black",bg_color="black",border_width=2,border_color="blue",corner_radius=5)
switch_var = StringVar(value="off")
switch = CTkSwitch(label,border_width=1,border_color="blue",command=AutoDelete,variable=switch_var,button_hover_color="darkblue" ,onvalue="on", offvalue="off",font=('Helvetica',12),text="Auto Delete",text_color="blue",progress_color="lime",corner_radius=12,fg_color="black",button_color="blue")
button3 = CTkButton(label,hover_color="darkblue",text_color="blue",command=bulk,text="Bulk",width=100,height=25,fg_color="black",bg_color="black",border_width=2,border_color="blue",corner_radius=5)
#button4 = CTkButton(label,hover_color="darkblue",text_color="blue",text="Delete Last Message",width=100,height=25,fg_color="black",bg_color="black",border_width=2,border_color="blue",corner_radius=5)
#packs-places(AUTOMATED)    
entry1.place(x=20,y=20)
check.place(x=300,y=30)
button2.place(x=380,y=23)
button5.place(x=400,y=2)
switch.place(x=25,y=85)
button3.place(x=25,y=130)
#button4.place(x=25,y=150)
tabview.pack(expand=TRUE,fill=BOTH)
label.pack(fill=X,side=BOTTOM)

#API
def START():
    token = entry2.get()
    channel_id = entry3.get()
    message =  entry4.get()

    message = str(message)
    send_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    payload = {
        'content': message}
    headers = {
        'Authorization': token
    }    
    if token =='':
        def org():
            entry2.configure(placeholder_text="Token",placeholder_text_color="blue",text_color="blue")
        entry2.configure(placeholder_text="INSERT TOKEN",placeholder_text_color="red",text_color='red')
        entry2.after(3000,org)
    else:
        pass    
    if channel_id =='':
        def org():
            entry3.configure(placeholder_text="channel ID",placeholder_text_color="blue",text_color="blue")
        entry3.configure(placeholder_text="INSERT CHANNEL ID",placeholder_text_color="red",text_color='red')
        entry3.after(3000,org) 
    else:
        pass
    if message =='':
        def org():
            entry4.configure(placeholder_text="message",placeholder_text_color="blue",text_color="blue")
        entry4.configure(placeholder_text="INSERT MESSAGE",placeholder_text_color="red",text_color='red')
        entry4.after(3000,org) 
    else:
        pass
    response = requests.post(send_message_url, json=payload, headers=headers)

    if response.status_code == 200:

            def org():
                button__3.configure(text_color='blue',text="send")
            button__3.configure(text_color='lime',text="sent!")
            button__3.after(3000,org)

            message_id = response.json()['id']
            
            delete_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
            
            response_delete = requests.delete(delete_message_url, headers=headers)
            
            if response_delete.status_code == 204:
                    def org():
                        button__3.configure(text_color='blue',text="send")
                    button__3.configure(text_color='red',text="Deleted!")
                    button__3.after(3000,org)
            else:  
                def error1():   
                    def QUIT():
                        error.destroy()
                        root.state('normal')
                    error = CTk()
                    error.geometry("400x152+800+350"),error.resizable(0,0),error.configure(fg_color="black"),error.title("ERROR!"),error.iconbitmap('logo-icon.ico')
                    frame = CTkFrame(error,fg_color="black",border_width=2,border_color="darkred",bg_color="black")
                    frame.pack(fill=X,expand=1)
                    label = CTkLabel(frame,text_color="red",text="ERROR")
                    label.place(x=15,y=25)
                    label6 = CTkLabel(frame,font=('Helvetica',10,'bold'),text_color="red",text="_________________________________________________________________")
                    label6.place(x=5,y=90)
                    label2 = CTkLabel(frame,text_color="red",text="Failed to Delete Message!")
                    label2.place(x=25,y=45)
                    LABEL3 = CTkLabel(frame,font=('Helvetica',13),text_color="red",text=response_delete.text)
                    LABEL3.place(x=20,y=70) 
                    button = CTkButton(frame,text="  ok  ",command=QUIT,width=10,hover_color="darkblue",text_color="blue",fg_color="black",border_width=2,border_color="blue")
                    button.place(x=240,y=115)
                    error.mainloop()
                error1()
    else: 
            def error2():   
                def QUIT():
                    error.destroy()
                    root.state('normal')
                error = CTk()
                error.geometry("400x152+800+350"),error.resizable(0,0),error.configure(fg_color="black"),error.title("ERROR!"),error.iconbitmap('logo-icon.ico')
                frame = CTkFrame(error,fg_color="black",border_width=2,border_color="darkred",bg_color="black")
                frame.pack(fill=X,expand=1)
                label = CTkLabel(frame,text_color="red",text="ERROR")
                label.place(x=15,y=25)
                label6 = CTkLabel(frame,font=('Helvetica',10,'bold'),text_color="red",text="_________________________________________________________________")
                label6.place(x=5,y=90)
                label2 = CTkLabel(frame,text_color="red",text="Failed to send message!")
                label2.place(x=25,y=45)
                LABEL3 = CTkLabel(frame,font=('Helvetica',13),text_color="red",text=response.text)
                LABEL3.place(x=20,y=70) 
                button = CTkButton(frame,text="  ok  ",command=QUIT,width=10,hover_color="darkblue",text_color="blue",fg_color="black",border_width=2,border_color="blue")
                button.place(x=300,y=115)
                error.mainloop()
            error2()
            
def hide():
    entry2.configure(show=TRUE)

tabview.add("API")
label2 = CTkFrame(tabview.tab("API"),height=200,fg_color="black",bg_color="black")

entry2 = CTkEntry(label2,justify=CENTER,text_color="white",placeholder_text_color="blue",placeholder_text="Token",width=390,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=5)
entry3 = CTkEntry(label2,justify=CENTER,text_color="blue",placeholder_text_color="blue",placeholder_text="channel ID",width=420,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=5)
entry4 = CTkEntry(label2,justify=CENTER,text_color="blue",placeholder_text_color="blue",placeholder_text="message",width=420,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=5)

button__ = CTkButton(label2,hover_color="darkblue",command=hide,text_color="blue",text="hide",width=10,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=2)
#button__2 = CTkButton(label2,hover_color="darkblue",text_color="blue",text="info",width=10,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=2)
button__3 = CTkButton(label2,hover_color="darkblue",text_color="blue",text="send",width=50,height=30,fg_color="black",bg_color="black",border_width=1,border_color="blue",corner_radius=2,command=START)
#packs-places(API)
entry2.place(x=15,y=20)
entry3.place(x=15,y=60)
entry4.place(x=15,y=100)
button__.place(x=400,y=20)
#button__2.place(x=400,y=60)
button__3.place(x=380,y=140)
label2.pack(fill=X,side=BOTTOM)

root.mainloop()