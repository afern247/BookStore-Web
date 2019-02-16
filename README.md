# Development branch

## Remove old junk files

- Update the .gitignore by merging the code into your personal branch.
- Remove the junk files in your personal branch:
```
git rm -r -f log
git rm -r -f tmp
git rm --cached *.pyc
find . -name '*.pyc' | xargs -n 1 git rm --cached
```
- Removing SQLite3 file:
```
git rm -f *.sqlite3
```

The suggestions to do these changes came from: [Why not to commit .pyc files into git](https://github.com/fraction/readme-boilerplate/issues/new) and [Ignoring SQLite files](https://github.com/fraction/readme-boilerplate/issues/new)

- After you clean those files, your online branch will not have them so you will only push the right files once you modify something. In order to keep developing offline, make sure you do `python manage.py migrate` so that the sqlite3 database can be created offline for your personal use which will not be pushed once changed.

## Do not push to the development branch code with these junk files.