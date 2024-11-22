from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")
        
        lbltitle =Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()    
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        # -----------------------DATA FRAME ---------------------
        Dataframe=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        dataframeLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("arial",12,"bold"),text="Patient Information")
        dataframeLeft.place(x=0,y=5,width=980,height=350)
        
        dataframeRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("arial",12,"bold"),text="Prescription")
        dataframeRight.place(x=990,y=5,width=460,height=350)
        
        
        # ---------------------------- buttos frame----------------------------
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        
        # ---------------------------- Details frame----------------------------
        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,height=190)
        
        
        
        # -------------------------------dataframeLeft----------------------------
        
        lblNameTablet=Label(dataframeLeft,text="Names of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNameTablet=ttk.Combobox(dataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.grid(row=0,column=1)
        
        lblref=Label(dataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeLeft,textvariable=self.ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(dataframeLeft,font=("arial",12,"bold"),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(dataframeLeft,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)
        
        lblNotablets=Label(dataframeLeft,font=("arial",12,"bold"),text="No of Tablets",padx=2,pady=6)
        lblNotablets.grid(row=3,column=0,sticky=W)
        txtNotablets=Entry(dataframeLeft,textvariable=self.NumberofTablets,font=("arial",12,"bold"),width=35)
        txtNotablets.grid(row=3,column=1)
        
        lblLot=Label(dataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(dataframeLeft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        lblisseDate=Label(dataframeLeft,font=("arial",12,"bold"),text="Issue Date: ",padx=2,pady=6)
        lblisseDate.grid(row=5,column=0,sticky=W)
        txtisseDate=Entry(dataframeLeft,textvariable=self.Issedate,font=("arial",12,"bold"),width=35)
        txtisseDate.grid(row=5,column=1)
        
        lblExpDate=Label(dataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataframeLeft,textvariable=self.ExpDate,font=("arial",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(dataframeLeft,font=("arial",12,"bold"),text="Daily Dose: ",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataframeLeft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(dataframeLeft,font=("arial",12,"bold"),text="Side Effect: ",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(dataframeLeft,textvariable=self.sideEffect,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        
        
                
        lblFurtherinfo=Label(dataframeLeft,font=("arial",12,"bold"),text="Further Information ",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(dataframeLeft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure=Label(dataframeLeft,font=("arial",12,"bold"),text="Blood Pressure ",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(dataframeLeft,textvariable=self.DrivingUsingMachine,font=("arial",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        lblStorage=Label(dataframeLeft,font=("arial",12,"bold"),text="Storage Advice: ",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeLeft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine=Label(dataframeLeft,font=("arial",12,"bold"),text="Medication ",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(dataframeLeft,textvariable=self.HowToUseMedication,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)
        
        lblPatientId=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient ID: ",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(dataframeLeft,textvariable=self.PatientId,font=("arial",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(dataframeLeft,font=("arial",12,"bold"),text="Nhs Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(dataframeLeft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        lblPatientName=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient Name: ",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(dataframeLeft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)
        
        lblDateOfBirth=Label(dataframeLeft,font=("arial",12,"bold"),text="Date of birth: ",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(dataframeLeft,textvariable=self.DateOfBirth,font=("arial",12,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient Address: ",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(dataframeLeft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        
        
        # -----------------------------------DataframeRight----------------------
        self.txtPrescription=Text(dataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        # --------------------Buttons-----------------------
        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptiondata,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=2)
        
        
        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="blue",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=3)
    
        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="red",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=4)
        
        
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="white",fg="black",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=5)
        
        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="orange",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=6)
        
        
        
        
        
        # ---------------------------------------Table---------------------------
        
        # ---------------------------------------Scrollbar---------------------------
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
    
        self.hospital_table=ttk.Treeview(Detailframe,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
                
        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        self.fetch_data()
        
        
        # ----------------------------------Functioality Decleration---------------------------
    def iPrescriptiondata(self):
        if self.Nameoftablets.get()==""or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.ref.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issedate.get(),                                                                                                
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.nhsNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateOfBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DrivingUsingMachine.get(),
                                                                                                self.PatientId.get(),
                                                                                                self.sideEffect.get()                                                                                                                                                                                                                                                                                                                                                 
                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","Recored has been inserted")
            
            
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s, dose=%s ,numberoftablets=%s ,lot=%s, issuedate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s  where Reference_No=%s",(
                                                                                                self.Nameoftablets.get(),
                                                                                                
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.nhsNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateOfBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                self.ref.get()
                                                                                                ))
        messagebox.showinfo("update","Patient has been updated successfully")
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),
        self.Issedate.set(row[5]),
        self.ExpDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.StorageAdvice.set(row[8]),
        self.nhsNumber.set(row[9]),
        self.PatientName.set(row[10]),
        self.DateOfBirth.set(row[11]),
        self.PatientAddress.set(row[12])
        
        
    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No. :\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issedate.get()+"\n")
        self.txtPrescription.insert(END,"Expire Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice: \t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"\blood Pressure:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"Nhs number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
    
    
    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hospital")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)    
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
        
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)
        
        
    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
    
    
            
                    
                                    
                        
        
        
        
        
        

    
    

        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    ob=Hospital(root)    
    root.mainloop()