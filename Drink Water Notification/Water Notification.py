import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now",
            message = "Drinking Water Helps Maintain the Balance of Body Fluids. Your body is composed of about 60% water. The functions of these bodily fluids include digestion, absorption, circulation, creation of saliva, transportation of nutrients, and maintenance",
            app_icon = ("icon.ico"),
            timeout = 2     
        )
        time.sleep(60*60)

        