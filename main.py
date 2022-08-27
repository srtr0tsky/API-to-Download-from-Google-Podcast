from selenium.webdriver.common.by import By
import module.connection_module as website
# Script to make download in site Google Podcasts 

# Variables
URL_PODCAST = input("Put the link to your episode on Google Podcasts here:")
FEED_URL = ""
PODCAST_NAME = ""

if __name__ == "__main__":
    browser = website.WebConnect().connection(URL_PODCAST)
    try: 
        FEED_URL, PODCAST_NAME = website.WebConnect().getFeedURL(browser) #return FEED URL and PODCAST NAME
    except Exception as error:
        print(error)
        browser.close()  # Close connection   
    finally: 
        browser.close() # Close connection
        
        print("FEED URL: " + FEED_URL)
        try:
           
            browser = website.WebConnect().connection(FEED_URL)  # Connect with the address in FEED URL
            titles = browser.find_elements(By.XPATH, "//item//title") # Seek the elements in page
            for i in range(len(titles)): # Search for a title that matches the podcast name
                title = titles[i].text # convert the object to text 
                if title in PODCAST_NAME:
                    downloads = browser.find_elements(By.XPATH, "//item//*[@type='audio/mpeg']")
                    LINK_DOWNLOAD = downloads[i].get_attribute('url')
                    break
        except Exception as error:
            print(error)      
            browser.close()
        finally: 
            browser.close()
            print("LINK TO DOWNLOAD: " + LINK_DOWNLOAD)
            website.WebConnect().download(url=LINK_DOWNLOAD, name=PODCAST_NAME)