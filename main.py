import os
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import lxml
import smtplib
from dotenv import load_dotenv
load_dotenv("./variables.env")
#----------Header For Request-------------#
header = {
    "User-Agent" : UserAgent().random,
    "Accept-Language": "en-US,en;q=0.9",
    "Referer" : "https://www.google.com/"
}
preset_price = 78
item_url = "https://www.amazon.com/Razer-Viper-Gaming-8500dpi-Buttons/dp/B084W6W9WB/ref=sr_1_1?crid=2UELYSQK4R27J&dib=eyJ2IjoiMSJ9.1M6CixlhKxKVNUvIDfHjYrca2gFhq2Vnb1VM8e8zv2SZdQSK2hgSgz-keovgGz78FS6uYnqA77BWY5_i32qi4zsDWdwMZWp14P9rFnZFl9l1qMnW_5Z3LIQ0zzY2z3FeOky0Hhfdnt5-J7At3pZ37_xxZhtG6XSF6PbpRfCt6ZhGJn3J2oXU4HQbFG6YDAsyRYuxuqDdhvHluFMRFXlhPMEV0qrhya0yeAHNw2OdTJo.TsO9VVAQhe-QO5-XSY5lk5PvnzoZVzRJbiqBlcy1SFQ&dib_tag=se&keywords=Razer%2Bviper%2Bmini&qid=1752081508&sprefix=razer%2Bviper%2Bmini%2Caps%2C301&sr=8-1&th=1"
http_request = requests.get(item_url,headers= header)
http_response = http_request.text
if "captcha" not in http_response:
    soup = BeautifulSoup(http_response,"lxml")
    whole_price = soup.select_one(".a-price-whole").contents[0]
    fraction_price = soup.select_one(".a-price-fraction").getText()
    price_string = f"{whole_price}.{fraction_price}"
    if float(price_string) <= preset_price:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("host_email"), password=os.getenv("app_pass"))
            connection.sendmail(from_addr=os.getenv("host_email"),to_addrs="[Recipient Email]",msg="Subject:Price Drop!!\n\nThis item is below the requested price, GRAB NOW!!!")





