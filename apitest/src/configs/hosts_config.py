
API_HOSTS = {
    "test": "http://192.168.40.158/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    "test": "http://192.168.40.158/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "127.0.0.1",
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
