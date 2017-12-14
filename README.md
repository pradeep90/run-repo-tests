# Hook to run tests during pre-commit

This is a hook to run all tests in your repository. Use it with [pre-commit](http://pre-commit.com/) by putting this in `.pre-commit-config.yaml`:

```yaml
-   repo: /home/pradeep/Dropbox/Programs/Python/pre-commit-run-tests/
    sha: 7ca9ef7
    hooks:
    -   id: pradeep-run-tests
```

Currently runs only Python tests (in `_test.py` files that have a main function).
