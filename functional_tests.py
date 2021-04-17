from selenium import webdriver

#browser = webdriver.Firefox()
browser=webdriver.Firefox(executable_path=r'C:\Python\Scripts\geckodriver.exe')
browser.get('http://localhost:8000')

#assert 'Django' in browser.title
assert 'MyTitleDjango' in browser.title