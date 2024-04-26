# iplantdet/__init__.py

import atexit
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

def createbrowser(headless=True):
	options = webdriver.ChromeOptions()
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-gpu")
	options.add_argument("--disable-crash-reporter")
	options.add_argument("--disable-extensions")
	options.add_argument("--disable-in-process-stack-traces")
	options.add_argument("--disable-logging")
	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("--log-level=3")
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	if headless:
		options.add_argument("--headless")
	service = Service(executable_path=binary_path)
	return webdriver.Chrome(service=service, options=options)

browser = createbrowser()

def closebrowser():
	browser.close()
atexit.register(closebrowser)

def gettaxon(sname=""):
	time.sleep(random.uniform(2, 3))
	sla = browser.find_element(By.XPATH, "//div[@id='sptitlel']").text
	for _ in range(3):
		if sla.startswith(sname):
			break
		else:
			time.sleep(random.uniform(2, 3))
	szh = browser.find_element(By.XPATH, "//span[@id='spcname']").text
	navdiv = browser.find_element(By.XPATH, "//div[@id='spsyslink']")
	fzh, fla = navdiv.find_element(By.XPATH, "a[3]").text.split()
	gzh, gla = navdiv.find_element(By.XPATH, "a[4]").text.split()
	return {"fzh": fzh, "fla": fla, "gzh": gzh, "gla": gla, "szh": szh, "sla": sla}

def det(jpgpath):
	browser.get("https://www.iplant.cn/")
	time.sleep(random.uniform(2, 3))
	inputframe = browser.find_element(By.NAME, "localFile")
	inputframe.send_keys(jpgpath)
	time.sleep(random.uniform(2, 3))
	results = []
	print("Identifying", jpgpath)
	for i in range(1, 6):
		choice = browser.find_element(By.XPATH, f"//div[@id='stugroup']/div[{i}]")
		name, like = choice.text.split('\n')
		sname = ' '.join(name.split(' ')[:2])
		choice.click()
		taxon = gettaxon(sname=sname)
		results.append({"name": name, "like": like, "taxon": taxon})
		print("    ", "Result", i, name, like)
	print()
	return results
