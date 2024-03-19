import random
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import random
from bs4 import BeautifulSoup
import csv
# from profile import profile

class opera():
    def experience(wait):
        list_eperience = []
        for section in range(3,6):
            try:
                main_parent = f'//*[@id="profile-content"]/div/div[2]/div/div/main/section[{section}]/div[3]/ul'
                list_element = wait.until(EC.visibility_of_element_located((By.XPATH, main_parent))).get_attribute('innerHTML')
                pagesource =  BeautifulSoup(list_element,'html.parser')
                page_list = pagesource.find_all('li',class_='artdeco-list__item KsFwwhqECQNDiHmPXfpqEXuOZIaLGWniElPk efYSRaxBWhKdSirBMNQpSSQmRNkMqoDHqQWHQSdM')
                for i in range(1,len(page_list)+1):
                    try:
                        pagesour= wait.until(EC.visibility_of_element_located((By.XPATH, f'{main_parent}/li[{i}]/div/div[2]'))).get_attribute('innerHTML')
                        page_source = BeautifulSoup(pagesour,'html.parser')
                        try:
                            jobs = page_source.find_all('li',{'class':'efYSRaxBWhKdSirBMNQpSSQmRNkMqoDHqQWHQSdM'})
                            company = page_source.find('a',{'data-field':'experience_company_logo'}).find('span',class_="visually-hidden").get_text().split('·')[0]
                            location = page_source.find('a',{'data-field':'experience_company_logo'}).find('span',class_="t-14 t-normal t-black--light").find('span',class_="visually-hidden").get_text()
                            if jobs:
                                for jb in jobs:
                                    try:

                                        job_times = jb.find('a',class_='optional-action-target-wrapper display-flex flex-column full-width')
                                        job = job_times.find('div',class_='display-flex align-items-center mr1 hoverable-link-text t-bold').find('span',class_='visually-hidden').get_text().split('·')[0]  
                                        times = job_times.find('span',class_='t-14 t-normal t-black--light').find('span',class_='visually-hidden').get_text().split('·')[0]  
                                        experience = {
                                            'company':company,
                                            'job':job,
                                            'time':times,
                                            'location':location
                                        }
                                        if experience not in list_eperience:
                                            list_eperience.append(experience)
                                    except:
                                        pass
                            else:
                                raise 'skip'
                        except:
                            company = page_source.find('span',class_="t-14 t-normal").find('span',class_="visually-hidden").get_text().split('·')[0]
                            time_location = page_source.find_all('span',class_="t-14 t-normal t-black--light")
                            job = page_source.find('div',class_="display-flex align-items-center mr1 t-bold").find('span',class_="visually-hidden").get_text()
                            try:
                                location = time_location[-1].find('span',class_="visually-hidden").get_text()
                            except:
                                location = 'Null'
                            try:
                                times = time_location[-2].find('span',class_="visually-hidden").get_text().split('·')[0]
                            except:
                                times = time_location[-1].find('span',class_="visually-hidden").get_text().split('·')[0]
                                
                            experience = {
                                'company':company,
                                'job':job,
                                'time':times,
                                'location':location
                            }
                            if experience not in list_eperience:
                                list_eperience.append(experience)
                    except:
                        pass
            except:
                section+=1
        return list_eperience
    

    
    def contact(driver,wait):
        max_retries = 5
        for attemps in range(max_retries):
            try:
                page_source = BeautifulSoup(driver.page_source,'html.parser')
                info_div = page_source.find('div',class_ = 'mt2 relative')
                name = info_div.find('h1').get_text().strip()
                title = info_div.find('div',class_ = "text-body-medium break-words").get_text().strip()
                location = info_div.find('span',class_="text-body-small inline t-black--light break-words").get_text().strip()
                next_button = wait.until(EC.visibility_of_element_located((By.ID, "top-card-text-details-contact-info")))
                next_button.click()
                sleep(1)
                page_source = BeautifulSoup(driver.page_source,'html.parser')
                contact_div = page_source.find_all('div',class_ = 'pv-profile-section__section-info section-info')
                url_inf = contact_div[0].find_all('section',class_ ='pv-contact-info__contact-type')
                url_info = []
                for urls in url_inf:
                    try:
                        a_href = urls.find('a').get('href')
                        url_info.append(a_href)
                    except:
                        pass
            except:
                max_retries-=1
                sleep(2)
        return name,title,location,url_info


    def login(driver,username,password):
        print('login')
        max_retries = 5
        delay = 2
        for attemps in range(max_retries):
            try:
                sleep(random.randint(2, 4))
                email_field = driver.find_element(By.ID,'session_key')
                email_field.send_keys(username)
                sleep(random.randint(2, 4))
                password_field = driver.find_element(By.ID,'session_password')
                password_field.send_keys(password)
                sleep(random.randint(2, 4))
                login_field = driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/button')
                login_field.click()
                sleep(random.randint(2, 4))
                sleep(5)
                break
            except:
                max_retries-=1
                delay+=10
                sleep(delay)

    def search(wait,title,driver):
        print('search')
        max_retries = 5
        tile_form = title.replace(" ",'%20e')
        delay = 2
        for attemps in range(max_retries):
            try:
                driver.get(f'https://www.linkedin.com/search/results/people/?keywords={tile_form}&origin=SWITCH_SEARCH_VERTICAL&searchId=92708440-a74c-46e1-a9a4-af8b1053b311&sid=cxp')
                break
            except:
                print(max_retries)
                max_retries-=1
                delay+=2
                sleep(delay)

    def get_url(driver):
        print('get_url')
        page_source = BeautifulSoup(driver.page_source,'html.parser')
        profiles = page_source.find_all('span',class_ = 'entity-result__title-text t-16')
        all_profile_url = []
        for profile in profiles:
            profile_id = profile.find_all('a')[0].get('href')
            all_profile_url.append(profile_id)
        return all_profile_url
    
    def get_all_url_on_pages(file_path,driver,wait,num_of_page):
        print('get_url')
        url_all_page =[]
        count=1
        with open(f'{file_path}/list_candidate.txt','w',newline= '') as file_output:
            for page in range(num_of_page):
                max_retries = 5
                delay = 2
                for attempt in range(max_retries):
                    try:
                        sleep(2)
                        url_one_page = opera.get_url(driver)
                        for url in url_one_page:
                            file_output.write(url+'\n')
                            print(url)
                        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                        sleep(2)
                        next_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'artdeco-pagination__button--next')))
                        next_button.click()
                        url_all_page+=url_one_page
                        break
                    except:
                        max_retries-=1
                        delay+=1
                        print(max_retries)
            return url_all_page
        
    def scan(file_path,driver,wait):
        print('scan')
        with open(f'{file_path}/list_candidate.txt','r',newline= '') as file_read:
            lst_url = file_read.read().splitlines()
            with open(f'{file_path}/output.csv','w',newline= '') as file_output:
                headers = ['Name', 'Job title', 'Location', 'URL', 'Experience']
                writer = csv.DictWriter(file_output,delimiter=',',lineterminator='\n',fieldnames=headers)
                writer.writeheader()
                count=1
                for i in range(0,3):
                    max_retries = 2
                    delay = 2
                    print(i)
                    for attempt in range(max_retries):
                        driver.get(lst_url[i])
                        list_eperiences = opera.experience(wait)
                        name,title,location,url_info = opera.contact(driver,wait)
                        try:
                            info = {headers[0]: name, headers[1]: title, headers[2]: location, headers[3]: url_info, headers[4]: list_eperiences}
                            print(f'{i}/{len(lst_url)}: {info}')
                            writer.writerow(info)
                            count+=1
                            break
                        except Exception as e:
                            max_retries-=1
                            delay+=1
                            sleep(delay)
                            print(max_retries)
