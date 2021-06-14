# HackerRank_Contest_Scraper
Collects all accepted (partial and full scored) codes submitted within the given timeframe of any contest. 
And saves them locally with a file name `<HackerRank_Id>.<language>` for plagiarism check.

## Installation

In Terminal:
- Run `pip install selenium`
- Run `pip install pyperclip` 

Downloads:
- [ChromeDriver](https://chromedriver.chromium.org/downloads)

Procedure:

Type `chrome://version` in Chrome Search Bar --> according to your chrome version Download [`ChromeDriver`](https://chromedriver.chromium.org/downloads) zip file --> Unzip (extract) the file to preferred location --> Copy the `path` 

Open `HackerRank` --> Click on `Administration` --> Choose the `Contest` --> Click on `Challenges` --> Choose a `Challenge` --> Click on `View Submissions`--->Copy the `URL`

Changes :
- Copy the `URL`  and Enter that in the terminal
- Copy the Path of `chromedriver.exe` and change that with `____Chrome Driver Path_____` and add `/chromedriver.exe` in the end
- Copy the Path of a folder where you want to save all codes and enter the path in the terminal
- Change the `__HackerRank Email Id___` with your `HackerRank login mail id`
- Change `___Password___` with with your `HackerRank Login Password`


## Please Help me to improve the code

You can also add tkinter gui.
