#limit 3 -->only 3 records 
#offset 2 -->skip 2 and start from 3

#after creating the database , we open it in the DB BROWSER (SQLITE)
#then all the tables we have created will be shown 
#---------------------------------
#connect to the database 
import sqlite3
db=sqlite3.connect("simpleSkillsApp.db")
#setting up the cursor
cr=db.cursor()



def commit_and_close():
    db.commit()
    db.close()
    print("connection to the Database has been closed  ")



uid=1
inputMessage="""
Welcome to Skills Application ,
What do you want to do ?
"s" =>Show All Skills
"a" => Add New skills
"d"=> Delete a skill
"u"=> update a skill
"q"=> Quit the App
====> PLEASE CHOOSE OPTION :  
"""



user_input=input(inputMessage).strip().lower()

command_list=["s","a","d","u","q"]


#define the methods
def show_skills():
    cr.execute(f"SELECT * FROM skillsTbl WHERE user_id='{uid}'") #''
    results=cr.fetchall()
    print(f"you have {len(results)} skills ")
    if len(results)>0:
        print("showing skills with progress")
    for row in results:
        print(f"userid=>{row[0]}")
        print(f"skillName => {row[1]},",end=" ")
        print(f"progress =>{row[2]}%")
        
    commit_and_close()



def add_skills():
    sk=input("Write skill name:").strip().capitalize()
    cr.execute(f"SELECT * FROM skillsTbl WHERE user_id='{uid}' AND skillName ='{sk}'")
    results=cr.fetchone()

    if results==None: 
        prog=input("Write skill progress").strip()
        cr.execute(f"INSERT INTO skillsTbl (user_id,skillName,progress)VALUES ('{uid}','{sk}','{prog}')") #''
        print("SKILL ADDED ")
    else:
        print("you cant add it ")
    commit_and_close()


def delete_skill():
    sk=input("write skill name ").strip().capitalize()
    cr.execute(f" DELETE FROM skillsTbl WHERE user_id= '{uid}' and skillName='{sk}'")
    print("SKILL DELETED ")
    commit_and_close()

def update_skill():
    sk=input("write skill name ").strip().capitalize()
    prog=input("please enter new skill progress ")
    cr.execute(f"UPDATE skillsTbl SET progress='{prog}' WHERE skillName='{sk}' AND user_id='{uid}'")
    print("skill updated")
    commit_and_close()


#check command  if exist :
if user_input in command_list:
    print("COMMAND FOUND")
    if user_input=="a":
        add_skills()
    elif user_input=="s":
        show_skills()
    elif user_input=="d":
        delete_skill()
    elif user_input=="u":
        update_skill()
    else:
        commit_and_close()
else:
    print(f"sorry this  COMMAND \"{user_input}\" not found ")