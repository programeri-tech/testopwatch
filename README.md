# testopwatch
Check how long each test takes and what test file is the slowest
```shell
❯ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
time_exec: 0.2517799s test_name: test_create_account (account.tests.test_account.AccountTests) OK
time_exec: 0.1164200s test_name: test_login (account.tests.test_account.AccountTests) OK
time_exec: 0.1113484s test_name: test_ping (account.tests.test_account.AccountTests) OK
time_exec: 0.0778311s test_name: test_activate (account.tests.test_account.AccountTests) OK
time_exec: 0.2358941s test_name: test_email_user (account.tests.test_account.AccountTests) OK
...
----------- Total test class times -----------
TestClass (account.tests.test_account.AccountTests) finished in 1.24016s
...
```

## Instructions:
1. Install
    ```shell
    ❯ pip install testopwatch
    ```

2. in your settings.py add the following
    ```python    
    TIME_RUNNER = "testopwatch.DjangoTimeRunner"
    ```
3. run your test with the built-in manager 
   ```shell
   ❯ python manage.py test --failfast --parallel
   ```

