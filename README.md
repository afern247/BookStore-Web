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
git rm -f db/*.sqlite3
```