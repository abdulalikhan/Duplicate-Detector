'''
main.py
Duplicate Detector v1.0
Built with Python, TKinter, FuzzyWuzzy, and Pandas
Abdul Ali Khan
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from find_duplicates import findDuplicates

filename = ''
records = []
recordIndex = 0


def make_ui():
    bgColor = '#232b32'
    containerColor = '#363f4b'
    selectColor = '#0f91ff'
    headingColor = '#0f4c81'
    txtColor = '#ffffff'
    fontFamily = 'Computer Modern'
    root = Tk()
    root.geometry('800x600')
    root.resizable(False, False)
    root.configure(background=bgColor)
    root.title("Duplicate Detector")
    heading = Label(root, text="Duplicate Detector", font=(
        fontFamily, 40), fg=headingColor, bg=bgColor)
    middleFrame = Frame(root, bg=bgColor)
    recordIdFrame = Frame(root, bg=bgColor)
    lbl = Label(middleFrame, text="Click 'Browse' to select a CSV file.", font=(
        fontFamily, 13), fg=txtColor, bg=bgColor)

    def chooseCSV():
        global filename
        filename = askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if not filename:
            return
        lbl.configure(text="File Opened: " + filename)
        btnCheck.config(state="normal")

    def copyRecordId():
        root.clipboard_clear()
        root.clipboard_append((lbl4.cget("text")).replace('Record ID: ', ''))

    def showNextRecord():
        global records
        global recordIndex
        if (len(records) > recordIndex+1):
            recordIndex += 1
        else:
            recordIndex = 0
        btnCopy.pack_forget()
        btnNext.pack_forget()
        closestRecord = records[recordIndex]
        lbl3.configure(text=closestRecord[0])
        lbl4.configure(text="Record ID: " +
                       str(closestRecord[2]))
        lbl5.configure(text="Percentage Similiarity: " +
                       str(closestRecord[1]) + "%")
        pbar['value'] = closestRecord[1]
        pbarStyle.configure("red.Horizontal.TProgressbar",
                            bordercolor=containerColor, troughcolor=containerColor)
        btnCopy.pack(side=LEFT, padx=10, pady=5)
        btnNext.pack(side=LEFT, padx=10, pady=5)

    btn = Button(middleFrame, text='Browse', font=(fontFamily, 13),
                 fg=txtColor, bg=headingColor, command=chooseCSV)

    descriptionBox = Text(root, height=5, width=80, font=(
        fontFamily, 13), fg=txtColor, bg=containerColor, selectbackground=selectColor)

    def findDuplicatesHandler():
        global recordIndex
        global records
        recordIndex = 0
        records = []
        btnCopy.pack_forget()
        btnNext.pack_forget()
        description = descriptionBox.get("1.0", 'end-1c')
        if not description:
            messagebox.showinfo("Information", "Please enter a description.")
            return
        root.geometry('800x650')
        filePath = filename
        records = findDuplicates(filePath, description)
        closestRecord = records[0]
        lbl2.configure(text="Possible Duplicate(s):")
        lbl3.configure(text=closestRecord[0])
        lbl4.configure(text="Record ID: " +
                       str(closestRecord[2]))
        lbl5.configure(text="Percentage Similiarity: " +
                       str(closestRecord[1]) + "%")
        pbar['value'] = closestRecord[1]
        pbarStyle.configure("red.Horizontal.TProgressbar",
                            bordercolor=containerColor, troughcolor=containerColor)
        btnCopy.pack(side=LEFT, padx=10, pady=5)
        btnNext.pack(side=LEFT, padx=10, pady=5)

    btnCheck = Button(root, text='Check for Duplicates', font=(fontFamily, 16),
                      fg=txtColor, bg=headingColor, state=DISABLED, command=findDuplicatesHandler)
    lbl2 = Label(root, text="", font=(fontFamily, 15),
                 fg=txtColor, bg=bgColor)
    lbl3 = Label(root, text="", font=(fontFamily, 13),
                 fg=txtColor, bg=bgColor, wraplength=700, justify=LEFT)
    lbl4 = Label(recordIdFrame, text="", font=(fontFamily, 13),
                 fg=txtColor, bg=bgColor)
    btnCopy = Button(recordIdFrame, text='Copy', font=(fontFamily, 13),
                     fg=txtColor, bg=headingColor, command=copyRecordId)
    lbl5 = Label(root, text="", font=(fontFamily, 15),
                 fg=txtColor, bg=bgColor)
    pbarStyle = ttk.Style()
    pbarStyle.theme_use('clam')
    pbarStyle.configure("red.Horizontal.TProgressbar",
                        troughcolor=bgColor, bordercolor=bgColor, background=headingColor)
    pbar = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL,
                           length=500, mode='determinate')
    btnNext = Button(recordIdFrame, text='Next >>', font=(fontFamily, 13),
                     fg=txtColor, bg=headingColor, command=showNextRecord)
    statusbar = Label(
        root, text="Duplicate Detector v1.0 - Abdul Ali Khan", fg=txtColor, bg=headingColor, font=(fontFamily, 10), relief=SUNKEN)
    heading.pack(pady=25, padx=50)
    middleFrame.pack(padx=10)
    lbl.pack(side=LEFT, padx=10)
    btn.pack(side=LEFT, padx=10)
    descriptionBox.pack(pady=10)
    btnCheck.pack(pady=10)
    lbl2.pack(pady=10)
    lbl3.pack(pady=5)
    recordIdFrame.pack(padx=10)
    lbl4.pack(side=LEFT, padx=10, pady=5)
    lbl5.pack(pady=5)
    pbar.pack(pady=5)
    statusbar.pack(side=BOTTOM, fill=X)
    root.mainloop()


if __name__ == '__main__':
    make_ui()
