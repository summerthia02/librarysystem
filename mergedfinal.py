# from appscript import con
import pymysql 
from ast import If
from email import header
from textwrap import fill
from tkinter import *  
import tkinter as tk                
from tkinter import font as tkfont
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk, ImageDraw
import os
from test import *
from mysql import *
from mmap import mmap
import mysql

listMaker = []
# To connect MySQL database
conn = pymysql.connect(
    host='127.0.0.1',
    user='root', 
    password = 'password',
    db='ALibrarySystem',
    )

cur = conn.cursor()
cur.execute("select * from Member")
output = cur.fetchall()
print(output)

#holding membership checker


# Fonts
headerOneFont = ("Lato", 35)
buHeadings = ("Lato 35 underline bold")
headerTwoFont = ("Lato", 28)
headerThreeFont = ("Lato", 24)

def createButtonMain(controller, font, x,y,self):
	createButton = tk.Button(self, text = "Back to Main Menu", font = font,command=lambda: controller.show_frame("HomePage") ).place(x = x, y = y)
	return createButton
 
def createBack(controller, font,x,y,self, prevFrameText, prevFrame):
	createBackButton = tk.Button(self, text = "Back to " + prevFrameText + " Menu", font = font,command=lambda: controller.show_frame(prevFrame) ).place(x = x, y = y)
	return createBackButton

def successFrame(controller, subheading, previousPageText):
	# create a new window 
	newSuccessWindow = Toplevel()
	newSuccessWindow.configure(bg="green")
	newSuccessWindow.title("Success Window")
	newSuccessWindow.geometry("600x600")

	# Success label 
	successLabel = tk.Label(newSuccessWindow, text = "Success!", font=headerOneFont, bg="green").pack(pady=25)
	# successLabel.place(x=260, y=50)

	# Subheading label 
	subheadingLabel = tk.Label(newSuccessWindow, text = subheading, font=headerOneFont,bg="green").pack(pady=25)
	# subheadingLabel.place(x=260, y=100)

	# frame for button border 

	# add button - back to previous function 
	createButton = tk.Button(newSuccessWindow, text = "Back to " + previousPageText + " Function", font = headerThreeFont, command=newSuccessWindow.destroy, bg="green", fg="black").pack(pady=25)
	# textLabel.place(x=260,y=120))

	newSuccessWindow.mainloop()

def errorFrame(controller, subheading, previousPageText):
	# create a new window 
	newErrorWindow = Toplevel()
	newErrorWindow.configure(bg="red")
	newErrorWindow.title("Error Window")
	newErrorWindow.geometry("800x800")

	# Success label 
	errorLabel = tk.Label(newErrorWindow, text = "Error!", font=headerOneFont, bg="red").pack(pady=25)
	# successLabel.place(x=260, y=50)

	# Subheading label 
	subheadingLabel = tk.Label(newErrorWindow, text = subheading, font=headerOneFont,bg="red").pack(pady=25)
	# subheadingLabel.place(x=260, y=100)

	# frame for button border 
	# add button - back to previous function 
	createButton = tk.Button(newErrorWindow, text = "Back to " + previousPageText + " Function", font = headerThreeFont, command=newErrorWindow.destroy, bg="red", fg="black").pack(pady=25)
	# createButton.pack()
	# textLabel.place(x=260,y=120))
	newErrorWindow.mainloop()


class aLibrarySystem(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for framepages in (StartPage, HomePage, MembershipPage, MembershipCreation,MembershipDeletion, 
		DeletionConfirmationFrame, MembershipUpdate, Update,UpdateConfirmationFrame, BooksPage, Acquisition,
		Withdrawal, WithdrawalConfirmationFrame, ReportsPage, FinesPage, FinesPayment, FineConfirmationFrame, SearchReport, MemberLoanReport,ReservationPage, MakeReservation,
                           CancelReservation, ReserveConfirmationFrame, ReservationCancellationConfirmationFrame, LoansPage, Borrow, BorrowConfirmationFrame, BookReturn, ReturnBookConfirmationFrame):
            page_name = framepages.__name__
            frame = framepages(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.refresh()
	

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Welcome to our Library System", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button3= tk.Button(self, text="Go to Page Home",command=lambda: controller.show_frame("HomePage"))
		button3.pack()

	def refresh(self):
		return  

     
		

	
class HomePage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		global bgImage
		bgImage = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Background.jpeg")))
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# add the ALS Title 
		alsLabel = tk.Label(self, text = "(ALS)", font = headerOneFont, fg = "white", bg = "#BB7793", borderwidth = 3, width = 10)
		alsLabel.grid(row = 0, column = 1, padx = 20, pady = 20)

		# images
		membershipImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Membership.jpeg")).resize((400,270)))
		bookImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Books.jpeg")).resize((400,270)))
		loansImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Loans.jpeg")).resize((400,270)))
		reservationsImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Reservations.jpeg")).resize((400,270)))
		finesImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Fines.jpeg")).resize((400,270)))
		reportsImg = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Reports.jpeg")).resize((400,270)))

		# buttons to tap on the photo + photo + positioning 
		membershipButton = tk.Button(self, text = "Membership", compound = "top", font = headerTwoFont, image = membershipImg, 
		command = lambda: controller.show_frame("MembershipPage"))
		membershipButton.image = membershipImg
		membershipButton.grid(row = 1, column = 0, padx = 20, pady = 20)

		booksButton = tk.Button(self, text = "Books", compound = "top", font = headerTwoFont, image = bookImg,
		command = lambda: controller.show_frame("BooksPage"))
		booksButton.image = bookImg
		booksButton.grid(row = 1, column = 1, padx = 20, pady = 20)

		loansButton = tk.Button(self, text = "Loans", compound = "top", font = headerTwoFont, image = loansImg,
		command = lambda: controller.show_frame("LoansPage"))
		loansButton.image = loansImg
		loansButton.grid(row = 1, column = 2, padx = 20, pady = 20)

		reservationButton = tk.Button(self, text = "Reservation", compound = "top", font = headerTwoFont, image = reservationsImg,
		command = lambda: controller.show_frame("ReservationPage"))
		reservationButton.image = reservationsImg
		reservationButton.grid(row = 2, column = 0, padx = 20, pady = 20)

		finesButton = tk.Button(self, text = "Fines", compound = "top", font = headerTwoFont, image = finesImg,
		command = lambda: controller.show_frame("FinesPage"))
		finesButton.image = finesImg
		finesButton.grid(row = 2, column = 1, padx = 20, pady = 20)

		reportsButton = tk.Button(self, text = "Reports", compound = "top", font = headerTwoFont, image = reportsImg,
		command = lambda: controller.show_frame("ReportsPage"))
		reportsButton.image = reportsImg
		reportsButton.grid(row = 2, column = 2, padx = 20, pady = 20)
	def refresh(self):
		pass

class MembershipPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)
		
		# create picture
		self.canvas = Canvas(self, width = 600, height = 400)
		self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Membership.jpeg")).resize((600,400)))
		self.canvas.create_image(300,200, image=self.image) 
		self.canvas.place(x=100,y=225)
		
		# create header
		header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)

		# create menu label
		membershipLabel = tk.Label(self, text = "Memberships", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
		membershipLabel.place(x = 275,y=550)

		# create button 
		createButton = tk.Button(self, text = "1. Creation", font = headerOneFont, command = lambda: controller.show_frame("MembershipCreation")).place(x = 750, y = 260)
		createLabel = tk.Label(self, text = "Membership Creation", font = headerTwoFont)
		createLabel.place(x = 1000, y = 260)
	
		# delete button	 
		deleteButton = tk.Button(self, text = "2. Deletion", font = headerOneFont, command = lambda: controller.show_frame("MembershipDeletion")).place(x = 750, y = 410)
		deleteLabel = tk.Label(self, text = "Membership Deletion", font = headerTwoFont)
		deleteLabel.place(x = 1000, y = 410)

		# update button 
		updateButton = tk.Button(self, text = "3. Update", font = headerOneFont, command = lambda: controller.show_frame("MembershipUpdate")).place(x = 750, y = 550)
		updateLabel = tk.Label(self, text = "Membership Deletion", font = headerTwoFont)
		updateLabel.place(x = 1000, y = 550)

		# Back to Main 
		createButtonMain(self.controller, headerThreeFont, 0, 0, self)
	def refresh(self):
		pass

class MembershipCreation(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " To Create Member, Please Enter Requested Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 250, y = 100)
		
		# labels and text entry box
		membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberIdEntry = Entry(self, textvariable=memberId,width= 40)
		memberIdEntry.place(x=580,y=200)
		memberIdEntry.insert(0, " A unique alphanumeric id that distinguishes every member")
		memberInput = memberIdEntry.get()

		nameLabel = Label(self, text=" Name ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		nameString = StringVar()
		nameEntry = Entry(self, textvariable=nameString,width= 40)
		nameEntry.place(x=580,y=250)
		nameEntry.insert(0, " Enter member’s name ")

		facultyLabel = Label(self, text=" Faculty ", font = headerThreeFont,bg="seashell1").place(x=430,y=295)
		facultyString = StringVar()
		facEntry = Entry(self, textvariable=facultyString,width= 40)
		facEntry.place(x=580,y=300)
		facEntry.insert(0, " e.g., Computing, Engineering, Science, etc.")
		facInput = facEntry.get()

		numberLabel = Label(self, text=" Phone Number ", font = headerThreeFont,bg="seashell1").place(x=390,y=345)
		numberString = StringVar()
		numEntry = Entry(self, textvariable=numberString,width= 40)
		numEntry.place(x=580,y=350)
		numEntry.insert(0, " e.g., 91234567, 81093487, 92054981, etc ")
		numInput = numEntry.get()

		emailLabel = Label(self, text=" Email Address ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		emailString = StringVar()
		emailEntry = Entry(self, textvariable=emailString,width= 40)
		emailEntry.place(x=580,y=400)
		emailEntry.insert(0, " e.g., ALSuser@als.edu ")
		emailInput = emailEntry.get()

        # buttons
		createMemberButton = tk.Button(self, text = "Create Member", font = buHeadings, bg="#A6934E", command= lambda: callCreate(cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")

		# create member in database
		def callCreate(inputCur, inputConn):
			membershipTuple = (memberIdEntry.get(), nameEntry.get(), facEntry.get(), numEntry.get(), emailEntry.get())

			if(mysql.create_member(membershipTuple[0], membershipTuple[1] ,membershipTuple[2],membershipTuple[3],membershipTuple[4],inputCur,inputConn) == True):
				functionCalled = successFrame(self.controller,"ALS Membership Created", "Create " )
			else:
				functionCalled = errorFrame(self.controller, "Member already exist;\nMissing or Incomplete fields.", "Create")
			return functionCalled

	def refresh(self):
		pass

class MembershipDeletion(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " To Delete Member, Please Enter Membership ID:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 275, y = 100)
		
		# labels and text entry box
		membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		memberId = StringVar()
		memberIdEntry = Entry(self, textvariable=memberId,width= 40)
		memberIdEntry.place(x=580,y=300)
		memberIdEntry.get()
		memberIdEntry.insert(0, " A unique alphanumeric id that distinguishes every member")

		def callDelete(inputCur, inputConn):

			membershipTuple = (memberId.get())
			if membershipTuple:
				flag = False
				global member_to_send
				inputCur.execute('select * from member')
				output = inputCur.fetchall()
				for member in output:
					if memberId.get() == member[0]:
						member_to_send = member		
						flag = True
				if flag:
					return controller.show_frame("DeletionConfirmationFrame")	
				else:
					return errorFrame(self.controller,"Member does not exist", "Delete " )
			else:
				return errorFrame(self.controller, "Member has loans;\nMissing or Incomplete fields.", "Create")

		deleteMemberButton = tk.Button(self, text = "Delete Member", font = buHeadings, bg="#A6934E", command= lambda:callDelete(cur, conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")
		
	def refresh(self):
		pass

class DeletionConfirmationFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		confirmLabel = tk.Label(self, text = "Please Confirm Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

		memberLabel = Label(self, text=" Member ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberId.set("")
		self.memberIdEntry = Label(self,width= 40, text = "xxx") 
		self.memberIdEntry.place(x=580,y=200)
		# memberIdEntry.insert(0, memberIdEntry)


		# self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		nameLabel = Label(self, text=" Name ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		nameString = StringVar()
		nameString.set("")
		self.nameEntry = Label(self,width= 40, text = "xxx")
		self.nameEntry.place(x=580,y=250)
		
		facultyLabel = Label(self, text=" Faculty ", font = headerThreeFont,bg="seashell1").place(x=430,y=295)
		facultyString = StringVar()
		facultyString.set("")
		self.facEntry = Label(self,width= 40, text = "xxx")
		self.facEntry.place(x=580,y=300)

		numberLabel = Label(self, text=" Phone Number ", font = headerThreeFont,bg="seashell1").place(x=390,y=345)
		numberString = StringVar()
		numberString.set("")
		self.numEntry = Label(self,width= 40, text = "xxx")
		self.numEntry.place(x=580,y=350)

		emailLabel = Label(self, text=" Email Address ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		emailString = StringVar()
		emailString.set("")
		self.emailEntry = Label(self,width= 40, text = "xxx")
		self.emailEntry.place(x=580,y=400)
	
        # buttons
		deleteMemberButton = tk.Button(self, text = "Delete Member", font = buHeadings, bg="#A6934E", command= lambda: callDelete(member_to_send[0], cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")

		def callDelete(memberId, inputCur,inputConn):
			mysql.delete_member(memberId,inputCur,inputConn)
			successFrame(self.controller,"Member Deleted ", "Delete " )
			return controller.show_frame("Update")


	def refresh(self):
		self.memberIdEntry.config(text=member_to_send[0])
		self.nameEntry.config(text = member_to_send[1])
		self.facEntry.config(text = member_to_send[2])
		self.numEntry.config(text = member_to_send[3])
		self.emailEntry.config(text = member_to_send[4])

class MembershipUpdate(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " To Update a Member, Please Enter Membership ID:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 275, y = 100)
		
		# labels and text entry box
		membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberIdEntry = Entry(self, textvariable=memberId,width= 40)
		memberIdEntry.place(x=580,y=200)
		memberIdEntry.insert(0, " A unique alphanumeric id that distinguishes every member")

		def callUpdatePage(inputCur, inputConn):
			if(mysql.member_exists(memberIdEntry.get(), inputCur, inputConn) == True):
				global updateMemberID
				updateMemberID = memberIdEntry.get()
				return controller.show_frame("Update")
			else:
				return errorFrame(self.controller, "Member Does Not exist", "Update")



		# buttons 
		updateMemberButton = tk.Button(self, text = "Update Member", font = buHeadings,bg="#A6934E", command=lambda: callUpdatePage(cur,conn)).place(x = 300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")



			# print(membershipTuple[1])
			# mysql.fuk("awdhu", "123a" ,"asda","asd","111@als.edu",curre,connen)

			# functionCalled = controller.show_frame("Update")
	
			# return functionCalled
			# print(self.member_lists)
	def refresh(self):
		pass

class Update(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = "To Update a Member, Please Enter Membership ID:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 275, y = 100)


		# labels and text entry box
		#self.memberIdinput = self.master.memberIdinput
		#self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=195)
		#self.membershipIdLabel['text'] = self.memberIdinput


		memberLabel = Label(self, text=" Member ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberId.set("")
		self.memberIdEntry = Label(self,width= 40, text = "xxx") 
		self.memberIdEntry.place(x=580,y=200)
		# memberIdEntry.insert(0, memberIdEntry)

		nameLabel = Label(self, text=" Name ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		nameString = StringVar()
		nameEntry = Entry(self, textvariable=nameString,width= 40)
		nameEntry.place(x=580,y=250)
		nameEntry.get()
		nameEntry.insert(0, " Curr Name ")

		facultyLabel = Label(self, text=" Faculty ", font = headerThreeFont,bg="seashell1").place(x=430,y=295)
		facultyString = StringVar()
		facEntry = Entry(self, textvariable=facultyString,width= 40)
		facEntry.place(x=580,y=300)
		facEntry.get()
		facEntry.insert(0, " Curr Fac")

		numberLabel = Label(self, text=" Phone Number ", font = headerThreeFont,bg="seashell1").place(x=390,y=345)
		numberString = StringVar()
		numEntry = Entry(self, textvariable=numberString,width= 40)
		numEntry.place(x=580,y=350)
		numEntry.get()
		numEntry.insert(0, " Curr Num ")

		emailLabel = Label(self, text=" Email Address ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		emailString = StringVar()
		emailEntry = Entry(self, textvariable=emailString,width= 40)
		emailEntry.place(x=580,y=400)
		emailEntry.get()
		emailEntry.insert(0, " Curr Email ")
		# call the confirmation page which prints out the deatils where inputId = memberId from Member

		def callUpdate(inputCur, inputConn):
			global membershipTuple
			membershipTuple = (nameEntry.get(), facEntry.get(), numEntry.get(), emailEntry.get())
			for ele in membershipTuple:
				if ele:
					continue
				else:
					return errorFrame(self.controller,"Missing or " + "\n" + "Incomplete fields ", "Update " )
					break
			return controller.show_frame("UpdateConfirmationFrame")


			# if(mysql.updateMember(membershipTuple[0], membershipTuple[1] ,membershipTuple[2],membershipTuple[3],membershipTuple[4],inputCur,inputConn) == True):
			# 	mysql.updateMember(membershipTuple[0], membershipTuple[1] ,membershipTuple[2],membershipTuple[3],membershipTuple[4],inputCur,inputConn)
			# 	functionCalled = confirmFrame(self.controller,"Updated ","Add table lol idk", "Update " )
			

			return functionCalled

		# buttons 
		updateMemberButton = tk.Button(self, text = "Update Member", font = buHeadings, bg="#A6934E", command=lambda: callUpdate(cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")


	def refresh(self):
		self.memberIdEntry.config(text=updateMemberID)

class UpdateConfirmationFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		confirmLabel = tk.Label(self, text = "Please Confirm Update Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

		memberLabel = Label(self, text=" Member ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberId.set("")
		self.memberIdEntry = Label(self,width= 40, text = "xxx") 
		self.memberIdEntry.place(x=580,y=200)
		# memberIdEntry.insert(0, memberIdEntry)


		# self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		nameLabel = Label(self, text=" Name ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		nameString = StringVar()
		nameString.set("")
		self.nameEntry = Label(self,width= 40, text = "xxx")
		self.nameEntry.place(x=580,y=250)
		
		facultyLabel = Label(self, text=" Faculty ", font = headerThreeFont,bg="seashell1").place(x=430,y=295)
		facultyString = StringVar()
		facultyString.set("")
		self.facEntry = Label(self,width= 40, text = "xxx")
		self.facEntry.place(x=580,y=300)

		numberLabel = Label(self, text=" Phone Number ", font = headerThreeFont,bg="seashell1").place(x=390,y=345)
		numberString = StringVar()
		numberString.set("")
		self.numEntry = Label(self,width= 40, text = "xxx")
		self.numEntry.place(x=580,y=350)

		emailLabel = Label(self, text=" Email Address ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		emailString = StringVar()
		emailString.set("")
		self.emailEntry = Label(self,width= 40, text = "xxx")
		self.emailEntry.place(x=580,y=400)

		def callUpdate(memberId, name, faculty, number, email, inputCur,inputConn):
			mysql.update_member(memberId, name, faculty, number, email,inputCur,inputConn)
			successFrame(self.controller,"Member Deleted ", "Delete " )
			return controller.show_frame("Update")        # buttons

		UpdateMemberButton = tk.Button(self, text = "Update Member", font = buHeadings, bg="#A6934E", command= lambda: callUpdate(updateMemberID,membershipTuple[0],membershipTuple[1],membershipTuple[2],membershipTuple[3],cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Membership", "MembershipPage")

	def refresh(self):
		self.memberIdEntry.config(text= updateMemberID)
		self.nameEntry.config(text = membershipTuple[0])
		self.facEntry.config(text = membershipTuple[1])
		self.numEntry.config(text = membershipTuple[2])
		self.emailEntry.config(text = membershipTuple[3])

class BooksPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# create picture
		self.canvas = Canvas(self, width = 625, height = 375)
		self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Books.jpeg")).resize((625,375)))
		self.canvas.create_image(300,175, image=self.image)
		self.canvas.place(x=100,y=175)

		# header
		header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)

		booksLabel = tk.Label(self, text = "Books", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
		booksLabel.place(x = 275,y=450)

		# Acquisition
		acquisitionButton = tk.Button(self, text = "4. Acquisition", font = headerOneFont, command = lambda: controller.show_frame("Acquisition")).place(x = 750, y = 260)
		acquisitionLabel = tk.Label(self, text = "Book Aquisition", font = headerTwoFont)
		acquisitionLabel.place(x = 1000, y = 260)

		# Withdrawal
		withdrawalButton = tk.Button(self, text = "5. Withdrawal", font = headerOneFont, command = lambda: controller.show_frame("Withdrawal")).place(x = 750, y = 410)
		withdrawalLabel = tk.Label(self, text = "Book Withdrawal", font = headerTwoFont)
		withdrawalLabel.place(x = 1000, y = 410)

		# Back to Main 
		createButtonMain(self.controller, headerThreeFont, 0, 0, self)

	def refresh(self):
		pass  

class Acquisition(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " For new Book Acquisition, Please Enter Required Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 225, y = 100)
		
		# labels and text entry box
		accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=375,y=195)
		accessionNum = StringVar()
		accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
		accessionNumEntry.place(x=580,y=200)
		accessionNumEntry.insert(0, " Used to identify an instance of book")

		titleLabel = Label(self, text=" Title ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		titleString = StringVar()
		titleEntry = Entry(self, textvariable=titleString,width= 40)
		titleEntry.place(x=580,y=250)
		titleEntry.insert(0, " Book Title ")

		authorsLabel = Label(self, text=" Authors ", font = headerThreeFont,bg="seashell1").place(x=415,y=295)
		authorsString = StringVar()
		authorsEntry = Entry(self, textvariable=authorsString,width= 40)
		authorsEntry.place(x=580,y=300)
		authorsEntry.insert(0, " There can be multiple authors for a book")

		ISBNLabel = Label(self, text=" ISBN ", font = headerThreeFont,bg="seashell1").place(x=430,y=345)
		ISBNString = StringVar()
		ISBNEntry = Entry(self, textvariable=ISBNString,width= 40)
		ISBNEntry.place(x=580,y=350)
		ISBNEntry.insert(0, " ISBN Number ")

		publisherLabel = Label(self, text=" Publisher ", font = headerThreeFont,bg="seashell1").place(x=410,y=395)
		publisherString = StringVar()
		publisherEntry = Entry(self, textvariable=publisherString,width= 40)
		publisherEntry.place(x=580,y=400)
		publisherEntry.insert(0, " Random House, Penguin, Cengage, Springer, etc. ")

		publicationYearLabel = Label(self, text=" Publication Year ", font = headerThreeFont,bg="seashell1").place(x=375,y=450)
		publicationYearString = StringVar()
		publicationYearEntry = Entry(self, textvariable=publicationYearString,width= 40)
		publicationYearEntry.place(x=580,y=450)
		publicationYearEntry.insert(0, " Edition Year ")

		# buttons
		addNewBookButton = tk.Button(self, text = "Add New Book", font = buHeadings, bg="#A6934E", command= lambda: callAcquisition(cur,conn)).place(x=300, y = 520)
		createBack(self.controller, buHeadings, 720, 520, self, "Books", "BooksPage")

		# create member in database
		def callAcquisition(inputCur, inputConn):
			authorTuple = authorsEntry.get().split(",")
			bookTuple = (accessionNumEntry.get(), titleEntry.get(), authorTuple, ISBNEntry.get(), publisherEntry.get(), publicationYearEntry.get())

			if(mysql.add_book(bookTuple[0], bookTuple[1] ,bookTuple[2],bookTuple[3],bookTuple[4],bookTuple[5],inputCur,inputConn) == True):
				functionCalled = successFrame(self.controller,"New Book added in Library.", "Acquisition " )
			else:
				functionCalled = errorFrame(self.controller, "Book already added;\nDuplicate, Missing or Incomplete fields.", "Acquisition")
			return functionCalled
	
	def refresh(self):
		pass  

class Withdrawal(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " To Remove Outdated Books From System, Please Enter Required Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 50, y = 100)
		
		# labels and text entry box
		accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		accessionNum = StringVar()
		accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
		accessionNumEntry.place(x=625,y=300)
		accessionNumEntry.get()
		accessionNumEntry.insert(0, " Used to identify an instance of book")

		# withdraw book 
		withdrawButton = tk.Button(self, text = "Withdraw Book", font = buHeadings, bg="#A6934E").place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Books", "BooksPage")

		def callWithdraw(inputCur, inputConn):
			accessionNumSelected = (accessionNumEntry.get())
			if accessionNumSelected:
				bookExists = False
				bookOnLoan = False
				bookReserved = False
				global book_to_send
                
                #check book exists 
				inputCur.execute('select * from Book')
				output = inputCur.fetchall()
				for book in output:
					# get book tuple
					if accessionNumSelected == book[0]:

						cur.execute("SELECT name FROM Author WHERE accession_num = '{}'".format(accessionNumSelected))
						authorTuple = cur.fetchall()
						to_print = ()
						for ele in authorTuple:
							to_print+=(ele[0],)
						authorTuple = ",".join(to_print)

						book_to_send = (book[0],book[1],authorTuple,book[2],book[3],book[4])

						bookExists = True   
                #check book on loan
				inputCur.execute('SELECT accession_num FROM Loans')
				output = cur.fetchall()
				for book in output:
					for accessionNum in book:
						if accessionNumSelected == accessionNum:
							bookOnLoan = True
                #check book reserved
				inputCur.execute('SELECT accession_num FROM Reserves')
				output = cur.fetchall()
				for book in output:
					for accessionNum in book:
						if accessionNumSelected == accessionNum:
							bookReserved = True
                
				if not bookExists:
					return errorFrame(self.controller,"Book does not exist", "Withdraw" )
				elif bookOnLoan and bookReserved:
					return errorFrame(self.controller,"Book is currently on loan and reserved", "Withdraw")
				elif bookOnLoan: 
					return errorFrame(self.controller,"Book is currently loan", "Withdraw")
				elif bookReserved: 
					return errorFrame(self.controller,"Book is currently reserved","Withdraw")
				else:
					
					return controller.show_frame("WithdrawalConfirmationFrame")	
			else: 
				return errorFrame(self.controller, "Missing or Incomplete fields.", "Withdrawal")

		withdrawBookButton = tk.Button(self, text = "Delete Book", font = buHeadings, bg="#A6934E", command= lambda:callWithdraw(cur, conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Books", "BooksPage")
	
	def refresh(self):
		pass  

class WithdrawalConfirmationFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		confirmLabel = tk.Label(self, text = "Please Confirm Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

		accessionNumLabel = Label(self, text=" Accession Number ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
		accessionNum = StringVar()
		accessionNum.set("")
		self.accessionNumEntry = Label(self,width= 40, text = "xxx") 
		self.accessionNumEntry.place(x=580,y=200)
		# memberIdEntry.insert(0, memberIdEntry)

		# self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		titleLabel = Label(self, text=" Title ", font = headerThreeFont,bg="seashell1").place(x=400,y=245)
		titleString = StringVar()
		titleString.set("")
		self.titleEntry = Label(self,width= 40, text = "xxx")
		self.titleEntry.place(x=580,y=250)
		
		authorsLabel = Label(self, text=" Authors ", font = headerThreeFont,bg="seashell1").place(x=400,y=295)
		authorsString = StringVar()
		authorsString.set("")
		self.authorsEntry = Label(self,width= 40, text = "xxx")
		self.authorsEntry.place(x=580,y=300)

		ISBNLabel = Label(self, text=" ISBN ", font = headerThreeFont,bg="seashell1").place(x=400,y=345)
		ISBNString = StringVar()
		ISBNString.set("")
		self.ISBNEntry = Label(self,width= 40, text = "xxx")
		self.ISBNEntry.place(x=580,y=350)

		publisherLabel = Label(self, text=" Publisher ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		publisherString = StringVar()
		publisherString.set("")
		self.publisherEntry = Label(self,width= 40, text = "xxx")
		self.publisherEntry.place(x=580,y=400)

		yearLabel = Label(self, text=" Year ", font = headerThreeFont,bg="seashell1").place(x=400,y=445)
		yearString = StringVar()
		yearString.set("")
		self.yearEntry = Label(self,width= 40, text = "xxx")
		self.yearEntry.place(x=580,y=450)
	
        # buttons
		withdrawButton = tk.Button(self, text = "Confirm Withdrawal", font = buHeadings, bg="#A6934E", command= lambda: callWithdraw(book_to_send[0], cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Withdrawal", "Withdrawal")

		def callWithdraw(memberId, inputCur,inputConn):
			mysql.withdraw_book(memberId,inputCur,inputConn)
			successFrame(self.controller,"Member Deleted ", "Delete " )
			return controller.show_frame("Update")

	def refresh(self):
		print(book_to_send)
		self.accessionNumEntry.config(text=book_to_send[0])
		self.titleEntry.config(text = book_to_send[1])
		self.authorsEntry.config(text = book_to_send[2])
		self.ISBNEntry.config(text = book_to_send[3])
		self.publisherEntry.config(text = book_to_send[4])
		self.yearEntry.config(text = book_to_send[5])

class ReportsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# create picture
		self.canvas = Canvas(self, width = 625, height = 375)
		self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Reports.jpeg")).resize((625,375)))
		self.canvas.create_image(300,175, image=self.image)
		self.canvas.place(x=0,y=225)

		def createPopUp(tpl):	
			popup = tk.Toplevel()
			for i in range(len(tpl)):
				for j in range(len(tpl[0])):
					self.textbox = ttk.Label(popup, text= tpl[i][j], font = headerThreeFont)
					self.textbox.config(text = tpl[i][j])
					self.textbox.grid(row=i, column=j)
			backButton = ttk.Button(popup, text="Back to search function", command=popup.destroy).grid(row=i+1, column=(j+1))
		
		# create header
		header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)

		# create menu label
		reportsLabel = tk.Label(self, text = "Reports", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
		reportsLabel.place(x = 120,y=500)

			

		searchButton = tk.Button(self, text = "11. Book\nSearch", font = headerOneFont, command = lambda: controller.show_frame("SearchReport")).place(x = 530, y = 210)
		searchLabel = tk.Label(self, text = "A member can perform a search on\nthe collecion of books.", font = headerTwoFont)
		searchLabel.place(x = 820, y = 210)

		# Books on Loan
		def callLoanReport():
			cur.execute("SELECT * FROM Loans")
			allbksonloan = cur.fetchall()
			tup =()
			for ele in allbksonloan:
				tup += (ele[1],)
			final_tup = ()
			title = ("Accesion Number", "Title", "ISBN","Publisher","Publication Year")
			final_tup += (title,)
			cur.execute("SELECT * FROM Book")
			allbks = cur.fetchall()
			for tofind in tup:
				for bk in allbks:
					if bk[0] == tofind:
						final_tup += (bk,)
			
			createPopUp(final_tup)

		loanButton = tk.Button(self, text = "12. Books on\nLoan", font = headerOneFont, command = lambda: callLoanReport()).place(x = 530, y = 310)
		loanLabel = tk.Label(self, text = "This function displays all the\nbooks currently on loan to members.", font = headerTwoFont)
		loanLabel.place(x = 820, y = 310)

		# Books on Reservation
		def callReservationReport():
			cur.execute("SELECT * FROM Reserves")
			allbksonloan = cur.fetchall()
			tup =()
			for ele in allbksonloan:
				tup += (ele[1],)
			final_tup = ()
			title = ("Accesion Number", "Title", "ISBN","Publisher","Publication Year")
			final_tup += (title,)
			cur.execute("SELECT * FROM Book")
			allbks = cur.fetchall()
			for tofind in tup:
				for bk in allbks:
					if bk[0] == tofind:
						final_tup += (bk,)
			createPopUp(final_tup)
		reservationButton = tk.Button(self, text = "12. Books on\nReservation", font = headerOneFont, command = lambda: callReservationReport()).place(x = 530, y = 410)
		reservationLabel = tk.Label(self, text = "This function displays all the\nbooks that members have reserved.", font = headerTwoFont)
		reservationLabel.place(x = 820, y = 410)

		# Outstanding Fines
		def callFinesReport():
			cur.execute("SELECT * FROM Fine")
			allbksonloan = cur.fetchall()
			tup =()
			for ele in allbksonloan:
				tup += (ele[0],)
			final_tup = ()
			title = ("MemberID ", "Name", "Faculty","Phone Number","Email Address")
			final_tup += (title,)
			cur.execute("SELECT * FROM Member")
			allbks = cur.fetchall()
			for tofind in tup:
				for bk in allbks:
					if bk[0] == tofind:
						final_tup += (bk,)
			createPopUp(final_tup)
		finesButton = tk.Button(self, text = "14. Outstanding\nFines", font = headerOneFont, command = lambda: callFinesReport()).place(x = 530, y = 510)
		finesLabel = tk.Label(self, text = "This function displays all the\noutstanding fines members have.", font = headerTwoFont)
		finesLabel.place(x = 820, y = 510)

		# Books on Loan to Member

		memberLoanButton = tk.Button(self, text = "15. Books on\nLoan to\nMember", font = headerOneFont, command = lambda: controller.show_frame("MemberLoanReport")).place(x = 530, y = 610)
		memberLoanLabel = tk.Label(self, text = "This function displays all the\nbooks a member identified by the\nmembership id has borrowed.", font = headerTwoFont)
		memberLoanLabel.place(x = 820, y = 610)

		# Back to Main 
		createButtonMain(self.controller, headerThreeFont, 0, 0, self)

	def refresh(self):
		pass
class MemberLoanReport(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		def createPopUp(tpl):	
			popup = tk.Toplevel()
			for i in range(len(tpl)):
				for j in range(len(tpl[0])):
					self.textbox = ttk.Label(popup, text= tpl[i][j], font = headerThreeFont)
					self.textbox.config(text = tpl[i][j])
					self.textbox.grid(row=i, column=j)
			backButton = ttk.Button(popup, text="Back to search function", command=popup.destroy).grid(row=i+1, column=(j+1))


		# create header
		header = tk.Label(self, text = "Books on Loan to Member: ", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)
		
		# labels and text entry box
		memberIDLabel = Label(self, text=" Member ID  ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		memberIDString = StringVar()
		memberIDEntry = Entry(self, textvariable=memberIDString,width= 40)
		memberIDEntry.place(x=580,y=250)
		memberIDEntry.insert(0, "A unique alphanumeric id that distinguishes every member")


		# buttons
		searchMemberButton = tk.Button(self, text = "Search Member", font = buHeadings, bg="#A6934E", command= lambda: callMemberLoan(cur,conn)).place(x=300, y = 520)
		createBack(self.controller, buHeadings, 720, 520, self, "reports ", "ReportsPage")

		# create member in database
		def callMemberLoan(cur, conn):
			ID = memberIDEntry.get()
			if(mysql.can_update(ID, cur, conn) == False):
				return errorFrame(self.controller, "No such member.", "Search Report")
			
			cur.execute("SELECT * FROM Book WHERE accession_num IN (SELECT accession_num FROM Loans WHERE memberID = '{}')".format(ID))
			output = cur.fetchall()
			print(output)
			if output == (): 
				return errorFrame(self.controller, "Member does not have loans.", "Search Report")
			else: 
				final = (("Accesion Number", "Title", "ISBN","Publisher","Publication Year"),)
				final += output
                                
                                
			createPopUp(final)

	def refresh(self):
		pass          
	
class SearchReport(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		def createPopUp(tpl):	
			popup = tk.Toplevel()
			for i in range(len(tpl)):
				for j in range(len(tpl[0])):
					self.textbox = ttk.Label(popup, text= tpl[i][j], font = headerThreeFont)
					self.textbox.config(text = tpl[i][j])
					self.textbox.grid(row=i, column=j)
			backButton = ttk.Button(popup, text="Back to search function", command=popup.destroy).grid(row=i+1, column=(j+1))
		# create header
		header = tk.Label(self, text = "Search based on one of the categories below: ", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)
		
		# labels and text entry box
		titleLabel = Label(self, text=" Title ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		titleString = StringVar()
		titleEntry = Entry(self, textvariable=titleString,width= 40)
		titleEntry.place(x=580,y=250)
		titleEntry.insert(0, "")

		authorsLabel = Label(self, text=" Authors ", font = headerThreeFont,bg="seashell1").place(x=415,y=295)
		authorsString = StringVar()
		authorsEntry = Entry(self, textvariable=authorsString,width= 40)
		authorsEntry.place(x=580,y=300)
		authorsEntry.insert(0, "")

		ISBNLabel = Label(self, text=" ISBN ", font = headerThreeFont,bg="seashell1").place(x=430,y=345)
		ISBNString = StringVar()
		ISBNEntry = Entry(self, textvariable=ISBNString,width= 40)
		ISBNEntry.place(x=580,y=350)
		ISBNEntry.insert(0, "")

		publisherLabel = Label(self, text=" Publisher ", font = headerThreeFont,bg="seashell1").place(x=410,y=395)
		publisherString = StringVar()
		publisherEntry = Entry(self, textvariable=publisherString,width= 40)
		publisherEntry.place(x=580,y=400)
		publisherEntry.insert(0, "")

		publicationYearLabel = Label(self, text=" Publication Year ", font = headerThreeFont,bg="seashell1").place(x=375,y=450)
		publicationYearString = StringVar()
		publicationYearEntry = Entry(self, textvariable=publicationYearString,width= 40)
		publicationYearEntry.place(x=580,y=450)
		publicationYearEntry.insert(0, "")

		# buttons
		searchBookButton = tk.Button(self, text = "Search Book", font = buHeadings, bg="#A6934E", command= lambda: callSearchBook(cur,conn)).place(x=300, y = 520)
		createBack(self.controller, buHeadings, 720, 520, self, "reports ", "ReportsPage")

		# create member in database
		def callSearchBook(cur, conn):
			searchTuple = (titleEntry.get(), authorsEntry.get(), ISBNEntry.get(), publisherEntry.get(), publicationYearEntry.get())
			indexTuple = ("title", "author", "ibsn", "Publisher", "Publication_year")
                                      
			print(searchTuple)
			for i in range(len(searchTuple)):
                                                                                #search for title, publisher
				if searchTuple[i] != "" and (i == 0 or i == 3):
                        
					cur.execute("select * from book where {} LIKE '% {} %' OR {} LIKE '% {}' or {} like '{} %'".format(indexTuple[i], searchTuple[i], indexTuple[i],searchTuple[i], indexTuple[i],searchTuple[i]))

					output = (("Accesion Number", "Title", "ISBN","Publisher","Publication Year"),)
					
					output += cur.fetchall()
					print(output)
					break
				#search for ibsn, publication_year
				if searchTuple[i] != "" and (i == 2 or i == 4):
					cur.execute("select * from book where {} = '{}'".format(indexTuple[i], searchTuple[i]))
					output = (("Accesion Number", "Title", "ISBN","Publisher","Publication Year"),)
					output += cur.fetchall()
					print(output)
					break
				#search for author
				elif searchTuple[i] != "" and i == 1:
					cur.execute("SELECT * FROM Book WHERE accession_num IN (SELECT accession_num FROM Author WHERE name LIKE '% {} %' OR name LIKE '% {}' OR name LIKE '{} %')".format(searchTuple[i],searchTuple[i], searchTuple[i]))
					output = (("Accesion Number", "Title", "ISBN","Publisher","Publication Year"),)
					output += cur.fetchall()
					break
				
				else:
					output = ()
					
			if output == ():
				return errorFrame(self.controller, "Missing or Incomplete fields.", "Search Report")
			
			createPopUp(output)

	def refresh(self):
		pass  


	
class FinesPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# create picture
		self.canvas = Canvas(self, width = 600, height = 400)
		self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Fines.jpeg")).resize((600,400)))
		self.canvas.create_image(300,200, image=self.image) 
		self.canvas.place(x=100,y=150)

		# create header
		header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)

		# create menu label
		finesLabel = tk.Label(self, text = "Fines", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
		finesLabel.place(x = 265,y=475)

		# Payment
		paymentButton = tk.Button(self, text = "10. Payment", font = headerOneFont, command = lambda: controller.show_frame("FinesPayment")).place(x = 750, y = 260)
		paymentLabel = tk.Label(self, text = "Fine Payment", font = headerTwoFont)
		paymentLabel.place(x = 1000, y = 260)

		# Back to Main 
		createButtonMain(self.controller, headerThreeFont, 0, 0, self)
	def refresh(self):
		pass


		

class FinesPayment(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		global memberIdEntry, dateEntry, amountEntry

		# add bg
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		#  header
		header = tk.Label(self, text = " To pay a Fine, Please Enter Requested Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 250, y = 100)
		
		# labels and text entry box
		membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberIdEntry = Entry(self, textvariable=memberId,width= 40)
		memberIdEntry.place(x=580,y=200)
		memberIdEntry.get()
		memberIdEntry.insert(0, " A unique alphanumeric id that distinguishes every member")
		

		dateLabel = Label(self, text="Payment Date", font = headerThreeFont, bg="seashell1").place(x=400,y=245)
		date = StringVar()
		dateEntry = Entry(self, textvariable=date,width= 40)
		dateEntry.place(x=580,y=250)
		dateEntry.get()
		dateEntry.insert(0, "Date payment received")
		dateInput = dateEntry.get()

		amountLabel = Label(self, text="Payment Amount", font = headerThreeFont, bg="seashell1").place(x=390,y=295)
		amount = StringVar()
		amountEntry = Entry(self, textvariable=amount,width= 40)
		amountEntry.place(x=580,y=300)
		amountEntry.get()
		amountEntry.insert(0, "payment amount received")
		amountInput = amountEntry.get()
        # buttons
		payFineButton = tk.Button(self, text = "Pay fine", font = buHeadings, bg="#A6934E", command= lambda: callConfirmation(cur, conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Fines", "FinesPage")
		

		# create member in database
		
		def callConfirmation (inputCur, inputConn):
        
			finesTuple = (memberId.get(), date.get(), amount.get())
			global member_id_2
			global date_2 
			global amount_2
			member_id_2 = finesTuple[0]
			date_2 = finesTuple[1]
			amount_2 = finesTuple[2]
			print(finesTuple)
			if((mysql.confirmation_pay_fine(finesTuple[0], finesTuple[1], finesTuple[2], inputCur,inputConn)) == "no member"):
				functionCalled = errorFrame(self.controller, "No such member.", "Create")
				return functionCalled
			    
			if((mysql.confirmation_pay_fine(finesTuple[0], finesTuple[1], finesTuple[2], inputCur,inputConn)) == "no fine"):
				functionCalled = errorFrame(self.controller, "Member has no fine.", "Create")
				return functionCalled
			elif ((mysql.confirmation_pay_fine(finesTuple[0], finesTuple[1], finesTuple[2], inputCur,inputConn)) == "incorrect amount"):
				functionCalled = errorFrame(self.controller, "Incorrect amount.", "Create")
				return functionCalled
		    
			elif((mysql.confirmation_pay_fine(finesTuple[0], finesTuple[1], finesTuple[2], inputCur,inputConn)) == "true" ):
				functionCalled = controller.show_frame("FineConfirmationFrame")
				return functionCalled
			else:
				functionCalled = errorFrame(self.controller, "Error in input details.", "Create")
                                                            
			return functionCalled
		

	def refresh(self):
		pass
	    
class FineConfirmationFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		confirmLabel = tk.Label(self, text = "Please Confirm Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

		memberLabel = Label(self, text=" Member ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberId.set("")
		self.memberIdEntry = Label(self,width= 40, text = "xxx") 
		self.memberIdEntry.place(x=580,y=200)


		# self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
		dateLabel = Label(self, text=" Name ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
		dateString = StringVar()
		dateString.set("")
		self.dateEntry = Label(self,width= 40, text = "xxx")
		self.dateEntry.place(x=580,y=250)
		
		

		amountLabel = Label(self, text="Amount paid: ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
		amountString = StringVar()
		amountString.set("")
		self.amountEntry = Label(self,width= 40, text = "xxx")
		self.amountEntry.place(x=580,y=400)
	
        # buttons
		confirmPaymentButton = tk.Button(self, text = "Confirm Payment", font = buHeadings, bg="#A6934E", command= lambda: callPayment(member_id_2, date_2, amount_2, cur,conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Fine", "FinesPage")

		def callPayment(member_id, date, amount, cur,conn):
			mysql.pay_fine(member_id, date, amount, cur, conn)
			successFrame(self.controller,"Fine Paid!", "FinesPage " )
			return controller.show_frame("FinesPayment")

		

	def refresh(self):
		self.memberIdEntry.config(text=member_id_2)
		self.dateEntry.config(text = date_2)
		self.amountEntry.config(text = amount_2)

class ReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # add bg image
        bg = tk.Label(self, image = bgImage)
        bg.place(x=0,y=0)

        # create picture
        self.canvas = Canvas(self, width = 600, height = 300)
        self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Reservations.jpeg")).resize((600,300)))
        self.canvas.create_image(300,150, image=self.image)
        self.canvas.place(x=20,y=200)

        # create header
        header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
        header.place(x = 450, y = 100)

        # create menu label
        reservationsLabel = tk.Label(self, text = "Reservations", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
        reservationsLabel.place(x = 200,y=400)

        # Reserve
        reserveButton = tk.Button(self, text = "8. Reserve a Book", font = headerOneFont, command = lambda: controller.show_frame("MakeReservation")).place(x = 630, y = 260)
        reserveLabel = tk.Label(self, text = "Book Reservation", font = headerTwoFont)
        reserveLabel.place(x = 1000, y = 260)

        # Cancel
        cancelButton = tk.Button(self, text = "9. Cancel Reservation", font = headerOneFont, command = lambda: controller.show_frame("CancelReservation")).place(x = 630, y = 410)
        cancelLabel = tk.Label(self, text = "Reservation Cancellation", font = headerTwoFont)
        cancelLabel.place(x = 1000, y = 410)
        createButtonMain(self.controller, headerThreeFont, 0, 0, self)


        # Back to Main
    def refresh(self):
        pass

class MakeReservation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bg = tk.Label(self, image = bgImage)
        bg.place(x=0,y=0)
        # add bg image
    
        #  header
        header = tk.Label(self, text = " To Reserve a Book, Please Enter Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
        header.place(x = 250, y = 100)

        # labels and text entry box
        accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=375,y=195)
        accessionNum = StringVar()
        accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
        accessionNumEntry.place(x=580,y=200)

        membershipIDLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=245)
        membershipID = StringVar()
        membershipIDEntry = Entry(self, textvariable=membershipID,width= 40)
        membershipIDEntry.place(x=580,y=250)
        membershipIDEntry.insert(0, " A unique alphanumeric id that distinguishes every member ")

        reserveDateLabel = Label(self, text=" Reserve Date ", font = headerThreeFont,bg="seashell1").place(x=410,y=295)
        reserveDate = StringVar()
        reserveDateEntry = Entry(self, textvariable=reserveDate,width= 40)
        reserveDateEntry.place(x=580,y=300)
        reserveDateEntry.insert(0, " Date of book reservation")
        
        
        def canReserve():
            #extract details and check and send to frames
            global member_reserve_send
            #This creates a class def which shows if ht emember can  be creaete to save the said item
            flagMemberTrue = False
#This runs the same way as per usual codes
            cur.execute('select * from member')
            all_member = cur.fetchall()
            for ele in all_member:
                if ele[0] == membershipID.get():
                    member_reserve_send = ele
                    flagMemberTrue = True
                    
            flagBookTrue = False
            global to_send_book
            cur.execute('select * from book')
            all_books = cur.fetchall()
            for ele in all_books:
                if ele[0] == accessionNum.get():
                    to_send_book = ele
                    flagBookTrue = True

            if flagMemberTrue == False or flagBookTrue == False:
                return errorFrame(self.controller,"Member or Book does not exist", "Reserve")
            
            # if book not in loans => cannot reserve
            flagBookonLoan = False
            cur.execute('SELECT * FROM Loans')
            all_book_loans = cur.fetchall()
            print(all_book_loans)
            for books in all_book_loans:
                if books[1] == accessionNum.get():
                    flagBookonLoan = True
            
            if flagBookonLoan == False:
                return errorFrame(self.controller, "Book is not on loan,\n cannot be reserved", "Reserve")
                
            # check if the book is already reserved
            flagReserveTrue = False
            cur.execute('SELECT accession_num FROM Reserves')
            all_book_reserves = cur.fetchall()
            for ele in all_book_reserves:
                if ele[0] == accessionNum.get():
                    flagReserveTrue = True
                
            if flagReserveTrue == True:
                return errorFrame(self.controller,"Books are already Reserved", "Reserve")
            
            cur.execute("SELECT COUNT(accession_num) FROM Reserves WHERE memberID = '{}'".format(membershipID.get()))
            all_reservations = cur.fetchall()[0][0]
            print(all_reservations)
            if int(all_reservations) >= 2:
                print(all_reservations)
                return errorFrame(self.controller,"Member currently has 2 book" + "\n" + "on reservation", "Reserve")
            
            
            finesflag = False
            cur.execute('select * from Fine')
            finez = cur.fetchall()
            global fineamount
            for ele in finez:
                if ele[0] == membershipID.get():
                    finesflag = True
                    fineamount = ele[2]
            if finesflag:
                errorFrame(self.controller,"Member has outstanding fine of $" + str(fineamount), "Reserve")

            global reserve_date_send
            reserve_date_send = reserveDate.get()

            return controller.show_frame("ReserveConfirmationFrame")
        reserveBookButton = tk.Button(self, text = "Reserve Book ", font = buHeadings, bg="#A6934E", command= lambda: canReserve()).place(x=300, y = 350)
        createBack(self.controller, buHeadings, 720, 400, self, "Reservations", "ReservationPage")
        
    def refresh(self):
        pass
                

class ReserveConfirmationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        confirmLabel = tk.Label(self, text = "Please Confirm Reservation Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

        accLabel = Label(self, text=" Accession Number ", font = headerThreeFont,bg="seashell1").place(x=320,y=195)
        accId = StringVar()
        accId.set("")
        self.accIdEntry = Label(self,width= 40, text = "xxx")
        self.accIdEntry.place(x=580,y=200)
        # memberIdEntry.insert(0, memberIdEntry)

        # self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
        bookLabel = Label(self, text=" Book Title ", font = headerThreeFont,bg="seashell1").place(x=390,y=245)
        bookString = StringVar()
        bookString.set("")
        self.bookEntry = Label(self,width= 40, text = "xxx")
        self.bookEntry.place(x=580,y=250)
        
        memberLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=380,y=295)
        memberId = StringVar()
        memberId.set("")
        self.memberIdEntry = Label(self,width= 40, text = "xxx")
        self.memberIdEntry.place(x=580,y=300)
        
        nameLabel = Label(self, text=" Member Name ", font = headerThreeFont,bg="seashell1").place(x=360,y=345)
        nameString = StringVar()
        nameString.set("")
        self.nameEntry = Label(self,width= 40, text = "xxx")
        self.nameEntry.place(x=580,y=350)
        
        dateLabel = Label(self, text=" Cancellation Date ", font = headerThreeFont,bg="seashell1").place(x=350,y=395)
        dateString = StringVar()
        dateString.set("")
        self.dateEntry = Label(self,width= 40, text = "xxx")
        self.dateEntry.place(x=580,y=400)
        
        def callReserve(accession_num,member_id, reserveDate, inputCur,inputConn):
            mysql.reserve_book(accession_num,member_id, reserveDate, inputCur,inputConn)
            successFrame(self.controller,"Book Reserved ", "Reserve " )
            return controller.show_frame("MakeReservation")
        # buttons
        reserveBookButton = tk.Button(self, text = "Confirm Reservation", font = buHeadings, bg="#A6934E", command= lambda: callReserve(to_send_book[0],member_reserve_send[0],reserve_date_send, cur,conn)).place(x=300, y=480)
        createBack(self.controller, buHeadings, 720, 480, self, "Reservations", "ReservationPage")

    def refresh(self):
        self.accIdEntry.config(text=to_send_book[0])
        self.bookEntry.config(text = to_send_book[1])
        self.memberIdEntry.config(text = member_reserve_send[0])
        self.nameEntry.config(text = member_reserve_send[1])
        self.dateEntry.config(text = reserve_date_send)

class CancelReservation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bg = tk.Label(self, image = bgImage)
        bg.place(x=0,y=0)

        #  header
        header = tk.Label(self, text = " To Cancel a Reservation, Please Enter Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
        header.place(x = 250, y = 100)

        # labels and text entry box
        accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=375,y=195)
        accessionNum = StringVar()
        accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
        accessionNumEntry.place(x=580,y=200)
        accessionNumEntry.get()
        accessionNumEntry.insert(0, " Used to identify an instance of book")

        membershipIDLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=245)
        membershipID = StringVar()
        membershipIDEntry = Entry(self, textvariable=membershipID,width= 40)
        membershipIDEntry.place(x=580,y=250)
        membershipIDEntry.get()
        membershipIDEntry.insert(0, " A unique alphanumeric id that distinguishes every member ")

        cancelDateLabel = Label(self, text=" Cancel Date ", font = headerThreeFont,bg="seashell1").place(x=410,y=295)
        cancelDate = StringVar()
        cancelDateEntry = Entry(self, textvariable=cancelDate,width= 40)
        cancelDateEntry.place(x=580,y=300)
        cancelDateEntry.get()
        cancelDateEntry.insert(0, " Date of Reservation Cancellation")

        # if the member has no such reservation
        # Reserves table -> memberid -> if memberid.get not in this then wrong
        def callCancelReserve(inputCur, inputConn):
            flagMemberReserve = False
            # get the global variables
            global to_send_memberid
            cur.execute('SELECT memberID FROM Reserves')
            all_member_reserves = cur.fetchall()
            for ele in all_member_reserves:
                if ele[0] == membershipID.get():
                    to_send_memberid = ele[0]
                    flagMemberReserve = True
            
#            print(to_send_memberid)
            if flagMemberReserve == False:
                return errorFrame(self.controller, "Member has no such reservation; Invalid Details", "Cancellation")
            
            # check to see if the book is reserved
            flagBookReserved = False
            cur.execute('SELECT accession_num FROM Reserves')
            all_books_reserves = cur.fetchall()
            for book_reserves in all_books_reserves:
                if book_reserves[0] == accessionNum.get():
                    flagBookReserved = True
            
            if flagBookReserved == False:
                return errorFrame(self.controller, "Book is not reserved; Invalid Details", "Cancellation")

            # to get the name of the member upon getting their member id
            global to_send_member_name
            cur.execute('SELECT * FROM Member')
            member_output = cur.fetchall()
            for ele in member_output:
                if ele[0]==to_send_memberid:
                    # i think it prints out a tuple of the member detail
                    to_send_member_name = ele[1]
                    
            print(to_send_member_name)
            
            # if book on loan can cancel
            # if book is not on loan AND reserved by the person , can't cancel
            flagBookOnLoan = False
            global to_send_book_acc
            cur.execute('SELECT accession_num FROM Loans')
            all_loaned_books = cur.fetchall()
            for ele in all_loaned_books:
                if ele[0] == accessionNum.get():
                    to_send_book_acc = ele[0]
                    flagBookOnLoan = True
            print(to_send_book_acc)


            if flagBookOnLoan == False:
                return errorFrame(self.controller, "Book is not on Loan", "Cancellation")


            global to_send_book_title
            cur.execute('SELECT * FROM Book')
            book_name = cur.fetchall()
            for booknames in book_name:
                if booknames[0] == to_send_book_acc:
                    to_send_book_title = booknames[1]
            
            print(to_send_book_title)

            # get the book title from the book acc number keyed in
            global cancel_reservation_date
            cancel_reservation_date = cancelDate.get()
            
            return controller.show_frame("ReservationCancellationConfirmationFrame")
        
        cancelreserveBookButton = tk.Button(self, text = "Cancel Reservation  ", font = buHeadings, bg="#A6934E", command= lambda: callCancelReserve(cur,conn)).place(x=300, y = 350)
        createBack(self.controller, buHeadings, 720, 400, self, "Reservation", "ReservationPage")
    
    def refresh(self):
        pass




class ReservationCancellationConfirmationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        confirmLabel = tk.Label(self, text = "Please Confirm Cancellation Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)
        #accession number
        accLabel = Label(self, text=" Accession Number ", font = headerThreeFont,bg="seashell1").place(x=320,y=195)
        accId = StringVar()
        accId.set("")
        self.accIdEntry = Label(self,width= 40, text = "xxx")
        self.accIdEntry.place(x=580,y=200)
        # memberIdEntry.insert(0, memberIdEntry)

        # self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
        bookLabel = Label(self, text=" Book Title ", font = headerThreeFont,bg="seashell1").place(x=390,y=245)
        bookString = StringVar()
        bookString.set("")
        self.bookEntry = Label(self,width= 40, text = "xxx")
        self.bookEntry.place(x=580,y=250)
        
        memberLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=380,y=295)
        memberId = StringVar()
        memberId.set("")
        self.memberIdEntry = Label(self,width= 40, text = "xxx")
        self.memberIdEntry.place(x=580,y=300)
        
        nameLabel = Label(self, text=" Member Name ", font = headerThreeFont,bg="seashell1").place(x=360,y=345)
        nameString = StringVar()
        nameString.set("")
        self.nameEntry = Label(self,width= 40, text = "xxx")
        self.nameEntry.place(x=580,y=350)
        
        dateLabel = Label(self, text=" Cancellation Date ", font = headerThreeFont,bg="seashell1").place(x=350,y=395)
        dateString = StringVar()
        dateString.set("")
        self.dateEntry = Label(self,width= 40, text = "xxx")
        self.dateEntry.place(x=580,y=400)
        
        def callCancelReserve(accession_num, member_id, date, cur, conn):
            mysql.cancel_reserve(accession_num, member_id, date, cur, conn)
            successFrame(self.controller, "Reservation Cancelled ", "Reservation")
            return controller.show_frame("Reservation")
                # cancel reserrve book button
    
        cancelreserveBookButton = tk.Button(self, text = "Cancel Reservation  ", font = buHeadings, bg="#A6934E", command= lambda: callCancelReserve(to_send_book_acc,to_send_memberid,cancel_reservation_date,cur, conn)).place(x=300, y = 500)
        createBack(self.controller, buHeadings, 720, 400, self, "Cancellation", "CancelReservation")


    def refresh(self):
        self.accIdEntry.config(text = to_send_book_acc)
        self.bookEntry.config(text = to_send_book_title)
        self.memberIdEntry.config(text = to_send_memberid)
        self.nameEntry.config(text = to_send_member_name)
        self.dateEntry.config(text = cancel_reservation_date)

class LoansPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# create picture
		self.canvas = Canvas(self, width = 625, height = 375)
		self.image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "Photos/Loans.jpeg")).resize((625,375)))
		self.canvas.create_image(300,175, image=self.image)
		self.canvas.place(x=100,y=175)

		# create header
		header = tk.Label(self, text = "Select one of the Options", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 450, y = 100)

		# create menu label
		loansLabel = tk.Label(self, text = "Loans", font = buHeadings, fg = "white", bg = "#4A7A8C" , borderwidth = 3, width = 10)
		loansLabel.place(x = 275,y=450)

		# Borrow
		borrowButton = tk.Button(self, text = "6. Borrow", font = headerOneFont, command = lambda: controller.show_frame("Borrow")).place(x = 750, y = 260)
		borrowLabel = tk.Label(self, text = "Book Borrowing", font = headerTwoFont)
		borrowLabel.place(x = 1000, y = 260)

		# Return
		returnButton = tk.Button(self, text = "7. Return", font = headerOneFont, command = lambda: controller.show_frame("BookReturn")).place(x = 750, y = 410)
		returnLabel = tk.Label(self, text = "Book Returning", font = headerTwoFont)
		returnLabel.place(x = 1000, y = 410)

		# Back to Main 
		createButtonMain(self.controller, headerThreeFont, 0, 0, self)
	def refresh(self):
		pass

class Borrow(tk.Frame):
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		self.controller = controller
		global accessionNumEntry, memberIdEntry
		global member_id_2
		global accession_num_2
		global title_2
		global name_2
		

		# add bg image
		bg = tk.Label(self, image = bgImage)
		bg.place(x=0,y=0)

		# header
		header = tk.Label(self, text = " To Borrow a Book, Please Enter Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
		header.place(x = 250, y = 100)
		
		# labels and text entry box
		membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=195)
		memberId = StringVar()
		memberIdEntry = Entry(self, textvariable=memberId,width= 40)
		memberIdEntry.place(x=580,y=200)
		memberIdEntry.insert(0, " A unique alphanumeric id that distinguishes every member")
		memberInput = memberIdEntry.get()

		accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=350,y=295)
		accessionNum = StringVar()
		accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
		accessionNumEntry.place(x=580,y=300)
		accessionNumEntry.insert(0, "")
		accessionNumInput= accessionNum.get()

		
        # buttons
		borrowBookutton = tk.Button(self, text = "Borrow Book", font = buHeadings, bg="#A6934E", command= lambda: callConfirmation(cur, conn)).place(x=300, y = 480)
		createBack(self.controller, buHeadings, 720, 480, self, "Loan", "LoansPage")
		
		
		def callConfirmation(cur, conn):
			global borrowTuple
			global detailsTuple
			member_id_2 = memberIdEntry.get()
			accession_num_2 = accessionNumEntry.get()
			

			if((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "no member"):
				functionCalled = errorFrame(self.controller, "No member found.", "Create")
				return functionCalled
			
			if((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "no book"):
				print(accession_num_2)
				functionCalled = errorFrame(self.controller, "No book found.", "Create")
				return functionCalled
			
			if((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "on loan"):

				cur.execute("SELECT dueDate FROM Loans WHERE accession_num = '{}'".format(accession_num_2))
				output = cur.fetchall()[0][0]
				output = "Book currently on loan until " + str(output)
				functionCalled = errorFrame(self.controller, output , "Create")
				return functionCalled
			
			if((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "reserved by member"):
				functionCalled = controller.show_frame("BorrowConfirmationFrame")
				borrowTuple = (memberIdEntry.get(), accessionNumEntry.get())
				detailsTuple = mysql.get_bookdetails(borrowTuple[1], cur, conn)
				member_id_2 = borrowTuple[0]
				accession_num_2 = borrowTuple[1]
				title_2 = detailsTuple[1]
				name_2  = mysql.get_name(borrowTuple[0], cur, conn)[1]
                                
				print("reserved by member")
				return functionCalled
			
			if((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "reserved"):
				functionCalled = errorFrame(self.controller, "Book currently reserved", "Create")
				return functionCalled
			
			elif((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "quota"):
				functionCalled = errorFrame(self.controller, "Member loan quota exceeded.", "Create")
				return functionCalled
			elif ((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "outstanding fine"):
				functionCalled = errorFrame(self.controller, "Member has outstanding fine.", "Create")
				return functionCalled
		    
			elif ((mysql.confirmation_borrow_book(member_id_2, accession_num_2, cur, conn)) == "can borrow"):
                                
				functionCalled = controller.show_frame("BorrowConfirmationFrame")
				borrowTuple = (memberIdEntry.get(), accessionNumEntry.get())
				detailsTuple = mysql.get_bookdetails(borrowTuple[1], cur, conn)
				member_id_2 = borrowTuple[0]
				accession_num_2 = borrowTuple[1]
				title_2 = detailsTuple[1]
				name_2  = mysql.get_name(borrowTuple[0], cur, conn)[1]
				
				return functionCalled
			else:
				functionCalled = errorFrame(self.controller, "Error in input details.", "Create")
                                                            
			return functionCalled
	def refresh(self):
		pass

class BorrowConfirmationFrame(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        confirmLabel = tk.Label(self, text = "Please Confirm Loan Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

        accLabel = Label(self, text=" Accession Number ", font = headerThreeFont,bg="seashell1").place(x=320,y=195)
        accId = StringVar()
        accId.set("")
        self.accIdEntry = Label(self,width= 40, text = "xxx")
        self.accIdEntry.place(x=580,y=200)
        # memberIdEntry.insert(0, memberIdEntry)

        # self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
        bookLabel = Label(self, text=" Book Title ", font = headerThreeFont,bg="seashell1").place(x=390,y=245)
        bookString = StringVar()
        bookString.set("")
        self.bookEntry = Label(self,width= 40, text = "xxx")
        self.bookEntry.place(x=580,y=250)
        
        memberLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=380,y=295)
        memberId = StringVar()
        memberId.set("")
        self.memberIdEntry = Label(self,width= 40, text = "xxx")
        self.memberIdEntry.place(x=580,y=300)
        
        nameLabel = Label(self, text=" Member Name ", font = headerThreeFont,bg="seashell1").place(x=360,y=345)
        nameString = StringVar()
        nameString.set("")
        self.nameEntry = Label(self,width= 40, text = "xxx")
        self.nameEntry.place(x=580,y=350)
        
        dateLabel = Label(self, text=" Borrow Date ", font = headerThreeFont,bg="seashell1").place(x=350,y=395)
        dateString = StringVar()
        dateString.set("")
        datestring = mysql.get_date(cur,conn)
        dateEntry = Label(self,width= 40, text = datestring)
        dateEntry.place(x=580,y=400)

        duedateLabel = Label(self, text=" Due Date ", font = headerThreeFont,bg="seashell1").place(x=350,y=445)
        duedateString = StringVar()
        duedateString.set("")
        duestring = mysql.get_duedate(cur,conn)
        duedateEntry = Label(self,width= 40, text = duestring)
        duedateEntry.place(x=580,y=450)

        
        def callBorrow(accession_num,member_id, inputCur,inputConn):

            if((mysql.confirmation_borrow_book(member_id, accession_num, inputCur, inputConn)) == "reserved by member"):
                    cur.execute("DELETE FROM Reserves WHERE accession_num = '{}' AND memberID = '{}'".format(accession_num, member_id))
                    conn.commit()
            mysql.borrow_book(member_id, accession_num, inputCur,inputConn)
            successFrame(self.controller,"Book Borrowed ", "Borrow " )
            return controller.show_frame("Borrow")
        # buttons
        borrowBookButton = tk.Button(self, text = "Borrow Book", font = buHeadings, bg="#A6934E", command= lambda: callBorrow(borrowTuple[1], borrowTuple[0], cur,conn)).place(x=300, y=480)
        createBack(self.controller, buHeadings, 720, 480, self, "borrow", "Borrow")

			
    def refresh(self):
        borrowTuple = (memberIdEntry.get(), accessionNumEntry.get())
        detailsTuple = mysql.get_bookdetails(borrowTuple[1], cur, conn)
		
        self.accIdEntry.config(text= borrowTuple[1])
        self.bookEntry.config(text = detailsTuple[1])
        self.memberIdEntry.config(text = borrowTuple[0])
        self.nameEntry.config(text = mysql.get_name(borrowTuple[0], cur, conn)[1])
        
class BookReturn(tk.Frame):
        def __init__(self, parent, controller):
                global bookTuple
                tk.Frame.__init__(self, parent)
                self.controller = controller

                bg = tk.Label(self, image = bgImage)
                bg.place(x=0,y=0)
                #  header
                header = tk.Label(self, text = " To Return A Book, Please Enter Information Below:", font = headerOneFont, fg = "black", bg ="#BB7793")
                header.place(x = 250, y = 100)

                # labels and text entry box
                accessionNumLabel = Label(self, text="Accession Number", font = headerThreeFont, bg="seashell1").place(x=375,y=195)
                accessionNum = StringVar()
                accessionNumEntry = Entry(self, textvariable=accessionNum,width= 40)
                accessionNumEntry.place(x=580,y=200)
                accessionNumEntry.insert(0, " Used to identify an instance of book")

                returnDateLabel = Label(self, text=" Return Date ", font = headerThreeFont,bg="seashell1").place(x=440,y=245)
                returnDateString = StringVar()
                returnDateEntry = Entry(self, textvariable=returnDateString,width= 40)
                returnDateEntry.place(x=580,y=250)
                returnDateEntry.insert(0, " Date of Book Return")
                
                def callReturnBookConfirmation(inputCur, inputConn):
                        global bookTuple
                        bookTuple = (accessionNumEntry.get(), returnDateEntry.get())
                        global accession_num_2, return_date_2
                        accession_num_2 = bookTuple[0]

                        return_date_2  = bookTuple[1]
                        global title, memberID, name, amount_to_add

                        detailsTuple = mysql.get_bookdetails(bookTuple[0], cur, conn)
                        print(detailsTuple)
                        title = detailsTuple[1]

                        loandetails = mysql.get_loandetails(bookTuple[0], cur, conn)
                        
                        if loandetails == ():
                                functionCalled = errorFrame(self.controller, " Book not on loan", "Return Function")
                                
                        else :
                                memberID = loandetails[0]
                                due = loandetails[3]
                                name = mysql.get_name(memberID, cur, conn)[1]
                                cur.execute("SELECT DATEDIFF('{}', '{}')".format(bookTuple[1], due))
                                amount_to_add = cur.fetchone()[0]
                                if amount_to_add < 0:
                                        amount_to_add = 0
##                                print("amount_to_add part 1")
##                                print(amount_to_add)
##
##                                if amount_to_add == None or amount_to_add <0:
##                                        amount_to_add = 0
##
##                                if amount_to_add != 0:
        
##                                        functionCalled = errorFrame(self.controller, " Book returned successfully but has fines", "Return Function")
##                                
##                                else:
##                                        
##                                        cur.execute('INSERT INTO Fine VALUES ("{}", "{}")'.format(memberID, amount_to_add))
##                                        conn.commit()
##                                        cur.execute("DELETE FROM Loans WHERE accession_num = '{}'".format(accession_num))
##                                        conn.commit()
##                                        functionCalled = errorFrame(self.controller, " Book returned successfully but has fines", "Return Function")
                                functionCalled = controller.show_frame("ReturnBookConfirmationFrame")
                                        
                        return functionCalled
        
                # buttons
                returnBookButton = tk.Button(self, text = "Return Book", font = buHeadings, bg="#A6934E", command= lambda: callReturnBookConfirmation(cur,conn)).place(x=300, y = 520)
                createBack(self.controller, buHeadings, 720, 520, self, "Loans", "LoansPage")


        def refresh(self):
                pass

class ReturnBookConfirmationFrame(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                self.controller = controller

                confirmLabel = tk.Label(self, text = "Please Confirm Return Details To Be Correct" , font=headerOneFont, bg="green").pack(pady=25)

                accessionNumLabel = Label(self, text=" Accession Number ", font = headerThreeFont,bg="seashell1").place(x=400,y=195)
                accessionNum = StringVar()
                accessionNum.set("")
                self.accessionNumEntry = Label(self,width= 40, text = "xxx") 
                self.accessionNumEntry.place(x=580,y=200)
                # memberIdEntry.insert(0, memberIdEntry)

                # self.membershipIdLabel = Label(self, text="Membership ID", font = headerThreeFont, bg="seashell1").place(x=400,y=300)
                titleLabel = Label(self, text=" Book Title ", font = headerThreeFont,bg="seashell1").place(x=400,y=245)
                titleString = StringVar()
                titleString.set("")
                self.titleEntry = Label(self,width= 40, text = "xxx")
                self.titleEntry.place(x=580,y=250)

                memberIDLabel = Label(self, text=" Membership ID ", font = headerThreeFont,bg="seashell1").place(x=400,y=295)
                memberIDString = StringVar()
                memberIDString.set("")
                self.memberIDEntry = Label(self,width= 40, text = "xxx")
                self.memberIDEntry.place(x=580,y=300)

                memberNameLabel = Label(self, text=" Member Name ", font = headerThreeFont,bg="seashell1").place(x=400,y=345)
                memberNameLString = StringVar()
                memberNameLString.set("")
                self.memberNameLEntry = Label(self,width= 40, text = "xxx")
                self.memberNameLEntry.place(x=580,y=350)

                returnDateLabel = Label(self, text=" Return Date ", font = headerThreeFont,bg="seashell1").place(x=400,y=395)
                returnDateString = StringVar()
                returnDateString.set("")
                self.returnDateEntry = Label(self,width= 40, text = "xxx")
                self.returnDateEntry.place(x=580,y=400)

                fineLabel = Label(self, text=" Fine: ", font = headerThreeFont,bg="seashell1").place(x=400,y=445)
                fineString = StringVar()
                fineString.set("")
                self.fineEntry = Label(self,width= 40, text = "xxx")
                self.fineEntry.place(x=580,y=450)


                # buttons
                cofirmReturnButton = tk.Button(self, text = "Confirm Return", font = buHeadings, bg="#A6934E", command= lambda: callReturn(memberID, bookTuple[0], bookTuple[1], amount_to_add, cur,conn)).place(x=300, y = 480)
                createBack(self.controller, buHeadings, 720, 480, self, "Loans", "LoansPage")


                def callReturn(memberID, accession_num, returnDate,amount,cur,conn):
                        
                        loandetails = mysql.get_loandetails(bookTuple[0], cur, conn)
                        due = loandetails[3]

                        if int(amount) > 0:
                                cur.execute('SELECT memberID FROM fine')
                                output= cur.fetchall()
                                fined_members = ()
                                for tpl in output:
                                        for member in tpl:
                                                fined_members += (member,)
                                if memberID in  fined_members:
                                        cur.execute("SELECT paymentAmount FROM Fine WHERE memberID = '{}'".format(memberID))
                                        current_amount = cur.fetchall()[0][0]
                                        print(current_amount)
                                        cur.execute("UPDATE FINE SET paymentAmount = '{}' WHERE memberID = '{}'".format(current_amount + amount, memberID))
                                        conn.commit()
                                        
                                else:
                                        cur.execute("INSERT INTO Fine VALUES ('{}', '{}')".format(memberID, amount))
                                        conn.commit()
                                cur.execute("DELETE FROM Loans WHERE accession_num = '{}'".format(accession_num))
                                conn.commit()
                                return errorFrame(self.controller,"Book Returned but with fines ", "BookReturn" )
                
                        cur.execute("DELETE FROM Loans WHERE accession_num = '{}'".format(accession_num))
                        conn.commit()
                        successFrame(self.controller,"Book Returned ", "Loans" )
                        
                        return controller.show_frame("BookReturn")
                        

        def refresh(self):
                self.accessionNumEntry.config(text=accession_num_2)
                #bookTitle = cur.execute('SELECT title FROM Books WHERE accession_num = "{}"'.format(accession_num_2)).fetchone()[0]
                self.titleEntry.config(text = title)
                #member_ID = cur.execute('SELECT memberID FROM Loans WHERE accession_num = "{}"'.format(accession_num_2)).fetchone()[0]
                self.memberIDEntry.config(text=memberID)
                #name = cur.execute('SELECT name FROM Member WHERE ID = "{}"'.format(member_ID).fetchone()[0]
                self.memberNameLEntry.config(text=name)    
                self.returnDateEntry.config(text=return_date_2)
                self.fineEntry.config(text=amount_to_add)
                self.fine = amount_to_add
     
                                   



if __name__ == "__main__":
    app = aLibrarySystem()
    app.mainloop()

conn.close()
