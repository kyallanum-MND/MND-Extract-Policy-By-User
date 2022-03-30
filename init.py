import requests
import json

#Declare API information
api_request = {
    "requestType": "getAllProducts",
    "userKey": "",
    "orgToken": ""
}

request_suffix = "/api/v1.3"
request_headers = {"Content-Type": "application/json"}

environment = input("Enter the URL of the environment: ")
api_request['userKey'] = input(f"Enter your User Key for {environment}: ")
api_request['orgToken'] = input(f"Enter the organization token: ")

#Get the products in the organization
products_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))

products_json = json.loads(products_str.content)
product_list = []
for product in products_json['products']:
    product_list.append({"productName": product['productName'], "productToken": product['productToken']})
    
del api_request['orgToken']

#Get the projects in the organization
api_request["requestType"] = "getAllProjects"

for product in product_list:
    api_request["productToken"] = product["productToken"]
    projects_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
    projects_json = json.loads(projects_str.content)
    product["projects"] = projects_json["projects"]


#Get the policies for each product and project
for product in product_list:
    api_request['requestType'] = "getProductPolicies"
    api_request['productToken'] = product["productToken"]            
    product_policies = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
    product_policies_json = json.loads(product_policies.content)
    product['product_policies'] = product_policies_json['policies']
    
    for project in product["projects"]:
        api_request['requestType'] = "getProjectPolicies"
        del api_request['productToken']
        api_request['projectToken'] = project['projectToken']
        project_policies = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
        project_policies_json = json.loads(project_policies.content)
        project['project_policies'] = project_policies_json['policies']
        
    del api_request['projectToken']

#Get all policies from a specific user.
user_email = input("Enter the Email Address of the Policy Owner: ")
for product in product_list:
    print(f"Product Name: {product['productName']}")
    for product_policy in product["product_policies"]:
        if product_policy["owner"]["email"] == user_email:
            print(f"\tPolicy Name: {product_policy['name']}\n\tOwner: {user_email}")
    
    if bool(product['product_policies']) == False:
        print(f"\tNone")
        
    print("\t==============================================")
        
    for project in product["projects"]:
        print(f"\tProject Name: {project['projectName']}")
        for project_policy in project["project_policies"]:
            if project_policy["owner"]["email"] == user_email:
                print(f"\t\tPolicy Name: {product_policy['name']}\n\t\tOwner: {user_email}")
        if bool(project['project_policies']) == False:
            print(f"\t\tNone")
    
    print("\n")
