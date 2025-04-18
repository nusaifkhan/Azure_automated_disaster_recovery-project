from azure.identity import DefaultAzureCredential

def get_azure_credentials():
    try:
        # Use DefaultAzureCredential for authentication
        credential = DefaultAzureCredential()
        print("Azure authentication successful")
        return credential
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
