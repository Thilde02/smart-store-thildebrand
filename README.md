# Pro Analytics 02 Python Starter Repository

> Use this repo to start a professional Python project.

- Additional information: <https://github.com/denisecase/pro-analytics-02>
- Project organization: [STRUCTURE](./STRUCTURE.md)
- Build professional skills:
  - **Environment Management**: Every project in isolation
  - **Code Quality**: Automated checks for fewer bugs
  - **Documentation**: Use modern project documentation tools
  - **Testing**: Prove your code works
  - **Version Control**: Collaborate professionally

---

## WORKFLOW 1. Set Up Your Machine

Proper setup is critical.


## WORKFLOW 2. Set Up Your Project

After verifying your machine is set up, set up a new Python project by copying this template. Complete each step in the following guide.

It includes the critical commands to set up your local environment

python -m venv .venv
.venv\Scripts\activate
uv run python -m analytics_project.data_prep
git add .
git commit -m "Add data_prep.py and successfully load raw data into pandas DataFrames"
git push

Issues Encountered
Filename mismatch (customers-data.csv vs customers_data.csv) resolved with Git add-commit-push

## WORKFLOW 3. Daily Workflow

Please ensure that the prior steps have been verified before continuing.
When working on a project, we open just that project in VS Code.

### 3.1 Git Pull from GitHub

Always start with `git pull` to check for any changes made to the GitHub repo.

```shell
git pull
```

### 3.2 Run Checks as You Work

This mirrors real work where we typically:

1. Update dependencies (for security and compatibility).
2. Clean unused cached packages to free space.
3. Use `git add .` to stage all changes.
4. Run ruff and fix minor issues.
5. Update pre-commit periodically.
6. Run pre-commit quality checks on all code files (**twice if needed**, the first pass may fix things).
7. Run tests.

In VS Code, open your repository, then open a terminal (Terminal / New Terminal) and run the following commands one at a time to check the code.

```shell
uv sync --extra dev --extra docs --upgrade
uv cache clean
git add .
uvx ruff check --fix
uvx pre-commit autoupdate
uv run pre-commit run --all-files
git add .
uv run pytest
```

NOTE: The second `git add .` ensures any automatic fixes made by Ruff or pre-commit are included before testing or committing.

<details>
<summary>Click to see a note on best practices</summary>

`uvx` runs the latest version of a tool in an isolated cache, outside the virtual environment.
This keeps the project light and simple, but behavior can change when the tool updates.
For fully reproducible results, or when you need to use the local `.venv`, use `uv run` instead.

</details>

### 3.3 Build Project Documentation

Make sure you have current doc dependencies, then build your docs, fix any errors, and serve them locally to test.

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

- After running the serve command, the local URL of the docs will be provided. To open the site, press **CTRL and click** the provided link (at the same time) to view the documentation. On a Mac, use **CMD and click**.
- Press **CTRL c** (at the same time) to stop the hosting process.

### 3.4 Execute

This project includes demo code.
Run the demo Python modules to confirm everything is working.

In VS Code terminal, run:

```shell
uv run python -m analytics_project.demo_module_basics
uv run python -m analytics_project.demo_module_languages
uv run python -m analytics_project.demo_module_stats
uv run python -m analytics_project.demo_module_viz
```

You should see:

- Log messages in the terminal
- Greetings in several languages
- Simple statistics
- A chart window open (close the chart window to continue).

If this works, your project is ready! If not, check:

- Are you in the right folder? (All terminal commands are to be run from the root project folder.)
- Did you run the full `uv sync --extra dev --extra docs --upgrade` command?
- Are there any error messages? (ask for help with the exact error)

---

### 3.5 Git add-commit-push to GitHub

Anytime we make working changes to code is a good time to git add-commit-push to GitHub.

1. Stage your changes with git add.
2. Commit your changes with a useful message in quotes.
3. Push your work to GitHub.

```shell
git add .
git commit -m "describe your change in quotes"
git push -u origin main
```

This will trigger the GitHub Actions workflow and publish your documentation via GitHub Pages.

### 3.6 Modify and Debug

With a working version safe in GitHub, start making changes to the code.

Before starting a new session, remember to do a `git pull` and keep your tools updated.

Each time forward progress is made, remember to git add-commit-push.


Tiffany Edits
Data Preparation

Created a Python script named data_scrubber.py located in the src folder.
This script uses a DataScrubber class to clean and standardize the datasets.

Cleaning Tasks Included:

Removing duplicate rows

Handling missing values (e.g., filling blanks or dropping incomplete rows)

Converting column types (e.g., date or numeric conversions)

Standardizing column names (making them lowercase and replacing spaces with underscores)

DataScrubber Class

The DataScrubber class was designed for reuse across all datasets.
It includes modular methods to handle each cleaning step and ensures that the same logic can be applied consistently to customers, products, and sales data.

Why This Approach:

Using one shared class instead of separate scripts for each dataset:

Reduces code duplication

Makes the project easier to maintain and expand later

Ensures consistent cleaning logic across all datasets

Data Warehouse Design ( week 4)

Schema: Star schema

Fact table: fact_sales (stores sales transactions)

Dimension tables: dim_customer (customer info), dim_product (product info)

Relationships: Sales rows reference customers and products through foreign keys.

Purpose: Optimized for quick queries and analytical reporting.

ETL Process

Load cleaned CSV files:

customers_prepared.csv

products_prepared.csv

sales_prepared.csv

Create tables in smart_sales.db if they don’t exist.

Delete old records (if any) to prevent duplication.

Insert data from CSVs into dimension and fact tables using Python and pandas.

Verify the data is correctly loaded into the warehouse.

Challenges Encountered

Some tables were initially in the wrong database (project.db).

Issues opening SQLite in VS Code due to missing sidebar icons and parse errors.

Adjusting file paths for CSVs so ETL script could load data properly.

Solutions Implemented

Created a cleanup Python script to remove incorrect tables from project.db.

Used Command Palette in VS Code to open and query databases.

Updated the ETL script to point explicitly to smart_sales.db and correct CSV paths.

Tested each step in Python before viewing tables in VS Code.

Week 5 - Reporting & OLAP Operations

For Project 5, I built interactive Power BI reports using cleaned CSVs (customers_prepared.csv, products_prepared.csv, sales_prepared.csv) as data sources. I created a star schema with sales_prepared as the fact table and customers_prepared and products_prepared as dimension tables, linking them by customerid and productid. I added a slicer on Region to filter sales by area, a dice using Region + Category to analyze product performance per region, and a drilldown chart with a sale_date hierarchy (Year → Month → Day) to explore seasonal trends. Challenges included phantom duplicate customer IDs, which I cleaned in Power Query, and not being able to connect directly to SQLite, so I used CSVs. The hardest part was fixing duplicate relationships, and the most interesting was seeing interactive visuals in action.
