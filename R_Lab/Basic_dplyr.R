# ======================================================
#  DPLYR BASICS: Data Manipulation in R
# ======================================================

#  Load Required Libraries
library(readxl)   # For reading Excel files (optional)
library(dplyr)    # For data manipulation

#  Load Dataset
dataset <- read.csv("R_Lab/dataset/ds_salaries.csv", header = TRUE, sep = ",")

#  Check Dataset Dimensions
dim(dataset)  # Output: 607 rows and 12 columns


# ======================================================
#  FILTERING: Select Specific Rows
# ======================================================

# Filter: work_year = 2020, job_title = "Data Scientist", salary_currency = "EUR"
filtered_data <- dataset %>%
filter(work_year == 2020, job_title == "Data Scientist", salary_currency == "EUR")

head(filtered_data)


# ======================================================
#  ARRANGING: Sort Rows
# ======================================================

# Sort by salary, remote_ratio, and salary_currency (ascending)
sorted_data <- dataset %>%
  arrange(salary, remote_ratio, salary_currency)

# Sort by salary (descending)
sorted_data_desc <- dataset %>%
  arrange(desc(salary))


# ======================================================
# ️ SLICING: Select Rows by Position
# ======================================================

# Rows 2 to 5
dataset %>% slice(2:5)

# First 5 rows
dataset %>% slice_head()

# Last 5 rows
dataset %>% slice_tail()

# Random 5 rows
dataset %>% slice_sample(n = 5)

# Highest salary in 2020 with lowest remote_ratio
dataset %>%
  filter(work_year == 2020) %>%
  slice_max(salary) %>%
  slice_min(remote_ratio)


# ======================================================
#  SELECTING: Choose Specific Columns
# ======================================================

# Select columns 3 to 5
dataset %>% select(3:5)

# Select specific column names
dataset %>% select(experience_level, employee_residence, job_title, salary)

# Exclude a range of columns
dataset %>% select(!(experience_level:employment_type))

# Select columns ending in "salary"
dataset %>% select(ends_with("salary"))

# Rename column
dataset %>% rename(SLRY = salary)


# ======================================================
#  MUTATING: Create New Columns
# ======================================================

# Add column: salary_after_tax (80% of salary)
new_dataset <- dataset %>%
  mutate(salary_after_tax = salary * 0.8)

# Add column: currency_in_dirham (using salary_in_usd)
new_dataset <- new_dataset %>%
  mutate(currency_in_dirham = salary_in_usd * 3.76)

# View specific columns
new_dataset %>%
  select(currency_in_dirham, salary_in_usd, everything())


# ======================================================
#  RELOCATING: Change Column Order
# ======================================================

# Move 'currency_in_dirham' and 'salary_in_usd' after 'S_No'
new_dataset <- new_dataset %>%
  relocate(currency_in_dirham, salary_in_usd, .after = S_No)

# Move 'salary_after_tax' after 'salary'
new_dataset <- new_dataset %>%
  relocate(salary_after_tax, .after = salary)


# ======================================================
#  SUMMARISING: Aggregate Values
# ======================================================

# Mean of salary_after_tax
new_dataset %>%
  summarise(mean_salary_after_tax = mean(salary_after_tax, na.rm = TRUE))

# Using reframe() (dplyr 1.1+)
new_dataset %>%
  reframe(mean_salary_after_tax = mean(salary_after_tax, na.rm = TRUE))

# ======================================================
#  CHALLENGE:
# Try creating new columns using your own logic!
# Example ideas: tax_slab, salary_grade, job_level, etc.
# ======================================================

