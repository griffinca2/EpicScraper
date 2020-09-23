from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tkinter import *
import easygui


import time 

available = []

def mainFunction(readfile, writefile):
    textfile = open(readfile, "r")
    write_to_file = open(writefile, 'a+')
    handles = textfile.read().splitlines()

    #Uncomment below to open program in normal browser
    #browser = webdriver.Chrome(executable_path='chromedriver.exe')

    #Options for using headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\webdrivers\chromedriver.exe')

    #Load the URL into the browser
    browser.get("https://www.epicgames.com/id/register")

    #Wait for the page to fully load
    time.sleep(3.2)

    elem = browser.find_element_by_name("displayName")
    for handle in handles:
        elem.send_keys(handle)
        time.sleep(2.1)

        try:
            browser.find_element_by_xpath("//*[text()='Already taken']")

        except NoSuchElementException:
            print(handle + " is available")
            available.append(handle)
            write_to_file.write(handle + '\n')
            print(available)

        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)

    textfile.close()
    write_to_file.close()
    browser.quit()
    sys.exit(0)


#Creating and running GUI interface
window = Tk()

window.title("Epic Games URL Search")
window.geometry('350x200')
lbl = Label(window, text="EG URL Search")
lbl.grid(column=0, row=0)


def clicked1():
    global readfile
    readfile = easygui.fileopenbox()

def clicked2():
    global writefile
    wf = easygui.enterbox(msg='Enter output file name(not including .txt.)', title='', default='', strip=True)
    writefile = wf + '.txt'

def clicked3():
    if(not readfile.strip() ):
        print('Input file is null. Please enter real file.')
    if(not writefile.strip()):
        print('Output file is null. Please enter correct values.')
    else:
        mainFunction(readfile, writefile)

btn_input_file = Button(window, text="Select input file:  ", command=clicked1, height=2, width=15)
btn_output_file = Button(window, text='Select output file: ', command=clicked2, height=2, width=15)
btn_run = Button(window, text='Run Program', command=clicked3, height=2, width=15)

btn_input_file.grid(column=1, row=0)
btn_output_file.grid(column=1, row=1)
btn_run.grid(column=1, row=2)
window.mainloop()