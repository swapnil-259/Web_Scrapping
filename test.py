import time 
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
username_input = '2226EC1088'
password_input = '@Swapnil259'

driver.get('https://tech.kiet.edu/StudentPortal/#/login')
print(driver.title)
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
button = driver.find_element(By.XPATH,"//button[@aria-label='LOG IN']")
username.send_keys(username_input)
password.send_keys(password_input)
button.click()
wait = WebDriverWait(driver, 15)
attendance_details = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-field='table_data' and @data-rowindex='3']")))
attendance = attendance_details.text
examination_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[2]/li/button")))
examination_btn.click()
datesheet_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[2]/div/div/div/a[2]")))
datesheet_btn.click()
select_one = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/div/div/div/div/div[1]/p")))
select_one.click()
year1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"fuse-chip-select__menu-list.css-11unzgr")))
year1.click()
datesheet = []
date= []
day = []
shift= []
subject = []
hall_ticket_data = []
ht_date = []
ht_shift = []
ht_suject = []
sub_code = []
block = []
floor = []
room_no = []
seat_no = []
time_from = []
time_to = []
for i in range(1,8):
    for j in range(1,5):
        datesheet_data = wait.until(EC.presence_of_all_elements_located((By.XPATH,f"/html/body/div[1]/div/div/main/div[2]/div/div[3]/div/div[2]/div/div[3]/table/tbody/tr{[i]}/td{[j]}/div")))
        datesheet.append(datesheet_data[0].text)
for i in range(0,len(datesheet),4):
    date.append(datesheet[i])
for i in range(1,len(datesheet),4):
    day.append(datesheet[i])
for i in range(2,len(datesheet),4):
    shift.append(datesheet[i])
for i in range(3,len(datesheet),4):
    subject.append(datesheet[i])
hallticket_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[2]/div/div/div/a[3]")))
hallticket_btn.click()
select = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/div/div/div/div/div[1]/p")))
select.click()
year2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fuse-chip-select__menu-list.css-11unzgr")))
year2.click()
for i in range(1,7):
    for j in range(1,11):
        hall_ticket = wait.until(EC.presence_of_all_elements_located((By.XPATH,f"/html/body/div[1]/div/div/main/div[2]/div/div[3]/div/div/div[4]/div[3]/table/tbody/tr{[i]}/td{[j]}/div")))
        hall_ticket_data.append(hall_ticket[0].text)
# print(hall_ticket_data)
for i in range(0, len(hall_ticket_data),10):
    ht_date.append(hall_ticket_data[i])
for i in range(1, len(hall_ticket_data),10):
    ht_shift.append(hall_ticket_data[i])
for i in range(2, len(hall_ticket_data),10):
    ht_suject.append(hall_ticket_data[i])
for i in range(3, len(hall_ticket_data),10):
    sub_code.append(hall_ticket_data[i])
for i in range(4, len(hall_ticket_data),10):
    block.append(hall_ticket_data[i])
for i in range(5, len(hall_ticket_data),10):
    floor.append(hall_ticket_data[i])
for i in range(6, len(hall_ticket_data),10):
    room_no.append(hall_ticket_data[i])
for i in range(7, len(hall_ticket_data),10):
    seat_no.append(hall_ticket_data[i])
for i in range(8, len(hall_ticket_data),10):
    time_from.append(hall_ticket_data[i])
for i in range(9, len(hall_ticket_data),10):
    time_to.append(hall_ticket_data[i])
# mentoring = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[3]/li/button")))
# mentoring.click()
# mentorcard_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[3]/div/div/div/a[1]")))
# mentorcard_btn.click()
# session_select = wait.until(EC.element_to_be_clickable((By.XPATH,"//html/body/div[1]/div/div/main/header/div/div[2]/button[3]")))
# session_select.click()
# select_sem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[3]/li[1]")))
# select_sem.click()
# sem1 = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[5]/div[3]/ul/div[1]/li")))
# sem1.click()
# sem_wise_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/header/div/div/div/button[5]")))
# sem_wise_btn.click()

# mentoring_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[3]/li/button")))
# mentoring_btn.click()
# mentorcard_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div/div/ul/ul[3]/div/div/div/a[1]")))
# mentorcard_btn.click()
# sem_wise_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/header/div/div/div/button[5]")))
# sem_wise_btn.click()
# sel_sem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fuse-chip-select__indicators.css-1wy0on6")))
# sel_sem.click()
# sel_sem2 = wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-option-0")))
# sel_sem2.click()



# sub1 =  wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]")))
# sub1.click()
# row1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]')))
# for element in row1:
#     data_value = element.get_attribute('data-value')
#     print(data_value)


my_db = mysql.connector.connect( 
    host = 'localhost',
    user = 'swapnil',
    password = '@Swapnil259',
    database = 'student_details'
)
mycursor = my_db.cursor()
insert_query_1 = "INSERT INTO users (username, password, attendance) VALUES (%s, %s, %s)"
insert_query_2 = "INSERT INTO datesheet (date, day, shift, subject) VALUES (%s, %s, %s, %s)"
insert_query_3 = "INSERT INTO hall_ticket (date,shift,subject,code, block,floor,room_no,seat_no,time_from,time_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
data_1 = (username_input, password_input,attendance)
for i in range(0,len(date)):
    data_2 = (date[i], day[i],shift[i], subject[i])
    mycursor.execute(insert_query_2, data_2)
for i in range(0,len(ht_date)):
    data_3 = (ht_date[i],ht_shift[i],ht_suject[i],sub_code[i],block[i],floor[i],room_no[i],seat_no[i],time_from[i],time_to[i])
    mycursor.execute(insert_query_3,data_3)
mycursor.execute(insert_query_1, data_1)
my_db.commit()
my_db.close()   
time.sleep(10)
# driver.save_screenshot("dashboard.png")
driver.quit()
