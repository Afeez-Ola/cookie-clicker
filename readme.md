# Cookie Clicker Bot

This Python script automates the clicking and purchasing actions in the "Cookie Clicker" web game using Selenium.

## Project Setup

1. Ensure you have Python installed on your system.
2. Install the required packages by running the following command:
    ```pip install selenium```
3. Download the appropriate ChromeDriver executable for your system and update the `chrome_driver_path` variable in the script accordingly.
4. Run the script using the following command:
    ```python interaction.py```


## Dependencies

- Python 3.x
- Selenium

## Usage

1. Open the "Cookie Clicker" game in your web browser.
2. Execute the script.
3. The script will start automatically clicking the cookie at a specified rate.
4. It will keep track of the current cookie count and determine the closest item that can be purchased.
5. The script will purchase the closest item available.
6. It will gradually increase the clicking rate as time progresses.
7. The process will continue indefinitely until the script is terminated.

## Configuration

You can modify the `clicks_per_second` variable to adjust the clicking rate. By default, it starts at 100 clicks per second and increases by 50 every 5 seconds.

The `items_dict` dictionary defines the items available for purchase and their corresponding prices. You can modify this dictionary to customize the purchasing strategy.

## Disclaimer

Please note that automating actions in web games may violate the terms of service or rules of the game. Use this script responsibly and ensure you comply with any applicable rules or restrictions.

## License

This project is licensed under the [MIT License](LICENSE).
