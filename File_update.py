def update_server_config (filepath, key, value):
    with open(filepath, 'r') as file:
        configs = file.read()
    
    # Update the configuration value
    #config = config.replace(f"{key}=600", f"{key}={value}")
    
    with open(filepath, 'w') as file:
        for config in configs.splitlines():
            if key in config:
                file.write(key +"=" + str(value) + "\n")
            else:
                file.write(config + "\n")

update_server_config('C:\\Users\\pemma\\OneDrive\\Documents\\Python_tutorial\\server.conf', 'MAX_CONNECTIONS', 500)       