from selenium import webdriver
import time
import sys
import numpy

b = webdriver.Chrome(r"E:\chromedriver.exe")
# time.sleep(2)
b.get("http://poshanabhiyaan.gov.in/#/login")
time.sleep(2)
x = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/div[4]/div[1]/span[2]").get_attribute("innerHTML")
y = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/div[4]/div[1]/span[3]").get_attribute("innerHTML")
z = int(x) + int(y)
print(z)
captchi = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/div[4]/div[2]/input")
captchi.send_keys(str(z))
usr = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/mat-form-field[1]/div/div[1]/div/input")
pas = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/mat-form-field[2]/div/div[1]/div/input")
usr.send_keys("mow&cd-3361705")
pas.send_keys("mow&cd-3361705")
butt = b.find_element_by_xpath("/html/body/app-login/div[1]/div[2]/div/form/div/div/div[5]/div[2]/button")
butt.click()
time.sleep(3)
ok = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[2]/div/div/div[3]/button")
ok.click()
i=0
for j in range(0, 1000):
  arrow = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[1]/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]")
  arrow.click()
  homevisit = b.find_element_by_xpath("/html/body/div/div[2]/div/div/mat-option[24]/span")
  time.sleep(1)
  homevisit.click()
  themeArr = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[1]/div[1]/div/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[2]")
  themeArr.click()
  # themeSize = b.find_element_by_xpath("/html/body/div/div[3]/div/div")
  time.sleep(1)
  count = 0
  for i in range(1, 100):
      try:  
          if b.find_element_by_xpath("/html/body/div/div[3]/div/div/mat-option[" + str(i) + "]/span").get_attribute("innerHTML"):
              count = count + 1
              print(count)
      except:
          print(count)
          break
  index = numpy.random.choice(range(1, count))
  themeClick = b.find_element_by_xpath("/html/body/div/div[3]/div/div/mat-option[" + str(index) + "]/span")
  themeClick.click()

  totalP = numpy.random.choice(range(35, 51))
  adults = numpy.random.choice(range(10, 25))
  child = totalP - adults
  adM = numpy.random.choice(range(5, 15)); adF = adults - adM
  chM = numpy.random.choice(range(8, 10)); chF = child - chM

  adduF = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/th[3]/input")
  adduM = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[1]/th[2]/input")
  chilF = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[2]/th[3]/input")
  chilM = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/table/tbody[1]/tr[2]/th[2]/input")
  totalPartici = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/input")

  arr = [adduF, adduM, chilF, chilM, totalPartici]
  arr2 = [adF, adM, chF, chM, totalP]

  for i in range(0, 5):
      arr[i].send_keys(str(arr2[i]))

  escape = b.find_element_by_xpath("/html/body/div/div[2]")
  escape.click()
  time.sleep(0.5)
  submit = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/div[1]/div/div/form/div/div[2]/div/div[3]/div/div/button")
  #Escape buttom implemented
  submit.click()
  time.sleep(3)
  addanother = b.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-hierarchy/p-dialog[1]/div/div[2]/div[1]/div[1]/button")
  addanother.click()
  j=j+1
