from tkinter import *
import base64
from email.mime import base
import tkinter as tk
from tkinter.filedialog import askopenfilename
import xlwt
from tkinter.filedialog import askopenfilename

root = tk.Tk()

# setting the windows size
root.geometry("700x400")

# declaring string variable
# for storing details
cid_var = tk.StringVar()
cname_var = tk.StringVar()
caddr_var = tk.StringVar()
cstate_var = tk.StringVar()
ccity_var = tk.StringVar()
cmobile_var = tk.StringVar()
cgender_var = tk.StringVar()
cage_var = tk.StringVar()

# defining a function that will
# get the details and
# print them on the screen
def submit():
    cid = cid_var.get()
    cname = cname_var.get()
    caddr = caddr_var.get()
    cstate = cstate_var.get()
    ccity = ccity_var.get()
    cmobile = cmobile_var.get()
    cgender = cgender_var.get()
    cage = cage_var.get()

    workbook = xlwt.Workbook()

#Naming the sheet in the excel
    sheet = workbook.add_sheet("xlwt")

    sheet.write(0, 0, 'Student Details')
    sheet.write(1, 0, 'Student ID')
    sheet.write(2, 0, 'Student Name')
    sheet.write(3, 0, 'Student Address')
    sheet.write(4, 0, 'State')
    sheet.write(5, 0, 'City')
    sheet.write(6, 0, 'Mobile No')
    sheet.write(7, 0, 'Gender')
    sheet.write(8, 0, 'Age')

    sheet.write(1, 1, cid)
    sheet.write(2, 1, cname)
    sheet.write(3, 1, caddr)
    sheet.write(4, 1, cstate)
    sheet.write(5, 1, ccity)
    sheet.write(6, 1, cmobile)
    sheet.write(7, 1, cgender)
    sheet.write(8, 1, cage)
    
#saving the data to excel
    workbook.save("book s2.xls")

    cid_var.set("")
    cname_var.set("")
    caddr_var.set("")
    cstate_var.set("")
    ccity_var.set("")
    cmobile_var.set("")
    cgender_var.set("")
    cage_var.set("")

cid_label = tk.Label(root, text='WELCOME TO NEW AL-HIJRA SOFTWARE', font=('calibre', 10, 'bold'))
cname_label = tk.Label(root, text='Student Name', font=('calibre', 10, 'bold'))
caddr_label = tk.Label(root, text='Student Address', font=('calibre', 10, 'bold'))
cstate_label = tk.Label(root, text='State', font=('calibre', 10, 'bold'))
ccity_label = tk.Label(root, text='City', font=('calibre', 10, 'bold'))

cgender_label = tk.Label(root, text='Gender', font=('calibre', 10, 'bold'))
cage_label = tk.Label(root, text='Age', font=('calibre', 10, 'bold'))

cid_entry = tk.Entry(root, textvariable=cid_var, font=('calibre', 10, 'normal'))
cname_entry = tk.Entry(root, textvariable=cname_var, font=('calibre', 10, 'normal'))
caddr_entry = tk.Entry(root, textvariable=caddr_var, font=('calibre', 10, 'normal'))
ccity_entry = tk.Entry(root, textvariable=ccity_var, font=('calibre', 10, 'normal'))
cmobile_entry = tk.Entry(root, textvariable=cmobile_var, font=('calibre', 10, 'normal'))
cgender_entry = tk.Entry(root, textvariable=cgender_var, font=('calibre', 10, 'normal'))
cage_entry = tk.Entry(root, textvariable=cage_var, font=('calibre', 10, 'normal'))

#submit button
sub_btn = tk.Button(root, text='submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
cid_label.grid(row=0, column=1)
cname_label.grid(row=1, column=0)
caddr_label.grid(row=2, column=0)
cstate_label.grid(row=3, column=0)
ccity_label.grid(row=4, column=0)

cgender_label.grid(row=6, column=0)
cage_label.grid(row=7, column=0)


cname_entry.grid(row=1, column=1)
caddr_entry.grid(row=2, column=1)

ccity_entry.grid(row=4, column=1)
cmobile_entry.grid(row=5, column=1)
cgender_entry.grid(row=6, column=1)
cage_entry.grid(row=7, column=1)

sub_btn.grid(row=9, column=1) 

vars = tk.IntVar()  
tk.Radiobutton(root, text="Male", padx=5,variable=vars, value=1).grid(row=6, column=2)
tk.Radiobutton(root, text="Female", padx =10,variable=vars, value=2).grid(row=6, column=3)
tk.Radiobutton(root, text="others", padx=15, variable=vars, value=3).grid(row=6, column=4)

list_of_cntry = (
['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
) 
cv = tk.StringVar()  
drplist= tk.OptionMenu(root, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("Select")

list_of_number = ('+92','+91')
cv = tk.StringVar()  
drplistno= tk.OptionMenu(root, cv, *list_of_number)  
drplistno.config(width=10)  
cv.set("Enter numbber")


drplistno.grid(row=5, column=0)

drplist.grid(row=3, column=1)







def file_open():
    text_window.delete('1.0', END)
    filePath = askopenfilename(
        initialdir='C:/', title='Select a File', filetype=(("Text File", ".txt"), ("All Files", "*.*")))
    with open(filePath, 'r+') as askedFile:
        fileContents = askedFile.read()

    text_window.insert(INSERT, fileContents)
    print(filePath)


open_button = Button(root, text="Select  File", command=file_open).grid(row=9, column=0)
text_window = Text(root, bg="white",width=200, height=150)
root.mainloop()



# performing an infinite loop
# for the window to display
root.mainloop()