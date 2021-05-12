from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
import validators

root = Tk()
root.geometry('900x500')
root.resizable(0,0)
root.title("youtube video downloader")
 


heading=Label(root,text = 'youtube video downloader', font = 'arial 20 bold',fg='brown4')
heading.grid(columnspan=2,pady=4)


direct=''
def openpath():
    global direct
    direct=filedialog.askdirectory()
    if(len(direct) > 1):
        path_error.config(text=direct,fg='green')
    else:
        path_error.config(text='please choose path',fg='red')
        
def downloader():
    option=types.get()
    url=url_enter.get()
    if(len(url)>1):
        url_error.config(text='')
        valid=validators.url(url_enter.get())
        if valid==True:
            url_error.config(text="Url is valid")
            yt = YouTube(url)

            select = StringVar()
            if(option== options[0]):
                select=yt.streams.filter(progressive=True).first()
            
            elif(option== options[1]):
                select=yt.streams.filter(progressive=True,file_extension='mp4').last()
            
            elif(option== options[2]):
                select=yt.streams.filter(only_audio=True).first()

            select.download(direct)

    
            download_msg.config(text='Download Completed Sucessfully')
        else:
            url_error.config(text="Invalid url")
            
     
        
             



url=Label(root,text='Please insert a valid video URL:', font=10)
url.grid(rowspan=2,column=0,pady=5)
entry_url=StringVar()
url_enter= Entry(root,width=80,textvariable=entry_url)
url_enter.grid(row=2,column=1,pady=5,sticky=(N,E))


    
url_error=Label(root,text='error msg',fg='maroon',font=3)
url_error.grid(row=3,column=1)
 



path=Label(root,text='Select The PATH:', font=10)
path.grid(row=4,column=0)
path_holder=Button(root,width=15,text='choose path',bg='RosyBrown1', font=5,command=openpath)
path_holder.grid(rowspan=1,pady=3)



path_error=Label(root,text='Path Location',font=3,fg='RosyBrown4')
path_error.grid(row=5,column=1)

download_type=Label(root,text='Download Type:', font=10)
download_type.grid(row=9,column=0,pady=5)

options=['high quality','low quality','audio']


types=ttk.Combobox(root,values=options,width=25)
types.grid(row=10,column=0)


download_btn=Button(root,text='Download',font='arial 15 bold',bg='RosyBrown1',command=downloader)
download_btn.grid(row=15,column=0,pady=10,padx=10)


download_msg=Label(root,text='Download Message',font=3,fg='dark green')
download_msg.grid(row=15,column=1)



root.mainloop()

