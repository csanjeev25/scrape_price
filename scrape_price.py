from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys

def paytm(driver,search):
	item={}
	item['name']=''
	item['price']=''
	item['avail']=''
	item['ship']=''
	try:
		driver.get(search)
		paytm='Error'
		try:
			if driver.find_element_css_selector('.NZJI'):
				name=driver.find_element_css_selector('.NZJI').text
		except:
			item['name']=None
			item['price']=None
			item['avail']=None
			item['ship']=None
			return item
		price = driver.find_element_by_css_selector('._1y_y').text
		price1=price[8:]
		price1=price1.replace(',','')
		avail='Y'
		time.sleep(6)
		if driver.find_element_css_selector('pyBu'):
			avail='N'
			item['name']=name
			item['price']=price1
			item['avail']=avail
			item['ship']=None
			return item
	except:
		avail='Y'
		pass
	time.sleep(6)
	try:
		time.sleep(6)
		try:
			if driver.find_element_by_css_selector('._2sEn'):
				ship_price = driver.find_element_by_css_selector('._2sEn').text
				item['name']=name
				item['price']=price1
				item['avail']=avail
				item['ship']=ship_price
				return item
			else:
				pass
		except:
			if not sp:
				item['name']=name
				item['price']=price1
				item['avail']=avail
				item['ship']=ship_price
				return item
			else:
				item['name']=name
				item['price']=price1
				item['avail']=avail
				item['ship']=sp
				return item
	except:
		item['name']=name
		item['price']=price1
		item['avail']=avail
		item['ship']=None
		return item

def file_write(data,header):
	data_frame = pd.DataFrame.from_dict(data, orient='index').reset_index()
	data_frame.to_csv('comapre.csv',columns=header,index=False)
	return True

def snapdeal(driver,search):
	item={}
	item['naiteme']=''
	item['price']=''
	item['avail']=''
	item['ship_price']=''
	try:
		driver.get(search)
		try:
			if driver.find_element_by_css_selector('.pdp-e-i-head'):
				name = driver.find_element_by_css_selector('.pdp-e-i-head').text
		except:
			item['naNonee']=None
			item['price']=None
			item['avail']=None
			item['ship_price']=None
			return item
		price = driver.find_element_by_css_selector('.payBlkBig').text
		nprice=price.replace(',','')
		try:
			if driver.find_element_by_css_selector('.sold-out-err'):
				avail='N'
				item['name']=name
				item['price']=nprice
				item['avail']=avail
				return item
		except:
			avail='Y'
			pass
		time.sleep(4)
		try:
			if driver.find_element_by_id('pincode-check'):
				pincode=driver.find_element_by_id('pincode-check')
				pincode.send_keys('110005')
				time.sleep(5)
				driver.find_element_by_id('pincode-check-bttn').click()
				time.sleep(5)
				try:
					sp=driver.find_element_by_css_selector('.availCharges').text
				except:
					pass
				try:
					sp=driver.find_element_by_css_selector('.avail-free').text
				except:
					pass
			item['name']=name
			item['price']=nprice
			item['avail']=avail
			item['ship_price'] = sp
			return item
		except:
			item['name']=name
			item['price']=nprice
			item['avail']=avail
			item['ship_price']=None
			return item
			pass
		time.sleep(5)
	except:
		item['name']=name
		item['price']=nprice
		item['avail']=avail
		item['ship_price']=None
		return item

def flipkart(driver,search,data,index):
	item={}
	item['price']=''
	item['Avail']=''
	item['ship_price']=''
	item['name']=''
	try:
		driver.get(search)
		tp=0
		try:
			try:
				if driver.find_element_by_class_name('_3eAQiD'):
					name=driver.find_element_by_class_name('_3eAQiD').text
			except:
				item['price']=None
				item['Avail']=None
				item['ship_price']=None
				item['name']=None
				return item
			inputElement = driver.find_element_by_class_name("_1vC4OE")
			price = inputElement.text
			tp=price[1:]
			tp=tp.replace(',','')
			if driver.find_element_by_css_selector('._3xgqrA'):
				x='N'
				item['price'] = tp
				item['Avail'] = x
				item['ship_price'] = None
				item['name'] = name
				return item
		except:
			x='Y'
			pass
		ship_price = driver.find_element_by_class_name('_3X4tVa')
		ship_price.send_keys('110005')
		driver.find_element_by_class_name('_2aK_gu').click()
		time.sleep(7)
		sp=driver.find_element_by_class_name('_3EaKlN').text
		sp=sp.replace('?','')
		item['price']=tp
		item['Avail']=x
		item['ship_price']=sp
		item['name']=name
		return item
	except:
		item['price']=tp
		item['Avail']=x
		item['ship_price']=None
		item['name']=name
		return item

def amazon(driver,search,data,index):
	item={}
	item['ship_price']=''
	item['price']=''
	item['Avail']=''
	item['name']=''
	try:
		driver.get(search)
		driver.implicitly_wait(8)
		price=0
		try:
			try:
				if driver.find_element_by_id('title_feature_div'):
					name=driver.find_element_by_id('title_feature_div').text
			except:
				item['ship_price']=None
				item['price']=None
				item['Avail']=None
				item['name']=None
				return item
			try:
				if driver.find_element_by_css_selector('.a-color-price'):
					price=driver.find_element_by_css_selector('.a-color-price')
			except:
				pass
			try:
				if driver.find_element_by_id('priceblock_saleprice'):
					price=driver.find_element_by_id('priceblock_saleprice')
			except:
				try:
					if driver.find_element_by_id('priceblock_ourprice'):
						price=driver.find_element_by_id('priceblock_ourprice')
				except:
					pass
			tp=price.text
			if tp == 'Currently unavailable.':
				item['ship_price'] = None
				item['price'] = None
				item['name'] = name
				item['Avail']= 'N'
				return item
			dp=tp.replace(',','')
			item['price']=dp
			try:
				if driver.find_element_by_id('price-shipping-message'):
					sp=driver.find_element_by_id('price-shipping-message').text
					newship=sp.replace('.Details','')
			except:
				try:
					if driver.find_element_by_id('ourprice_shippingmessage'):
						sp = driver.find_element_by_id('ourprice_shippingmessage').text
						ph=sp.replace('+','')
						newship=ph.replace('Delivery charge Details','')
						newship=newship.strip()
				except:
					pass
			item['ship_price'] = newship
			item['price']=dp
			item['Avail']='Y'
			item['name']=name
			return item
		except:
			if item['price'] == '':
				item['price'] = None
				item['Avail']='N'
				item['ship_price']=None
				item['name']=name
				return item
			else:
				item['Avail']='Y'
				item['ship_price']=None
				item['name']=name
				return item
	except:
		pass

def main():
	item=input("Enter product")
	df = pd.read_csv('input.csv')
	header=["Shopclues_PID","FlipKart Title","FlipKart Assured","FlipKart Selling Price","FlipKart Total Discount","Amazon Title","Amazon Fullfilled","Amazon Selling price","Amazon Total Discount","Paytm Title","Paytm Selling Price","Paytm Total Discount","SD Title","SD Gold","SD Selling Price","SD discount","Amazon SP","Flipkart SP","Snapdeal SP","Paytm SP","Amazon Availability","Flipkart Availability","Snapdeal Availability","Paytm Availability"]
	data={}
	i=0
	for index,row in df.iterrows():
		try:
			display = Display(visible=0, size=(800, 800))
			display.start()
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('--no-sandbox')
			driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=chrome_options)
			data[index]={}
			data[index]['Shopclues_PID']=row.PID
			Amazon=row.Amazon
			Am_url=Amazon.strip()
			Flipkart=row.Flipkart
			Flip_url=Flipkart.strip()
			Snapdeal=row.Snapdeal
			Snap_url=Snapdeal.strip()
			Paytm=row.Paytm
			Paytm_url=Paytm.strip()
			if Am_url != None:
				h=amazon(driver,row.Amazon,data,index)
				print(h)
				data[index]['Amazon Selling price']=h['price']
				data[index]['Amazon Availability']=h['Avail']
				data[index]['Amazon SP']=h['ship_price']
				data[index]['Amazon Title']=h['name']
			else:
				data[index]['Amazon Selling Price']=None
				data[index]['Amazon Availability']=None
				data[index]['Amazon SP']=None
				data[index]['Amazon Title']=None
			if Flip_url != None:
				p =flipkart(driver,row.Flipkart,data,index)
				print(p)
				data[index]['FlipKart Selling Price']=p['price']
				data[index]['Flipkart Availability']=p['Avail']
				data[index]['FlipKart Title']=p['name']
				data[index]['Flipkart SP']=p['ship_price']
			else:
				data[index]['Flipkart Selling Price']=None
				data[index]['Flipkart Availability']=None
				data[index]['Flipkart Title']=None
				data[index]['Flipkart SP']=None
			if Snap_url != None:
				g = snapdeal(driver,row.Snapdeal)
				print(g)
				data[index]['SD Title']=g['name']
				data[index]['SD Selling Price']=g['price']
				data[index]['Snapdeal Availability']=g['avail'] 
				data[index]['Snapdeal SP']=g['ship_price']
			else:
				data[index]['SD Title']=None
				data[index]['SD Selling Price']=None
				data[index]['Snapdeal Availability']=None
				data[index]['Snapdeal SP']=None   
			if Paytm_url != None:
				r=paytm(driver,row.Paytm)
				data[index]['Paytm Selling Price'] = r['price']
				data[index]['Paytm Availability'] = r['avail']
				data[index]['Paytm Title'] = r['name']
				data[index]['Paytm SP'] = r['ship'] 
			else:
				data[index]['Paytm Selling Price'] = None
				data[index]['Paytm Availability'] = None
				data[index]['Paytm Title'] = None
				data[index]['Paytm Title']=None
			file_write(data,header)
			driver.close()
			driver.quit()
			display.stop()
		except Exception as e:
			pass

if __name__ == "__main__":
	main()

		




