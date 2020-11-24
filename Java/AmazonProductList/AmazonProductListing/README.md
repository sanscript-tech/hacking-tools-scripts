# Amazon top 5 products List
The aim of the program is to fetch the top 5 recommended products that amazon provides
for a given keyword from user.

### Library used:
* [Selenium](https://www.selenium.dev/)
* [Firefox Webdriver](https://github.com/mozilla/geckodriver/releases)

### Pre-requisites:
* Download and add selenium jar file to your classpath from this [link](https://www.selenium.dev/downloads/)

Or
* Add Selenium dependency from [mvn repository](https://mvnrepository.com/search?q=selenium)

* Download the latest release of FireFox webdriver from this [link](https://github.com/mozilla/geckodriver/releases) and
save it in `/urs/local/bin` of your machine.

### Usage:
#### Selenium dependency add method(Recommended):
* Open the code files in an IDE supporting java(Recommended: Intellij IDEA)
* Run the AmazonProductListClass.java from the IDE only
#### Download and add selenium jar file
* Set selenium jar file to you classpath ([Reference](https://medium.com/@andrey.dobra/how-to-set-up-selenium-webdriver-in-eclipse-with-external-jar-files-or-maven-84e2d14fb5ce#:~:text=Right%20click%20on%20the%20project,downloaded%20from%20the%20official%20website.))
* Run `>> javac AmazonProductListClass.java`
* Then `>> java AmazonProductListClass`

### I/O:
```
Enter keyword to search: $(searchWord)
<Sample Output for word "table":
1  +3 colors/patterns
Sponsored
Smiling Cloud® Quality LapDesk Bed Laptop Table with Dock Stand and Coffee Cup Holder/Study Table/Foldable Portable/Full Size/Sleek Rounded Edges/Non-Slip Legs (Sky Blue - with CupHolder)
₹999
2  Sponsored
Kundi Bed Tray Table Adjustable Foldable Multi-Function Portable Laptop Table/Study Table with Drawer (Black)
18
₹1,399
3  Sponsored
GLAMFLOX Wooden Portable Desk with Foldable Legs and Cup Slot for Eating Breakfast; Reading Book; Watching Movie on Bed/Couch/Sofa for Beds Laptop Notebook Holder (Black)
45
₹899
4  +2 colors/patterns
Sponsored
Amazon Brand - Solimo Wanderer Multi-Purpose Laptop Table (Wenge)
36
5  Best seller
MemeHo® Smart Multi-Purpose Laptop Table with Dock Stand/Study Table/Bed Table/Foldable and Portable/Ergonomic & Rounded Edges/Non-Slip Legs/Engineered Wood (Black)
8,056
Limited time deal
>
```


