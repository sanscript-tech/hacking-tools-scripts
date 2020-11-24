#include<stdio.h>
#include<curl/curl.h>
#include<json-c/json.h>
#include<string.h>

// Callback function to handle API response.
static size_t write_callback(char *contents, size_t size, size_t nmemb, void *userp)
{
    // Json objects to parse response.
    json_object *parsed_json, *main_data, *temp, *wind, *wind_speed, *humidity;

    // Tokenise JSON
    parsed_json = json_tokener_parse(contents);

    // Extract data from JSON response.
    json_object_object_get_ex(parsed_json, "main", &main_data);
    json_object_object_get_ex(main_data, "temp", &temp);
    json_object_object_get_ex(main_data, "humidity", &humidity);
    json_object_object_get_ex(parsed_json, "wind", &wind);
    json_object_object_get_ex(wind, "speed", &wind_speed);

    // Print json response with color.
    printf("\033[93mTemperature: %s°C\033[0m\n", json_object_get_string(temp));
    printf("\033[93mHumidity   : %s%%\033[0m\n", json_object_get_string(humidity));
    printf("\033[93mWind Speed : %sknots\033[0m\n", json_object_get_string(wind_speed));

    // return size of the data handled.
    return size * nmemb;
}


int main(int argc, char **argv)
{
    // Define necessary variables.
    char *location = argv[1];
    char key[64], url[1024];

    // Initialise CURL structures.
    CURL *curl;
    CURLcode res;

    // Open key file to extract API key.
    FILE *fp = fopen("key", "r");
    if(fp == NULL)
    {
        fprintf(stderr, "Unable to open `key` file.");
        exit(1);
    }
    fgets(key, 64, fp);
    fclose(fp);

    // Formulate the API endpoint.
    sprintf(url, "https://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=%s", location, key);

    printf("\033[92mWeather details for %s:\n", location);

    // Perform a GET HTTP request.
    curl = curl_easy_init();
    if(curl)
    {
        // Set CURL options
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);

        // Perform the request, res will get the return code
        res = curl_easy_perform(curl);
        /* Check for errors */
        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

        // cleanup
        curl_easy_cleanup(curl);
    }

    return 0;
}
