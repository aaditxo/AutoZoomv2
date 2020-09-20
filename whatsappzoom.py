from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from easygui import *
import pyautogui

contacts = ["+965 9929 0755"]
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
sleep(2)

meetings={}

def join(id,pswd):
	brake=False
	while brake==False:
		try:
			meet_id = id
			password = pswd
			pyautogui.press('esc',interval=0.1)
			sleep(0.2)
			pyautogui.press('win',interval=0.1)
			pyautogui.write('zoom')
			pyautogui.press('enter',interval=0.5)
			sleep(5)
			x,y = pyautogui.locateCenterOnScreen('joinButton.png',confidence=0.7)
			pyautogui.click(x,y)
			pyautogui.press('enter',interval=1)
			pyautogui.write(meet_id)
			pyautogui.press('enter',interval=1)
			sleep(3)
			pyautogui.write(password)
			pyautogui.press('enter',interval = 1)
			sleep(4)
			try:
				x,y = pyautogui.locateCenterOnScreen('mute.png')
				pyautogui.click(x,y)
			except:
				pass
			brake=True
		except:
			continue

while 1:
	try:
		for contact in contacts:
			selected_contact = driver.find_element_by_xpath(f'//span[@class="_3ko75 _5h6Y_ _3Whw5"][@title="{contact}"][@dir="auto"]')
			selected_contact.click()
			inp_xpath = '//span[@dir="ltr"][@class="_3Whw5 selectable-text invisible-space copyable-text"]'
			input_box = driver.find_elements_by_xpath(inp_xpath)
			print(f'{len(input_box)} elements found.')
			for i in input_box:
				t=i.text
				if 'Join Zoom Meeting' and 'One tap mobile' and 'Dial by your location' in t:
					l=t.split('\n')
					for j in l:
						if 'Meeting ID:' in j:
							meetingid=(j.replace('Meeting ID:','')).replace(' ','')
						if 'Passcode:' in j:
							passcode=(j.replace('Passcode:','')).replace(' ','')
					key,value = meetingid,passcode
					j=key in meetings and value == meetings[key]
					if j==False:
						meetings.update({meetingid:passcode})
						msg = f"Do you want to join Zoom Meeting hosted by {contact}?"
						title = "Join Zoom Meeting"
						if ccbox(msg, title):
						    print(f'You chose to join {meetingid} hosted by {contact} using passcode {passcode}.')
						    sleep(1)
						    join(meetingid,passcode)
						else:
						    print(f'You didnt join {meetingid} hosted by {contact} using passcode {passcode}.')

			sleep(2)
	except Exception as e:
		print(f'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!DEBUG!!
!!EXCEPTION!!
{str(e)}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')

driver.quit()