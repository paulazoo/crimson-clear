
def get_cookies(driver):
  cookies = driver.get_cookies()
  for cookie in cookies:
    print('printing cookie...')
    print(cookie)
    driver.add_cookie(cookie)

  with open('cookie_storage.txt', 'w') as f:
    str_cookie = str(cookies)
    f.write(str_cookie)

  return cookies