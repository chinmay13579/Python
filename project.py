from tkinter import*
import tkinter.messagebox as tkMessagebox
import sqlite3
import tkinter.ttk  as ttk

root=Tk()
root.title("python inventory management system")
width=1024
height=720
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"% (width,height,x,y))
rooot.resizeab le(0,0)
root.config(bg="#800000)

USERNAME=StringVar()
PASSWORD=StringVar()
PRODUCT_NAME=StringVar()
PRODUCT_Price=IntVar()
PRODUCT_QTY=IntVar()
SEARCH= StringVar()
            
def Database():
            global conn,cursor
            conn=sqlite3.connect("database.db")
            cursor=conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS 'admin' (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT,password TEXT")
            cursor.execute("CREATE TABLE IF NOT EXISTS 'product'(product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,product_name  TEXT,product_qty TEXT,product_price TEXT")
            cursor.execute("SELECT * FROM 'admin' WHERE 'username'='admin' AND password='admin'")
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO 'admin' (username.password) VALUES('admin,'admin')")
                conn.commit()

            
def Exit():
            result=tkMessageBox.askquestion('Python Inventory Management System','Do you want to Exit ?',icon="warning")
            if result=='yes':
               root.destroy()
               exit()

def Exit2():
            result=tkMessageBox.askquestion('Python Inventory Management System','Do you want to Exit ?',icon="warning")
            if result=='yes':
               Home.destroy()
               exit()
            def ShowLoginForm():
                 global loginform
                 loginform=Toplevel()
                 loginform.title("Python Inventory Management System/Account Login")
                 width=600
                 height=500
                 screen_width=root.winfo_screenwidth()
                 screen_height=root.winfo_screenheight()
                 x=(screen_width/2)-(width/2)
                 y=(screen_height/2)-(height/2)
                 loginfor.resizeable(0,0)
                 loginform.geometry("%dx%d+%d+%d"%(width,height,x,y))
                 LoginForm()
            

      global lbl_result
            TopLoginForm=Frame(loginform,width=600,height=100,bd=1,relief=SOLID)
            TopLoginForm.pack(side=TOP,pady=20)
            lbl_text=Label(TopLoginForm,text="Administrator Login".font=('arial',18),width=600)
            lbl_text.pack(fill=X)
            MidloginForm=Frame(loginform,width=600)
            MidLoginForm.pack(side=Top,pady=50)
            lbl_username=Label(MidLoginForm,text="Username:",font=('arial',25,bd=18)
            lbl_username.grid(row=0)
            lbl_username=Label(MidLoginForm,text="Password:",font=('arial',25,bd=18)
            lbl_password.grid(row=1)
            lbl_result=Label(MidLoginForm,text="",font=('arial',18))
            lbl_result.grid(row=3,columnspan=2)
            username=Entry(MidLoginForm,textvariable=USERNAME,font=('arial',25),width=15)
            username.grid(row=0,ccolumn=1)
            password=Entry(MidLoginForm,textvariable=PASSWORD,font=('arial',25),width=15,show="*")
            password.grid(row=2,column=1)
            btn_login=Button(MidLoginForm,text="Login",font=('arial',25),width=30,command=Login)
            btn_login.grid(row=2,columnspan=2,pady=20)
            btn_login.bind('<Return>',Login)


      def Home():
             global Home
             Home=Tk()
             Home.title("Python Inventory Mnangement System/Home")
             width=1024
             height=720
             x=(screen_width/2)-(width/2)
             y=(screen_height/2)-(height/2)
             Home.geometry("%dx%d+%d+%d"%(width,height,x,y))
             Home.resizeable(0,0)
             Title=Frame(Home,bd=1,relief=SOLID)
             Title.pack(pady=10)
             lbl_display=Label(Title,text="Python Inventory Management System",font=('arial',45))
             lbl_display,pack()
             menubar=Menu(Home)
             filemenu=Menu(menubar,tearoff=0)
             filemenu2=Menu(menubar,tearoff=0)
             filemenu.add_command(label="Logout",command=Logout)
             filemenu2.add_command(label="Exit",command=Exit2)
             filemenu2.add_command(label="Add New",command=ShowAddNew)
             filemenu2.add_command(label="View",command=Showview)
             menubar.add_cascade(label="Account",command=filemenu)
             menubar.add_cascade(label="Inventory",command=filemenu2)
             Home.config(menu=menubar)
             Home.config(bg="#99ff99)

        def ShowAddNew():
                global addnewform
                addnewform=Toplevel()
                addnewform.title("/Add New")
                width=600
                height=500
                screen_width=Home.winfo_screenwidth()
                screen_height=Home.winfo_screenheight()
                x=(screen_width/2)-(width/2)
                y=(screen_height/2)-(height/2)
                addnewform.geometry("%dx%d+%d+%d"%(width,height,x,y)))
                addnewform.resizable(0,0)
                AddNewForm()

        def AddNewForm():
                TopAddNew=Frame(addnewform,width=600,hright=100,bd=1,relief=SOLID)
                TopAddNew.pack(side=TOP,pady=20)
                lbl_text=Label(TopAddNew,text="Add New Product",font=('arial',18),width=600)
                lbl_text.pack(fill=X)
                MidAddNew=Frame(addnewform,width=600)
                MidAddNew.pack(side=TOP,pady=50)
                lbl_productname=Label(MidAddNew,text="Product Name",font=('arial',25),bd=10)
                lbl_productname.grid(row=0,sticky=W)
                bl_qty=Label(MidAddNew,text="Product Quantity",font=('arial',25),bd=10)
                lbl_qty.grid(row=1,sticky=W)
                lbl_price=Label(MidAddNew,text="Product Price",font=('arial',25),bd=10)
                lbl_price.grid(row=1,sticky=W)
                productname=Entry(MidAddNew,textvariable=PRODUCT_NAME,font=('arial',25,width=15))
                productname.grid(row=0,column=0)
                productqty=Entry(MidAddNew,textvariable=PRODUCT_QTY,font=('arial',25,width=15))
                productqty.grid(row=1,column=1)
                
                productprice=Entry(MidAddNew,textvariable=PRODUCT_PRICE,font=('arial',25,width=15))
                productprice.grid(row=2,column=1)
                btn_add=Button(MidAddNew,text="Save",font=('arial',18),width=30,bg="#009ACD",command=AddNew)
                btn_add.grid(row=3,columnspan=2,pady=20)


           def Viewform():
                global tree
                TopViewForm=Frame(viewform,width=600,bd=1,relief=SOLID)
                TopViewForm.pack(side=TOP,fill=X)
                LeftViewForm=Frame(viewform,width=600)
                LeftViewForm.pack(side=LEFT,fill=X)
                MidViewForm=Frame(viewform,width=600)
                MidViewForm.pack(side=RIGHT)
                lbl_text=Label(TopViewForm,text="View Product",font=('arial',18),width=600)
                lbl_text.pack(fill=X)
                lbl_textsearch=Label(LeftViewForm,text="Search",font=('arial',15))
                lbl_textsearch.pack(side=TOP,anchor=W)
                search=Entry(LeftViewForm,textvariable=SEARCH,font=('arial',15),width=10)
                search.pack(side=TOP,padx=10,pady=10,fill=X)
                btn_search=Button(LeftViewForm,text="Search",command=Search)
                btn_search.pack(side=TOP,padx=10,pady=10,fill=X)
                btn_reset=Button(LeftViewForm,text="Reset",command=Search)
                btn_reset.pack(side=TOP,padx=10,pady=10,fill=X)
                btn_delete=Button(LeftViewForm,text="Delete",command=Search)
                btn_delete.pack(side=TOP,padx=10,pady=10,fill=X)
                scrollbarx=Scrollbar(MidViewForm,orient=HORIZONTAL)
                scrollbary=Scrollbar(MidViewForm,orient=VERTICAL)
                tree=ttk.Treeview(MidViewForm,columns=("ProductID","Product Name","Product Qty","Product Price"),selectmode="database",height=100,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT,fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM,fill=X)
                tree.heading('ProductID',text="ProductID",anchor=w)
                tree.heading('Product Name',text="Product Name",anchor=w)
                tree.heading('Product Qty',text="Product Qty",anchor=w)
                tree.heading('Product Price',text="Product Price",anchor=w)
                tree.column('#0',streach=No,minwidth=0,width=0)
                tree.column('#1',streach=No,minwidth=0,width=0)
                tree.column('#2',streach=No,minwidth=0,width=200)
                tree.column('#3',streach=No,minwidth=0,width=120)
                tree.column('#4',streach=No,minwidth=0,width=120)
                tree.pack()
                DisplayData()
                
         def DisplayData():
                Database()
                cursor.execute("SELECT * FROM 'PRODUCT'")
                fetch=cursor.fetchall()
                for data in fetch:
                    tree.insert(''.'end'values=(data))
                cursor.Close()
                conn.Close()

         def Search():
                if SEARCH.get!="":
                    tree.delete(*tree.get_children())
                    Database()
                    cursor.execute("SELECT * FROM 'product' LIKE?",('%'+str(SEARCH.get())+'%',))
                    fetch=cursor.fetchall()
                    for data in fetch:
                        tree.insert('','end',values(data))

                cursor.Close()
                conn.Close()

         def Reset():
                tree.delete(*tree.getch_children())
                DisplayData()
                SEARCH.set("")

          def Delete():
              if nt tree.selection():
                        print("ERROR")
              else:
                    result=tkMessageBox.askquestion('Python Inventory Management System','Do you want to delete this record',icon="warning")
                    if result="Yes":
                            curItem=tree.focus()
                            contents=(tree.item(curItem))
                            selecteditem=contents('values')
                            tree.delete(curItem)
                            Database()
                            cursor.execute("DELETE * FROM 'product' WHERE 'product_id'=%d",selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()

         def ShowView():
                global viewform
                viewform=TopLevel()
                viewform.title("Python Inventory Management System/View Product")
                width=600
                height=400
                screen_width=Home.winfo_screenwidth()
                screen_height==Home.winfo_screenheight()
                x=(screen_width/2)-(width/2)
                y=(screen_height/2)-(height/2)
                viewform.geometry("%dx%d+%d+%d"%(width,height,x,y)))
                viewform.resizeable(0,0)
                ViewForm()
                
                
                
                               

        
                               
                
                
                
                
                
                
                
                               
                               
                
                
                
                         
                         
                         
                               
                               
                    
 
