### WS-Extract-Policies-By-User

This is a tool created by WhiteSource Support, to easily find policies created by a user in a WhiteSource Organization. 

To run, you will need Python installed. From there you just need to:

```
$> pip install -r requirements.txt
$> python init.py
```

The concept behind this is that it will get every single product and project in your organization, and then check for policies related to the user specified and print them out.