# sales-analysis-python-mysql-using-pdbc
A menu-driven Sales Analysis System using Python, MySQL and Python Database Connectivity (PDBC).
The project analyzes product sales data and provides information such as total sales, best-selling products, highest-revenue products, category-wise sales, city-wise sales, discounts, and low-sales products.

## Features

- Display all products
- Search product by name
- Calculate total sales
- Find best-selling product
- Find highest-revenue product
- Category-wise sales analysis
- City-wise sales analysis
- Calculate total discount
- Identify low-sales products
- Store low-sales analysis in the database
- Prevent duplicate analysis records
- Handle invalid menu input

## Technologies Used

- Python
- MySQL
- Python Database Connectivity (PDBC)
- mysql-connector-python
- python-dotenv

## Project Structure

```text
Sales-Analysis-PDBC/
│
├── salesAnalysisProject.py
├── database_setup.sql
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Database Setup

1. Open MySQL Workbench.
2. Open `database_setup.sql`.
3. Execute the SQL script.

This will create the `products` database, required tables, and sample product data.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Sales-Analysis-PDBC
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project directory.

You can use `.env.example` as a reference:

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=products
```

Enter your own MySQL username and password.

> The `.env` file is ignored by Git and should not be uploaded to GitHub.

## Run the Project

```bash
python salesAnalysisProject.py
```

The program will display the following menu:

```text
1. Display All Products
2. Search Product
3. Calculate Total Sales
4. Find Best Selling Products
5. Find Highest Revenue Products
6. Category-Wise Sales Analysis
7. City-wise Sales Analysis
8. Calculate Total Discount
9. Find Products with low sales
10. Exit
```

## What I Learned

Through this project, I practiced:

- Connecting Python with MySQL
- Executing SQL queries using Python
- Fetching and processing database records
- Aggregate functions and GROUP BY
- Subqueries
- Parameterized SQL queries
- Database transactions using commit
- Environment variables for database credentials
- Basic exception handling
- Building a menu-driven database application
