Python Flask JSON API
===
By [Clevyr](https://clevyr.com)

## Installation

Must have **Python 3** installed

```
git clone <repo>
cd <repo>
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Lastly, make a copy of the DB.
cp db/todo.db.original db/todo.db
```

## Commands
```
make seed # seeds the database

make run # runs the flask app

make test # runs the tests
```

## Your Job

Fork the repo, and update your own fork.

Make that repo public.

Make all the tests pass!

This includes:
* Adding a new `is_complete` `BOOL` value to the database
* Making sure all of the routes return valid responses


## Notes

You can and should feel free to edit anything EXCEPT for the `tests` directory.
