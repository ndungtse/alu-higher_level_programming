# Python - Object-relational mapping

Connecting Python to a MySQL database two ways: first directly with the
`MySQLdb` module (raw SQL, including a look at SQL injection), then through the
`SQLAlchemy` ORM by mapping Python classes to tables.

## Requirements

- Interpreted on Ubuntu 20.04 LTS using `python3` (3.8.5)
- `MySQLdb` 2.0.x and `SQLAlchemy` 1.4.x, MySQL on `localhost:3306`
- First line of every file is `#!/usr/bin/python3`
- pycodestyle (2.7.*) compliant; files end with a new line and are executable
- No `execute` with SQLAlchemy

## Tasks

| File | Module | Description |
|------|--------|-------------|
| `0-select_states.py` | MySQLdb | List all states, sorted by id |
| `1-filter_states.py` | MySQLdb | States whose name starts with `N` |
| `2-my_filter_states.py` | MySQLdb | States matching an argument (via `format`) |
| `3-my_safe_filter_states.py` | MySQLdb | Same, safe from SQL injection |
| `4-cities_by_state.py` | MySQLdb | All cities with their state name |
| `5-filter_cities.py` | MySQLdb | Cities of a given state (injection-free) |
| `model_state.py` | SQLAlchemy | `State` model for the `states` table |
| `7-model_state_fetch_all.py` | SQLAlchemy | List all `State` objects |
| `8-model_state_fetch_first.py` | SQLAlchemy | First `State`, else `Nothing` |
| `9-model_state_filter_a.py` | SQLAlchemy | States containing `a` |
| `10-model_state_my_get.py` | SQLAlchemy | State id by name, else `Not found` |
| `11-model_state_insert.py` | SQLAlchemy | Add `Louisiana`, print its id |
| `12-model_state_update_id_2.py` | SQLAlchemy | Rename state id 2 to `New Mexico` |
| `13-model_state_delete_a.py` | SQLAlchemy | Delete states containing `a` |
| `model_city.py` | SQLAlchemy | `City` model for the `cities` table |
| `14-model_city_fetch_by_state.py` | SQLAlchemy | All cities with their state |
| `relationship_state.py` | SQLAlchemy | `State` with a cascading `cities` relationship (advanced) |
| `relationship_city.py` | SQLAlchemy | `City` with a `state` backref (advanced) |
| `100-relationship_states_cities.py` | SQLAlchemy | Create a state + city via the relationship (advanced) |
| `101-relationship_states_cities_list.py` | SQLAlchemy | List states with their cities (advanced) |
| `102-relationship_cities_states_list.py` | SQLAlchemy | List cities with their state (advanced) |
