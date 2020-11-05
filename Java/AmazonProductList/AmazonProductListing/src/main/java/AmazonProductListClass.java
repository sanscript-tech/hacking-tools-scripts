/*
 Author : Haripriya Baskaran
 */

// Importing selenium library from openqa

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class AmazonProductListClass {
    // Declaring url, search elements locator, and the search word which user will be giving as input
    private static final String URL = "https://www.amazon.in/";
    private static final By searchBar = By.xpath("//*[@id=\"twotabsearchtextbox\"]");
    private static final By searchButton = By.xpath("//*[@id=\"nav-search-submit-text\"]/input");
    private static final By result = By.xpath(".//*[contains(@class,'celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results')]");

    public static void main(String[] args) throws IOException {
        //Input keyword taken from user
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter keyword to search: ");
        String searchWord = br.readLine();

        // Webdriver initialised in headless mode
        FirefoxOptions option = new FirefoxOptions();
        option.setHeadless(true);
        WebDriver driver = new FirefoxDriver(option);

        // Url set to driver
        driver.get(URL);

        //input given to search bar
        driver.findElement(searchBar).sendKeys(searchWord);
        driver.findElement(searchButton).click();

        // Wait till the result page loads
        WebDriverWait wait = new WebDriverWait(driver, 5);
        wait.until(ExpectedConditions.visibilityOfElementLocated(result));

        //Get result of products on the page in a list of webelements
        List<WebElement> productList = driver.findElements(result);
        for (int i = 0; i < 5; i++) {
            // first 5 products are printed out
            String[] text = productList.get(i).getText().split("\\n");
            System.out.println((i + 1) + "  " + text[0] + "\n" + text[1] + "\n" + text[2] + "\n" + text[3]);
        }

        // driver is closed
        driver.quit();
    }
}
