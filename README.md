# Hook to run tests during pre-commit

This is a hook to run all tests in your repository, (Currently, it supports only Python tests.)

Use it with [pre-commit](http://pre-commit.com/) by putting this in `.pre-commit-config.yaml`:

```yaml
-   repo: git://github.com/pradeep90/run-repo-tests
    sha: v0.1
    hooks:
    -   id: run-python-tests
```

Currently runs only Python tests (in `_test.py` files that have a main function).
