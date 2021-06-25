# HackerRank_Contest_Scraper
Collects all accepted (partial and full scored) codes submitted within the given timeframe of any contest. 

And saves them locally with a file name `<HackerRank_Id>.<language>` for plagiarism check.

## Demo:

![alt-text](https://github.com/belelaritra/HackerRank_Contest_Scraper/blob/main/Gif/HackerRank_Scraper.gif)

## Installation:

In Terminal:
- Run `pip install selenium`
- Run `pip install pyperclip` 

## Download:

- [ChromeDriver](https://chromedriver.chromium.org/downloads)

## Procedure:

> Type `chrome://version` in Chrome Search Bar 
>> according to your chrome version and Operating System Download [`ChromeDriver`](https://chromedriver.chromium.org/downloads) zip file 
>>>  Unzip (extract) the file to your preferred location 
>>>> Copy the `path`

## Changes:
>Copy the Path of `chromedriver.exe`  (Example: `C:\Users\user\Downloads`)
>>add `\chromedriver.exe` in the end  (Example: `C:\Users\user\Downloads\chromedriver.exe`)
>>>and change that with `____Chrome Driver Path_____`

Before:
```
driver = webdriver.Chrome(r"___ChromeDriver Path___")
```
After (Example):
```
driver = webdriver.Chrome(r"C:\\Users\\user\\Downloads\\chromedriver.exe")
```

## User Manual:
>Enter your `HackerRank Username or Email`
>>Enter your `HackerRank Password`
>>>Enter the `Contest Name` (Partial or Complete Name)
>>>>Enter the `Question Name` (Partial or Complete Name) under that Contest
>>>>>Choose the Path where you want to save all accepted files.
>>>>>>Enter `Submit`

## Shortcut Keys:

- Enter `esc` key, to close the GUI.
- Enter `tab` key to change the entry box.
- Enter `enter` key to click buttons & to change focus.
