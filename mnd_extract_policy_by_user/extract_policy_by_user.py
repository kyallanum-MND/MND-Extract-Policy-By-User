import requests
import json

class WSDataNotReturnedError(Exception):
    def __init__(self, msg):
        print(f"Error:\n\t{msg}")
        super().__init()

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
try:
    products_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
except Exception:
    raise WSDataNotReturnedError("Products in the given organization were not found.")

products_json = json.loads(products_str.content)

if "errorMessage" in products_json:
    raise WSDataNotReturnedError(products_json['errorMessage'])

product_list = []
for product in products_json['products']:
    product_list.append({"productName": product['productName'], "productToken": product['productToken']})
    
del api_request['orgToken']

#Get the projects in the organization
api_request["requestType"] = "getAllProjects"

for product in product_list:
    api_request["productToken"] = product["productToken"]
    print(f"Getting projects for product: {product['productName']}...", end="")
    try:
        projects_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
    except Exception:
        raise WSDataNotReturnedError(f"Product {product['productName']} - {product['productToken']} returned an error:")
    
    projects_json = json.loads(projects_str.content)
    
    if "errorMessage" in projects_json:
            raise WSDataNotReturnedError(projects_str['errorMessage'])
    
    print("Finished")
    product["projects"] = projects_json["projects"]


#Get the policies for each product and project
for product in product_list:
    api_request['requestType'] = "getProductPolicies"
    api_request['productToken'] = product["productToken"]
    
    print(f"Getting Policies for product: {product['productName']}...", end="")
    try:           
        product_policies = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
    except Exception:
        raise WSDataNotReturnedError(f"Product {product['productName']} - {product['productToken']} returned an error when attempting to get policies.")
    
    product_policies_json = json.loads(product_policies.content)
    
    if "errorMessage" in product_policies_json:
        raise WSDataNotReturnedError(product_policies_json['errorMessage'])
    
    print("Finished")
    
    product['product_policies'] = product_policies_json['policies']
    
    print(f"\tGetting Policies for projects in the product: {product['productName']}...", end="")
    
    for project in product["projects"]:
        api_request['requestType'] = "getProjectPolicies"
        api_request['projectToken'] = project['projectToken']
        
        try:
            project_policies = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
        except Exception:
            raise WSDataNotReturnedError(f"Project {project['projectName']} - {project['projectToken']} returned an error when attempting to get policies.")
        
        project_policies_json = json.loads(project_policies.content)
        
        if "errorMessage" in project_policies_json:
            raise WSDataNotReturnedError(project_policies_json['errorMessage'])
        
        project['project_policies'] = project_policies_json['policies']
        
    if "projectToken" in api_request:
        del api_request['projectToken']

    print(f"Finished")

#Get all policies from a specific user.
user_email = input("Enter the Email Address of the Policy Owner: ")
output_str = ""
for product in product_list:
    output_str += f"Product Name: {product['productName']}\n"
    num_policies = 0
    for product_policy in product["product_policies"]:
        if product_policy["owner"]["email"] == user_email:
            output_str += f"\tPolicy Name: {product_policy['name']}\n\tOwner: {user_email}"
            num_policies += 1
    
    if num_policies == 0:
        output_str += f"\tNone\n"
        
    output_str += "\t==============================================\n"
        
    for project in product["projects"]:
        output_str += f"\tProject Name: {project['projectName']}\n"
        num_policies = 0
        for project_policy in project["project_policies"]:
            if project_policy["owner"]["email"] == user_email:
                output_str += f"\t\tPolicy Name: {product_policy['name']}\n\t\tOwner: {user_email}\n"
                num_policies += 1
                
        if num_policies == 0:
            output_str += f"\t\tNone\n"
    
    output_str += "\n"
    
    with open("policies.txt", 'w') as f:
        f.write(output_str)

    
print("Results have been stored in: \"policies.txt\"")