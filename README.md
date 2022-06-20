[![Logo](https://whitesource-resources.s3.amazonaws.com/ws-sig-images/Whitesource_Logo_178x44.png)](https://www.whitesourcesoftware.com/)  
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

# [Mend Extract Policy By User Tool](https://github.com/kyallanum-MND/MND-Extract-Policy-By-User)
This tool allows you to extract all of the policies a user owns.

## Prerequisites
* Python 3.6+

## Installation and Execution by cloning this repo:
1. Clone the repo:
```shell
git clone https://github.com/kyallanum-MND/MND-Extract-Policy-By-User.git
```

2. Run setup.py
```shell
cd MND-Extract-Policy-By-User
python setup.py install
```

3. Execution
```shell
mnd_extract_policy_by_user
```

## Execution
When running this script there are two stages: Information Gathering, and Sorting.
1. Information Gathering runs API requests to get all of the products and projects in an organization, and then gets every single policy for every single product and project.
2. Sorting goes through every single product and project and determines whether a policy owned by the given user exists.

At the end it will create a file called policies.txt that will create a file in the following format:
```
Product Name: <Product Name>
    Policy Name: <Policy Name>
        Owner: <user email>
    ==============================================
    Project Name: <Project Name>
        Policy Name: <Policy Name>
            Owner: <user email>
```

If there is no policy under a Product or Project, then it will print "None" to show that it did in fact check that organization. In order to find all of the policies that a user owns, they can Ctrl+F \<user email\> and this will show all of the policies the user owns.