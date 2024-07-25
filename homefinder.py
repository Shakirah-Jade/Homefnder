from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

driver.get("https://homefinder.com/rentals/CA/county/Orange")

contents = driver.find_elements(By.CSS_SELECTOR, ".results-items .listing-tile")

extracted_Listings = []

for content in contents:
  
    Listing_data = {
        "Url": content.get_attribute("href"),
        "Image": content.find_element(By.CSS_SELECTOR, ".img-fluid").get_attribute("src"),
        "Address": content.find_element(By.CSS_SELECTOR, ".mb-0").text,
        "Name": content.find_element(By.CSS_SELECTOR, ".addr-component").text,
        "Price": content.find_element(By.CSS_SELECTOR, ".h4").text,
        "Rent": content.find_element(By.CSS_SELECTOR, ".text-rentals").text,
        "Bed": content.find_element(By.CSS_SELECTOR, ".text-muted").text,
    }

    extracted_Listings.append(Listing_data)


print(extracted_Listings)

csv_file = "Listings.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
   
    writer = csv.DictWriter(file, fieldnames=["Url", "Image", "Address","Name", "Price","Rent","Bed"])
    writer.writeheader()
  
    writer.writerows(extracted_Listings)

print(f"Data has been written to {csv_file}")

driver.quit()
