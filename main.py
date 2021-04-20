# docker run -v "$(pwd):/app" test
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        import time
        from selenium import webdriver

        driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
        driver.get('http://www.web.de/')
        print_hi("Bin da")
        driver.save_screenshot("test.png")
        time.sleep(5)
        driver.quit()

    except:
        x = sys.exc_info()
        print_hi(x)
        xx = 9

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
