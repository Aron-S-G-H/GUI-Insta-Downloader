# Programmer = Arone Sadegh

# Import the required Libraries and Mudules
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import instaloader
import requests
import threading
import os


# created a tkinter gui window frame
root = Tk()
# Define the geometry 
root.geometry('600x600')
root.resizable(False,False)
# Set the title of tkinter frame 
root.title('Instagram Downloader')
# Set the background of tkinter frame 
root.config(background='grey')


# function for downloading User profile picture 
def download_profile():
    def download_image():
        # Function to check the internet connection
        def connection(url='http://www.google.com/', timeout=5):
            try:
                req = requests.get(url, timeout=timeout)
                req.raise_for_status()
                return True
            except requests.HTTPError as error:
                messagebox.showerror('Error',f'Checking Internet Connection Failed, Status Code: {error.response.status_code}')
            except requests.ConnectionError:
                messagebox.showerror('Error','No Internet Connection Available.')
            return False
        if connection()==True:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                # Start download Profile Picture 
                obj=instaloader.Instaloader()
                profile=profile_pic_input.get()
                obj.download_profile(profile,profile_pic_only=True)
                messagebox.showinfo('Status','Profile Image Downloaded Successfully')
            except:
                messagebox.showerror('Error','Username Is Incorrect or Does Not Exist')
    # thread is a separate flow of execution. This means that our program will have two things happening at once
    threading.Thread(target=download_image).start()


# Function for downloadin video or image by URL 
def download_post():
    # Get url from user by GUI input (Entry)
    link = post_input.get()
    def media():
        if 'https://www.instagram.com/p/' in link:
            try :
                # Function to check the internet connection
                def connection(url='http://www.google.com/', timeout=5):
                    try:
                        req = requests.get(url, timeout=timeout)
                        req.raise_for_status()
                        return True
                    except requests.HTTPError as error:
                        messagebox.showerror('Error',f'Checking Internet Connection Failed, Status Code: {error.response.status_code}')
                    except requests.ConnectionError:
                        messagebox.showerror('Error','No Internet Connection Available.')
                        return False
                if connection()==True:
                    location = filedialog.askdirectory()
                    os.chdir(location)                    
                    short_link = link.replace('https://www.instagram.com/p/','').replace('/','')
                    L = instaloader.Instaloader()
                    post = instaloader.Post.from_shortcode(L.context,short_link)
                    L.download_post(post,target=short_link)
                    messagebox.showinfo('Status','Download Completed !')
            except:
                messagebox.showerror('Error','URL Is Incorrect')
        else :
            messagebox.showerror('Error','URL Not Found')
    # thread is a separate flow of execution. This means that our program will have two things happening at once
    threading.Thread(target=media).start() 
    


# Load an image
load_img=Image.open("C:\\Users\\user\\Desktop\\Py-Work\\Insta-Downloader\\img\\image.jpg")
# Resize the image using resize method
resize_img=load_img.resize((150,150),Image.ANTIALIAS)
# Create an object of tkinter ImageTk and pass the resized image to it
img=ImageTk.PhotoImage(resize_img)
# Create a Label Widget to display the Image
label_img = ttk.Label(root, image = img)
label_img.place(x=30,y=20)


# Create a Label Widget to display the text next to the img
label_img_text=Label(root,text='Instagram',bg='grey',fg='white',font=('Calibri',50,'bold'))
label_img_text.place(x=230,y=45)
# Creat a Label Widget to display the hint text 
hint_text=Label(root,text='* Enter the Username of your desired account in below to download profile picture *',bg='grey',fg='yellow',font=('Calibri',10))
hint_text.place(x=60,y=220)
hint_text2=Label(root,text='* Enter the URL of your desire Image/Video from instagram in below to download it *',bg='grey',fg='yellow',font=('Calibri',10))
hint_text2.place(x=65,y=360)


# Add some Labels to our App
my_name = Label(root,text="Arone Sadegh",bg="grey",fg='yellow',font=('Calibri',10))
my_name.place(x=0,y=580)
github = Label(root,text='Github : Arone-S-G-H',bg='grey',fg='yellow',font=('Calibri',10))
github.place(x=250,y=580)
linkdin = Label(root,text='Linkdin : Arone Sadegh',bg='grey',fg='yellow',font=('Calibri',10))
linkdin.place(x=470,y=580)


# Set the current value of the input with a StringVar object 
Current_value=StringVar()
# Set input to receive username and download the profile picture
profile_pic_input = ttk.Entry(root,textvariable=Current_value,width=35)
# the Entry widget has focus, it’s ready to accept the user input
profile_pic_input.focus()
profile_pic_input.place(x=190,y=260)

# Set the current value of the input with a StringVar object 
Current_value2=StringVar()
# Set input to recieve instagram image or video URL 
post_input = ttk.Entry(root,textvariable=Current_value2,width=35)
# the Entry widget has focus, it’s ready to accept the user input
post_input.focus()
post_input.place(x=190,y=400)



# Create style Object
style_button=ttk.Style()
# configure style, and naming that , style TButtton is used for ttk.button
style_button.configure('TButton',font=('calibri',10,'bold',UNDERLINE),foreground='red')
button1=ttk.Button(root,text='Download',style='TButton',command=download_profile)
button1.place(x=260,y=300)
button1=ttk.Button(root,text='Download',style='TButton',command=download_post)
button1.place(x=260,y=440)
button2=ttk.Button(root,text='Exit',style='TButton',command=root.destroy)
button2.place(x=260,y=500)
# Start the GUI fram of our app 
root.mainloop()