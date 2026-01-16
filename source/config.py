import os

class LocalConfig:
    backend_url: str = "http://127.0.0.1:8000/users/"
    
class DevConfig(LocalConfig):
    backend_url: str = "http://backend:5000/users/"
    
    
def get_config():
    env = os.getenv("ENVIRONMENT")
    
    if not env:
        print("Local config")
        return LocalConfig
    
    else:
        print("Dev config")
        return DevConfig
    
configuration = get_config()