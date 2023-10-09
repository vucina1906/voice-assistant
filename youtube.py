from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Vuk\Desktop\Projects\VoiceAssistant\Project2\chromedriver.exe')
        
    def play(self,query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissible"] ')
        video.click()
                 
#assist = music()
#assist.play('dynamite')