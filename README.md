# Example project for alembic issue #1195

See title

## State

The project is in a state that now expects the user to create a new alembic revision for a change in the user model.
Migrations are applied automatically while running `main.py`. Doing so will result in in the following exception:

```plain
[...]alembic/operations/batch.py", line 670, in add_constraint
    raise ValueError("Constraint must have a name")
```

## Reproducing the issue

1. Clone the repository
2. Run `uv sync` to create a virtualenv and install dependencies
3. Run `uv run alembic revision --autogenerate -m "add external id"` to create the errornous migration
4. Run `uv run python main.py` to apply migrations (and create a user)
5. Check the error produced on the console

## Expected behavior

The migration should've been applied and the `external_id` column should've been added to the user table. Afterwards,
a user should've been crated and its Id printed out to the console.
