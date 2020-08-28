# Bulk Issue Creation

This project is intended to make bulk-creating issues for JIRA as simple as possible.

## Running

The program assumes you have a `users.txt` file in the same directory as the `create_issues.py` script, with a single Jira user handle per line (as shown below):

```txt
jabrahms
jmiller
```

The program can be run with the command `python create_issues.py`

The output CSV will owerwrite `./output.csv`
