### WS-Extract-Policies-By-User

This is a tool created by WhiteSource Support, to easily find policies created by a user in a WhiteSource Organization. 

To run, you will need Python installed. From there you just need to:

```bash
$> python -m venv env                 #Install virtual environment
$> env/scripts/activate               #Activate virtual environment
$> pip install -r requirements.txt    #Install required packages
$> python init.py                     #Run the script
```

The concept behind this is that it will get every single product and project in your organization, and then check for policies related to the user specified and print them out. It will output the whole organization structure in a "policies.txt" file, and you will be able to search for the user's email address to see which policies that user owns.
