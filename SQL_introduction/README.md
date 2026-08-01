# SQL - Introduction

Introductory SQL scripts for MySQL 8.0, covering DDL and DML basics: creating
and deleting databases, creating and describing tables, and inserting,
selecting, updating, deleting and aggregating data.

## Requirements

- Executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files end with a new line
- Every SQL query is preceded by a comment, and every file starts with a
  comment describing the task
- All SQL keywords are in uppercase

## Tasks

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases |
| `1-create_database_if_missing.sql` | Create database `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Delete database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all tables of a database |
| `4-first_table.sql` | Create table `first_table` |
| `5-full_table.sql` | Print the full description of `first_table` |
| `6-list_values.sql` | List all rows of `first_table` |
| `7-insert_value.sql` | Insert a row into `first_table` |
| `8-count_89.sql` | Count records with `id = 89` |
| `9-full_creation.sql` | Create `second_table` and add rows |
| `10-top_score.sql` | List records ordered by score |
| `11-best_score.sql` | List records with score >= 10 |
| `12-no_cheating.sql` | Update Bob's score to 10 by name |
| `13-change_class.sql` | Remove records with score <= 5 |
| `14-average.sql` | Compute the average score |
| `15-groups.sql` | Count records per score |
| `16-no_link.sql` | List records that have a name |
| `100-move_to_utf8.sql` | Convert `hbtn_0c_0`/`first_table` to utf8mb4 |
| `101-avg_temperatures.sql` | Average temperature by city |
| `102-top_city.sql` | Top 3 cities by temperature (Jul/Aug) |
| `103-max_state.sql` | Max temperature per state |
