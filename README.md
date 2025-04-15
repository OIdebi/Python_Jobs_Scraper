# 🧰 Junior Python Developer Job Scraper

This Python script scrapes junior-level Python developer job listings from [CV-Library UK](https://www.cv-library.co.uk/junior-python-developer-jobs) and saves the data into a CSV file for further analysis or reporting.

---

## 🔍 What It Does

- Scrapes job titles, company names, job locations, and salaries.
- Collects data using `BeautifulSoup` and `requests`.
- Exports the scraped job data into a structured CSV file (`Jobs.csv`).

---

## 🧪 Tech Stack

- Python
- `requests` for making HTTP requests
- `BeautifulSoup` for parsing HTML
- `csv` for saving data to file

---

## 🚀 How to Use

### 1. Clone this repo

```bash
git clone https://github.com/OIdebi/python-job-scraper.git
cd python-job-scraper
```
### 2.Install dependencies
```bash
pip install -r requirements.txt
```

You can also install the dependencies manually if requirements.txt is not available:
```bash
pip install beautifulsoup4 requests
```

### 3.Run the script
```bash
python scraper.py
```

This will generate a file called Jobs.csv containing:

📂 Output Format
The Jobs.csv file will contain four rows:

Row	Description
1	Job Titles
2	Company Names
3	Locations
4	Salary Info

🧑‍💻 Author
Built by [OIdebi]
Feel free to connect or contribute!

