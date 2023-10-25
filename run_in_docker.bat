SET ./env_docker.sh

SET DATE_WITH_TIME=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%

docker run --rm ^
--network=wordpress_default ^
-v %CD%/apitest:/automation/apitest ^
-e WC_KEY=%WC_KEY% ^
-e WC_SECRET=%WC_SECRET% ^
-e WP_HOST=%WP_HOST% ^
-e MACHINE=%MACHINE% ^
-e DB_USER=%DB_USER% ^
-e DB_PASSWORD=%DB_PASSWORD% ^
api_test ^
pytest -c /automation/apitest/pytest.ini ^
--color=yes ^
--html /automation/apitest/results/test_results_%DATE_WITH_TIME%.html ^
--self-contained-html ^
-m %1% /automation/apitest