
API_HOSTS = {
    # "test": "http://http://192.168.40.158/shop/wp-json/wc/v3/", '''Use when running locally'''
    "test": "http://192.168.40.158/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    # "test": "http://http://192.168.40.158/shop/", '''Use when running locally'''
    "test": "http://192.168.40.158/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "localhost",
                       "database": "wp_",
                       "table_prefix": "wordpress",
                       "port": 3306
                       },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host": "host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'docker': {
              "test": {
                  "host": "host.docker.internal",
                  "database": "wordpress",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "wordpress",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "wordpress",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
}
