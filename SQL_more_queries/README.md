# SQL - More queries

MySQL scripts covering user management and privileges, table constraints
(`NOT NULL`, `UNIQUE`, `DEFAULT`, `PRIMARY KEY`, `FOREIGN KEY`), and querying
across multiple tables with subqueries and `JOIN`s.

## Requirements

- Executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files end with a new line
- Every SQL query is preceded by a comment, and every file starts with a
  comment describing the task
- All SQL keywords are in uppercase

## Tasks

| File | Description |
|------|-------------|
| `0-privileges.sql` | List privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Create `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Create `hbtn_0d_2` + read-only `user_0d_2` |
| `3-force_name.sql` | Table `force_name` with `NOT NULL` name |
| `4-never_empty.sql` | Table `id_not_null` with default id `1` |
| `5-unique_id.sql` | Table `unique_id` with unique default id |
| `6-states.sql` | Database `hbtn_0d_usa` + `states` (primary key) |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | California cities via subquery |
| `9-cities_by_state_join.sql` | Cities with state name via `JOIN` |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows, `NULL` genre if none |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Show count per genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with all linked genres |
| `100-not_my_genres.sql` | Genres not linked to Dexter |
| `101-not_a_comedy.sql` | Shows without the Comedy genre |
| `102-rating_shows.sql` | Shows by total rating |
| `103-rating_genres.sql` | Genres by total rating |
| `blog_post.md` | Task 21 blog: "How Do SQL Database Engines Work?" |
