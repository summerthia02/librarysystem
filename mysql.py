import pymysql
from datetime import *


# To connect MySQL database
try:
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = 'password',
        db='ALibrarySystem',
        )
      
    cur = conn.cursor()
    print("connected to latest!")
except:
    print("error in connection!")
    

####Member####
def create_member(memberid, name, faculty, phone, email, cur, conn):
    print(memberid, name, faculty, phone, email)
    if (memberid == "" or name == "" or faculty == "" or phone == "" or email == ""):
        print("Error! Member already exist; Missing or Incomplete fields")
        return False
    try:
        cur.execute("INSERT INTO Member VALUES ('{}',' {}', '{}', '{}', '{}')".format(memberid, name, faculty, phone, email))
        conn.commit()
        print("Success! ALS Membership created")
        return True

    except:
        print("Error! Member already exist; Missing or Incomplete fields")
        return False
   
 #test create_member
#create_member("A002B", "Sherlock Holmes" ,"","44327676","elementarydrw@als.edu", cur, conn) #test for empty string
#create_member("A101B", "Sherlock Holmes" ,"Law","44327676","elementarydrw@als.edu", cur, conn)

def confirmation_delete_member(ID, cur, conn):
    try:
        cur.execute("SELECT * FROM Member WHERE ID = '{}'".format(ID))
        member_details = cur.fetchall()[0]
        print("confirm details: ")
        print(member_details)
        #return in tuple format (memberid, name, faculty, phone, email) 
        return member_details
    except:
        return False

#confirmation_delete_member("A201B", cur, conn)
    
def member_exists(ID, cur, conn):
    cur.execute("SELECT * FROM Member")
    output = cur.fetchall()
    for ele in output:
        if ele [0]== ID:
            return True
    return False

def delete_member(ID, cur, conn):
    try:
        cur.execute("DELETE FROM Member WHERE ID = '{}'".format(ID))
        conn.commit()
        print('deleted')
        return True
    except:
        print("Member has loans, reservations or outstanding fines.")
        return False

#delete_member("A201B", cur, conn)
#first page of update page where user inputs member_ID, checks to see if member exists
    
def can_update(ID, cur, conn):
    cur.execute("SELECT ID FROM Member")
    output = cur.fetchall()
    all_ID = []
    for tpl in output:
        all_ID.append(tpl[0])
    print(all_ID)
    if ID not in all_ID:
        print("ID not in database")
        return False
    print("ID found")
    return True

#print(can_update("A101A", cur, conn))

#prints confirmation page, return output is a tuple 
def confirmation_update_member(ID, name, faculty, number, email, cur, conn):
    return((ID, name, faculty, number, email))

#updates member in database
def update_member(ID, name, faculty, number, email, cur, conn):
    try:
        cur.execute("UPDATE Member SET name = '{}', faculty = '{}', phone = '{}', email = '{}' WHERE ID = '{}'".format(name, faculty, number, email, ID))
        conn.commit()
        print("Success! ALS Membership Updated.")
        return True
    except:
        print("Error! Missing or Incomplete fields.")
        return False
    
#update_member("A101A","ur mudder", "bza","1223444","fly@als.edu", cur, conn)
#update_member("A101A","Hermione Granger", "Science","33336663","flying@als.edu", cur, conn) #change back to original
#### Fines ##
### user input (id, fineAmount)

def add_fine(member_id, date, amount, cur, conn):
    #check if member already has existing fine
    cur.execute("SELECT memberID FROM Fine")
    output = cur.fetchall()
    all_ID = []
    
    for tpl in output:
        all_ID.append(tpl[0])
    if member_id in all_ID:
        cur.execute("SELECT paymentAmount FROM Fine WHERE memberID = '{}'".format(member_id))
        current_amount = cur.fetchone()[0]
        if current_amount == None:
            current_amount = 0
        sql = "UPDATE Fine SET paymentAmount = '{}' WHERE memberID = '{}'".format(current_amount + amount, member_id)
        print("updated amount is: " + str(int(current_amount)+int(amount)))
        
    else:
        sql = "INSERT INTO Fine VALUES ('{}', '{}')".format(member_id, amount)
        print("amount set: " + str(amount))

    try:
        cur.execute(sql)
        conn.commit()
        print("fine added")
        return True
    except:
        print("cannot add fine")
        return False
    
#confirmation_pay_fine checks for NO FINE and INCORRECT AMOUNT, if no error, prints confirmation  
def confirmation_pay_fine(member_id, date, amount, cur, conn):
    cur.execute("SELECT ID FROM Member")
    output = cur.fetchall()
    all_ID = []
    for tpl in output:
        all_ID.append(tpl[0])
    print(all_ID)
    if member_id not in all_ID:
        print(member_id + "no such member")
        return "no member"
    
    cur.execute("SELECT memberID FROM Fine")
    output = cur.fetchall()
    all_ID = []
    for tpl in output:
        all_ID.append(tpl[0])
    print(all_ID)
    if member_id not in all_ID:
        print("Member has no fine")
        return "no fine"
    
    #check for amount
    cur.execute("SELECT paymentAmount FROM Fine WHERE memberID = '{}'".format(member_id))
    current_amount = cur.fetchone()[0]
    if int(current_amount) != int(amount):
        print("amount entered: " + str(amount))
        print ("correct should be: " + str(current_amount))
        print("incorrect amount.")
        return "incorrect amount"
    
    else:
        print("confirm details: ")
        output = (current_amount, member_id, date)
        print(output)
        return "true"
#confirmation_pay_fine("A101B", "12345678", 2, cur, conn)

def pay_fine(member_id, date, amount, cur, conn):
    print("pay_fine running")
    try:
        cur.execute("DELETE FROM Fine WHERE memberID = '{}'".format(member_id))
        conn.commit()
        cur.execute("INSERT INTO Payment VALUES ('{}', '{}', '{}')".format(member_id, date, amount));
        conn.commit()
        print("fine paid")
        return True
    except:
        print("error")
        return False
    

#pay_fine("A101A", "2022-03-10", 2, cur, conn)
####Book####
#authors is in tuple format !!
def add_book(accession_num, title, authors, isbn, publisher, publication_year, cur, conn):
    try:
        sql = "INSERT INTO Book VALUES ('{}', '{}', '{}', '{}', '{}')".format(accession_num, title, isbn, publisher, publication_year)
        cur.execute(sql)
        conn.commit()
        for author in authors:
            cur.execute("INSERT INTO Author VALUES ('{}', '{}')".format(author, accession_num))
            conn.commit()
        print("Book added!")
        return True
    except:
        print("Error! Book already added; Duplicate, Missing or Incomplete fields.")
        return False

#test add_book() 
#print(add_book('A04','Crime and Punishment',('Fyodor Dostoevsky',), '9790000000004','Penguin',2002, cur, conn))
#print(add_book("A01","A 1984 Story", ("George Orwell",), "9790000000001","Intra S.r.l.s.",2021, cur, conn))
    
#confirmation page, returns tuple of information required
def confirmation_withdraw_book(accession_num, cur, conn):
    try:
        cur.execute("SELECT * FROM Book WHERE accession_num = '{}'".format(accession_num))
        output = cur.fetchall()
        if output == ():
            print("cannot find book")
            return False
        print("confirm details: ")
        print(output)
        return output
    except:
        print("cannot find book")
        return False
    
#confirmation_withdraw_book("A01", cur, conn)
#confirmation_withdraw_book("A04", cur, conn) 

def withdraw_book(book_num, cur, conn):
    #check if book is on loan
    cur.execute("SELECT accession_num FROM Loans")
    output = cur.fetchall()
    for tpl in output:
        for accession_num in tpl:
            if accession_num == book_num:
                print("Error! Book is currently on loan.")
                return 0
    #Check if book is on reserve
    cur.execute("SELECT accession_num FROM Reserves")
    output = cur.fetchall()
    for tpl in output:
        for accession_num in tpl:
            if accession_num == book_num:
                print("Error! Book is currently Reserved.")
                return 1
            
    #passed checks, can withdraw book
    
    cur.execute("DELETE FROM Book WHERE accession_num = '{}' ".format(book_num))
    conn.commit()
    cur.execute("DELETE FROM Author WHERE accession_num = '{}'".format(book_num))
    conn.commit()
    print("book withdrawn")
    return True
#test withdraw_book(book, cur, conn)
#withdraw_book("A01", cur, conn)


def confirmation_borrow_book(member_ID, book_num, cur, conn):
    #check if member exists
    if (can_update(member_ID, cur, conn)) == False:
        return ("no member")
    #check if book exists
    print("acc_num entered: " + book_num)
    cur.execute("SELECT * FROM Book WHERE accession_num = '{}'".format(book_num))
    output = cur.fetchall()
    print(output)
    if output == ():
        print("cannot find book")
        return ("no book")
    #check if book is on loan
    cur.execute("SELECT accession_num FROM Loans")
    output = cur.fetchall()
    for tpl in output:
        for accession_num in tpl:
            if accession_num == book_num:
                cur.execute("SELECT dueDate FROM Loans WHERE accession_num = '{}'".format(book_num))
                output = cur.fetchall()[0][0]
                print("Error! Book is currently on loan until " + str(output) )
                return ("on loan")
    
    
    #check if member has already 2 books on loan
    cur.execute("SELECT COUNT(accession_num) FROM Loans WHERE memberID = '{}'".format(member_ID))
    num_loans = cur.fetchall()[0][0]
    print(num_loans)
    if num_loans > 1:
        print("Member loan quota exceeded.")
        return ("quota")

    #check if book is already on reserve
    cur.execute("SELECT accession_num FROM Reserves")
    output = cur.fetchall()

    for tpl in output:
        for accession_num in tpl:
            if accession_num == book_num:
                cur.execute("SELECT memberID FROM Reserves WHERE accession_num = '{}'".format(book_num))
                member = cur.fetchall()[0][0]
                print(member)
                if member != member_ID:
                    return ("reserved")
                else:
                    return ("reserved by member")

    
    #check if member has outstanding fines
    cur.execute("SELECT memberID FROM Fine")
    output = cur.fetchall()
    fined_members = ()
    for tpl in output:
        for member in tpl:
            fined_members += (member,)
    if member_ID in fined_members:
        return ("outstanding fine")


    #pass all checks, borrow book
    return ("can borrow")
#print(confirmation_borrow_book("A201B", "A04", cur, conn))

def borrow_book(member_ID, book_num, cur, conn):
    print(datetime.today().strftime('%Y-%m-%d'))
    cur.execute('SELECT CURDATE()')
    date = cur.fetchall()[0][0]
    cur.execute('SELECT DATE_ADD("{}", INTERVAL 14 DAY)'.format(date))
    due = cur.fetchone()[0]
    cur.execute("INSERT INTO Loans VALUES ('{}', '{}', '{}', '{}', NULL)".format(member_ID, book_num, date, due))
    conn.commit()
    print("book borrowed")
    return ("book borrowed")
#test borrow_book
#mem = ("A101A","Hermione Granger", "Science","33336663","flying@als.edu")
#book = ('A01', 'A 1984 Story', '9790000000001', 'Intra S.r.l.s.', 2021)
#confirmation_borrow_book("A101A", "A01", cur, conn) #test case for book on loan
#confirmation_borrow_book("A101A", "A01", cur, conn)
#borrow_book("A201B", "A04", cur, conn)
#print(confirmation_borrow_book("A201B", "A06", cur, conn))
def confirmation_return_book(book_num, date, cur, conn):
    try:
        cur.execute("SELECT accession_num, title FROM Book WHERE accession_num = '{}'".format(book_num))
        output = cur.fetchall()
        accession_num, title = output[0][0], output[0][1]

        
        cur.execute('SELECT memberID FROM Loans WHERE accession_num = "{}"'.format(book_num))
        output = cur.fetchall()
        memberID = output[0][0]
        cur.execute('SELECT name FROM Member WHERE ID = "{}"'.format(memberID))
        output = cur.fetchall()[0]
        name = output[0][0]
        cur.execute('SELECT dueDate FROM Loans WHERE accession_num = "{}"'.format(book_num))
        due = cur.fetchone()[0]
        cur.execute("SELECT DATEDIFF('{}', '{}')".format(date, due))
        amount_to_add = cur.fetchone()[0]
        if amount_to_add == None or amount_to_add <0:
            amount_to_add = 0
        output = (accession_num, title, memberID, name, date, amount_to_add)
        
        print("confirm details:")
        print(output)
        return output

    
    except:
        print("error in confirmation")
        return False

#confirmation_return_book("A02", "12345678", cur, conn)

def return_book(book_num, date, cur, conn):
    cur.execute('SELECT dueDate FROM Loans WHERE accession_num = "{}"'.format(book_num))
    due = cur.fetchone()[0]
    print(due)
    #check if book is overdue, if yes add fine
    cur.execute("SELECT DATEDIFF('{}', '{}')".format(date, due)) 
    amount_to_add = cur.fetchone()[0]
    
    if amount_to_add > 0: 
        cur.execute('SELECT memberID FROM Loans WHERE accession_num = "{}"'.format(book_num))
        memberID = cur.fetchone()[0]
        add_fine(memberID, date, amount_to_add, cur, conn) #calls add_fine() function which updates member's fine records
        print("Error! Book returned successfully but has fines.")
        return False
        
    #to return, delete book from loans table
    cur.execute("DELETE FROM Loans WHERE accession_num = '{}'".format(book_num))
    conn.commit()
    return True

 #test return_book   
#return_book('A02', '20220330', cur, conn)

## Reservation ##

#confirmation page
def confirmation_reserve_book(accession_num, member_id, reserveDate, cur, conn):
    try:
        cur.execute("SELECT accession_num, title FROM Book WHERE accession_num = '{}'".format(accession_num))
        book_details = cur.fetchone()
        cur.execute("SELECT ID, name FROM Member WHERE id = '{}'".format(member_id))
        member_details = cur.fetchone()
        print("Confirm reservation details to be correct:")
        output = (book_details[0], book_details[1], member_details[0], member_details[1], reserveDate)
        print(output)
        return output
    except:
        print("error in confirmation!")
        return False
    
#confirmation_reserve_book("A01","A101A", "2022-03-09", cur, conn)

def can_reserve_book(accession_num, member_id, reserveDate, cur, conn):

    try:
        #check if member has outstanding fines
        cur.execute("SELECT memberID FROM Fine")
        output = cur.fetchall()
        if output:
            for tpl in output:
                for value in tpl:
                    if value == member_id:
                        cur.execute("SELECT paymentamount FROM Fine WHERE memberID = '{}'".format(member_id))
                        output = cur.fetchone()[0]
                        if output:
                            print("Member has outstanding fine of $'{}'".format(output))
                            return 0
                
        #check if member already has 2 reserved books
        cur.execute ("SELECT COUNT(memberID) FROM Reserves WHERE memberID = '{}'".format(member_id))
        num_reserved = cur.fetchone()[0]
        if num_reserved >= 2:
            print("Member currently has 2 books on reservation")
            return 1
        
        #check if book is already in reserve
        cur.execute("SELECT accession_num FROM Reserves")
        currently_reserved = cur.fetchall()[0]
        print(currently_reserved)
        if accession_num in currently_reserved:
            print("book is already reserved")
            return 2
        
        else:
            return True
    except:
        print("error in trying to reserve")

def reserve_book(accession_num,member_id, reserveDate, cur, conn):
    if can_reserve_book(member_id, accession_num, reserveDate, cur, conn) == False:
        return False
    try:
        cur.execute("INSERT INTO Reserves VALUES ('{}', '{}', '{}')".format(member_id, accession_num, reserveDate))
        conn.commit()
        print("book reserved")
        return True
    except:
        print("error")
        return False
    
    
#print(can_reserve_book("A01", "A202B", "2022-03-09", cur, conn)) #book is already reserved
#reserve_book("A01", "A101A", "2022-03-09", cur, conn)

def confirmation_cancel_reserve(accession_num, member_id, date, cur, conn):
    try:
        cur.execute("SELECT accession_num, title FROM Book WHERE accession_num = '{}'".format(accession_num))
        book_details = cur.fetchone()
        cur.execute("SELECT ID, name FROM Member WHERE id = '{}'".format(member_id))
        member_details = cur.fetchone()
        print("Confirm cancellation details to be correct:")
        output = (book_details[0], book_details[1], member_details[0], member_details[1], date)
        print(output)
        return output
    except:
        print("error in confirmation!")
        return False
    
#confirmation_cancel_reserve("A01","A101A", "2022-03-09")

def cancel_reserve(accession_num, member_id, date, cur, conn):
    try:
        cur.execute("DELETE FROM Reserves WHERE accession_num = '{}' AND memberID = '{}'".format(accession_num, member_id))
        print("cancelled reservation")
        conn.commit()
        return True
    except:
        print("error.")
        return False
        
#cancel_reserve("A101A", "A01", "2022-03-09", cur, conn)
    

###REPORT####

#output is a tuple of tuples, each tuple represents 1 book
def book_search(category, user_input, cur, conn):
    try:
        if category ==  'Authors':
            cur.execute("SELECT * FROM Book WHERE accession_num = (SELECT accession_num FROM Author WHERE name = '{}')".format(user_input))
            output = cur.fetchall()
        else: 
            cur.execute("SELECT * FROM Book WHERE {} = '{}'".format(category, user_input))
            output = cur.fetchall()
        
        print(output[0])
        return(output[0])
    
    except:
        print("error")
        return False
    
#test book_search
#book_search('Authors', 'Aldous Huxley', cur, conn)
#book_search('ibsn', "9790000000002", cur, conn)

#no choice cannot get authors for this becos our tbl put author separate
#output is a tuple of tuples, each tuple represents 1 book
def books_onloan(cur, conn):
    try:
        cur.execute("SELECT * FROM Book WHERE accession_num = (SELECT accession_num FROM Loans)")
        output = cur.fetchall()
        print(output)
        return (output)
    except:
        print("error")
        return False
#books_onloan(cur,conn)

def books_onreserves(cur, conn):
    try:
        cur.execute("SELECT * FROM Book WHERE accession_num IN (SELECT accession_num FROM Reserves)")
        output = cur.fetchall()
        print(output)
        return (output)
    except:
        print("error")
        return False

#books_onreserves(cur, conn)

#members with outstanding fines
def fined_members(cur, conn):
    try:
        cur.execute("SELECT * FROM Member WHERE ID = (SELECT memberID FROM Fine)")
        output = cur.fetchall()
        
        print(output)
        return output
    except:
        print("error")
        return False

#fined_members(cur, conn)

#books on loan to member
def member_loans(ID, cur, conn):
    try:
        cur.execute("SELECT * FROM Book WHERE accession_num = (SELECT accession_num FROM Loans WHERE memberID = '{}')".format(ID))
        output = cur.fetchall()
        print(output)
        return output
    except:
        print("error")
        return False
#member_loans("A101A", cur, conn)

def get_duedate(cur, conn):
    cur.execute('SELECT CURDATE()')
    date = cur.fetchall()[0][0]
    cur.execute('SELECT DATE_ADD("{}", INTERVAL 14 DAY)'.format(date))
    due = cur.fetchall()[0][0]
    return due
#get_duedate(cur, conn)

def get_bookdetails(accession_num, cur, conn):
    cur.execute("SELECT * FROM Book WHERE accession_num  = '{}'".format(accession_num))
    output = cur.fetchall()[0]
    print(output)
    return output

def get_name(memberid, cur,conn):
    cur.execute("SELECT * FROM Member WHERE id  = '{}'".format(memberid))
    output = cur.fetchall()[0]
    print(output)
    return output
def get_date(cur,conn):
    cur.execute('SELECT CURDATE()')
    date = cur.fetchall()[0][0]
    return date

def confirmation_return_book(book_num, date, cur, conn):
    try:
        cur.execute("SELECT accession_num, title FROM Book WHERE accession_num = '{}'".format(book_num))
        output = cur.fetchall()
        accession_num, title = output[0][0], output[0][1]

        
        cur.execute('SELECT memberID FROM Loans WHERE accession_num = "{}"'.format(book_num))
        output = cur.fetchall()
        memberID = output[0][0]
        cur.execute('SELECT name FROM Member WHERE ID = "{}"'.format(memberID))
        output = cur.fetchall()[0]
        name = output[0][0]
        cur.execute('SELECT dueDate FROM Loans WHERE accession_num = "{}"'.format(book_num))
        due = cur.fetchone()[0]
        cur.execute("SELECT DATEDIFF('{}', '{}')".format(date, due))
        amount_to_add = cur.fetchone()[0]
        if amount_to_add == None or amount_to_add <0:
            amount_to_add = 0
        output = (accession_num, title, memberID, name, date, amount_to_add)
        
        print("confirm details:")
        print(output)
        return output

    
    except:
        print("error in confirmation")
        return False

def get_duedate(cur, conn):
    cur.execute('SELECT CURDATE()')
    date = cur.fetchall()[0][0]
    cur.execute('SELECT DATE_ADD("{}", INTERVAL 14 DAY)'.format(date))
    due = cur.fetchall()[0][0]
    return due
#get_duedate(cur, conn)

def get_bookdetails(accession_num, cur, conn):
    cur.execute("SELECT * FROM Book WHERE accession_num  = '{}'".format(accession_num))
    output = cur.fetchall()
    book =()
    print("book details")
    for tpl in output:
        for bk in tpl:
            book += (bk,)
    print(book)
    return book

def get_loandetails(accession_num, cur, conn):
    cur.execute("SELECT * FROM Loans WHERE accession_num  = '{}'".format(accession_num))
    output = cur.fetchall()
    book =()
    for tpl in output:
        for b in tpl:
            book += (b,)
    print(book)
    return book

def get_name(memberid, cur,conn):
    cur.execute("SELECT * FROM Member WHERE id  = '{}'".format(memberid))
    output = cur.fetchall()[0]
    print(output)
    return output
def get_date(cur,conn):
    cur.execute('SELECT CURDATE()')
    date = cur.fetchall()[0][0]
    return date


get_bookdetails("A02", cur, conn)
#get_name("A101A", cur, conn)
# To close the connection
#conn.close()

