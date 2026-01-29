from datetime import date
menu="""
    ---------EDUTECH - STUDENT ATTENDANCE MANAGEMENT SYSTEM--------
             
              PRESS 1 FOR ATTENDANCE MARKING
              PRESS 2 FOR INDIVIDUAL STUDENT ATTENDANCE REPORT
              PRESS 3 FOR WHOLE CLASS ATTENDANCE REPORT
              PRESS 4 FOR EXIT
"""
attendance=[]#creating list of dictionaries

def mark_attendance():#function for attendance marking
   roll_no=int(input("Enter student roll no: "))
   attendance_date = input("Enter date (DD-MM-YYYY): ").strip()
    # Format check
   try:
        date.strptime(attendance_date, "%d-%m-%Y")
        today_d=date.today()
        today_d=today_d.strftime("%d-%m-%Y")
        if attendance_date>today_d:
            print("Future date attendance cannot be entered.")
            return
   except ValueError:
        print(" Invalid date format")
        return

    # Duplicate check
   for record in attendance:
        if record["Roll_no"] == roll_no and record["date"] == attendance_date:
            print(" Attendance already marked for this date")
            return
   name=input("Enter student name: ")
   course=input("Enter course name: ")
   status=input("Enter attendance(P/A)").upper()
   # entering records in dictionary
   record={
       'Name': name,
       'Roll_no': roll_no,
       'Course' : course,
       'date' : attendance_date,
       'Status' : status
   }
   attendance.append(record)# adding record in list of dictionaries
     
    
      
def attendance_report_student():#function for student attendance report
    r=int(input("Enter roll number to view attendance report: "))
    total_days=0
    present_days=0
    for record in attendance:
        if record['Roll_no'] == r:
            n=record['Name']
            total_days+=1
        if record['Status']== 'P':
            present_days+=1
    if total_days==0:
        print("NO ATTENDANCE RECORD FOUND!")
        return
    else:
        absent_days =total_days - present_days
        percent_days=int((present_days/total_days)*100)
    if percent_days<75:
        s="Defaulter"
    else:
        s="Regular" 
    print()
    print("-------------ATTENDANCE REPORT--------------")
    print(" Roll No   |    Name   |     Total   |     Present    |     Absent     |        Present %   | Status")
    print(f"    {r}    |  {n}    |     {total_days}       |       {present_days}        |        {absent_days}       |      {percent_days:.2f}%       |      {s} ") 
        
        
def fullclass_attendance():#function for whole class attendance
    if not attendance:#if list is empty then it will return
        print("NO ATTENDANCE RECORD FOUND")
        return
    summary={}
    for record in attendance:
        roll= record['Roll_no']
        if  roll not in summary:
            summary[roll]={
               'name':record['Name'],
               'total_days':0,
               'present_days':0,
            }
        summary[roll]['total_days']+=1
        if record['Status']=='P':
             summary[roll]['present_days']+=1
    print()
    print("======================== WHOLE CLASS ATTENDANCE REPORT =========================")
    print("   Roll No   |       Name       | Total   |      Present    |    Absent   |      Present %    |   Status")
    print("-" * 100)
    
    for roll, data in summary.items():
        total = data['total_days']
        present = data['present_days']

        absent = total - present
        percent = (present / total) * 100   
        status = "Defaulter" if percent < 75 else "Regular"
        print(f"      {roll}    |      {data['name']}       |   {total}     |         {present}       |      {absent}     |       {percent:.2f}%      |  {status} ") 
                
                     

while True:
    print(menu)
    try:
       choice=int(input("Enter your choice:"))
       if choice==1:
          mark_attendance()
       elif choice==2:
          attendance_report_student()
       elif choice==3:
         fullclass_attendance()
       elif choice==4:
         print("Exiting EDUTECH")
         break
       else:
           print("Invalid Input!.Try again")  
    except ValueError:
        print("Invalid Input!.Try again")  
    
          
            
        
        