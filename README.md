# Freight Rate Monitor - Jadlog

This Python project allows you to estimate freight prices using the Jadlog transport company website.
It performs real-time scraping of the form on the Jadlog website using Selenium.

## Features
- Real scraping with Selenium (headless Chrome)
- Input for origin/destination ZIP code and cargo weight
- Returns estimated freight cost and delivery time
- Clean and responsive interface using Streamlit

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

You must have **Google Chrome** and **chromedriver** installed on your system.

## Usage

```bash
streamlit run app.py
```

Enter:
- Origin ZIP (e.g., 01001-000)
- Destination ZIP (e.g., 20040-000)
- Weight (e.g., 5.0 kg)

The system will return the estimated price and delivery time.

## Notes
- This project is for educational/demo purposes only.
- Be mindful of sending too many requests to the website.

## License
MIT