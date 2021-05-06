payload_create_workspace = "{\"data\":{\"type\":\"NotebookSession\",\"attributes\":{\"title\":\"test1\"," \
                           "\"notebook_type\":\"jupyterlab\",\"external_disk_slug\":\"\"," \
                           "\"external_disk_title\":\"\",\"external_disk_size\":null,\"job_datasets\":[]," \
                           "\"use_spots\":true,\"commit\":\"\",\"output_dir\":\"output\",\"git_branch\":\"master\"," \
                           "\"git_commit\":\"latest\",\"local_folders\":[]}}} "

payload_create_experiment = "{\"data\":{\"type\":\"Experiment\",\"attributes\":{\"title\":\"test1\"," \
                            "\"working_dir\":\"\"," \
                            "\"command\":\"python -c 1+1\",\"commit\":\"\"," \
                            "\"external_disk_slug\":\"\",\"output_dir\":\"output\",\"restart_if_stuck\":false," \
                            "\"timeout\":-1," \
                            "\"auto_sync\":true,\"job_datasets\":[],\"webhooks\":false," \
                            "\"notifications\":{" \
                            "\"on_error\":false,\"on_success\":false},\"algorithm\":\"GridSearch\",\"objective\":null," \
                            "\"objective_function\":\"min\",\"objective_goal\":null,\"max_jobs\":-1," \
                            "\"parallel_jobs\":1," \
                            "\"experiments_count\":1,\"parameters\":[],\"local_folders\":[],\"git_commit\":\"latest\"," \
                            "\"git_branch\":\"master\",\"timezone\":\"Asia/Calcutta\",\"params\":[]," \
                            "\"is_scheduled\":false," \
                            "\"is_recurring\":false}}} "

payload_create_webservice = "{\"data\":{\"type\":\"Endpoint\",\"attributes\":{\"file_name\":\"predict.py\"," \
                            "\"script\":\"\"," \
                            "\"function_name\":\"predict\",\"prep_file\":\"\",\"prep_function\":\"\"," \
                            "\"commit\":\"\"," \
                            "\"env_setup\":\"python_3\",\"input_file\":false,\"kafka_brokers\":[\"\"]," \
                            "\"kafka_input_topics\":[" \
                            "\"\"],\"kafka_output_topics\":[\"\"],\"command_type\":\"file\"," \
                            "\"models_config_file\":\"\"," \
                            "\"title\":\"TestSample\",\"git_branch\":\"master\",\"git_commit\":\"latest\"," \
                            "\"flask_config\":[]," \
                            "\"nginx_config\":[],\"gunicorn_config\":[],\"max_replica\":1," \
                            "\"min_replica\":1,\"local_folders\":[]," \
                            "\"kind\":0}}} "

payload_create_stream = "{\"data\":{\"type\":\"Endpoint\",\"attributes\":{\"file_name\":\"predict.py\",\"script\":\"\"," \
                        "\"function_name\":\"predict\",\"prep_file\":\"\",\"prep_function\":\"\",\"commit\":\"\"," \
                        "\"env_setup\":\"python_3\",\"input_file\":false,\"kafka_brokers\":[" \
                        "\"kafka.aks-cicd-4372.cnvrg.io:9092\"],\"kafka_input_topics\":[\"cnvrg_aut_input\"]," \
                        "\"kafka_output_topics\":[\"\"],\"command_type\":\"file\",\"models_config_file\":\"\"," \
                        "\"title\":\"TestSample\",\"git_branch\":\"master\",\"git_commit\":\"latest\"," \
                        "\"flask_config\":[]," \
                        "\"nginx_config\":[],\"gunicorn_config\":[],\"max_replica\":1,\"min_replica\":1," \
                        "\"local_folders\":[]," \
                        "\"kind\":1}}} "

payload_create_batch = "{\"data\":{\"type\":\"Endpoint\",\"attributes\":{\"file_name\":\"predict.py\",\"script\":\"\"," \
                       "\"function_name\":\"predict\",\"prep_file\":\"\",\"prep_function\":\"\",\"commit\":\"\"," \
                       "\"env_setup\":\"python_3\",\"input_file\":false,\"kafka_brokers\":[\"\"]," \
                       "\"kafka_input_topics\":[" \
                       "\"\"],\"kafka_output_topics\":[\"\"],\"command_type\":\"file\",\"models_config_file\":\"\"," \
                       "\"title\":\"TestSample\",\"git_branch\":\"master\",\"git_commit\":\"latest\"," \
                       "\"flask_config\":[]," \
                       "\"nginx_config\":[],\"gunicorn_config\":[],\"max_replica\":1,\"min_replica\":1," \
                       "\"local_folders\":[]," \
                       "\"kind\":2}}} "

payload_voila_app = "{\"data\":{\"type\":\"Webapp\",\"attributes\":{\"webapp_type\":\"voila\",\"title\":\"Testsample\"," \
                    "\"file_name\":\"basics.ipynb\",\"commit\":\"\",\"job_datasets\":[],\"git\":{" \
                    "\"branch\":\"master\",\"commit\":\"latest\"}," \
                    "\"output_dir\":\"output\",\"strip_sources\":false}}} "

payload_shiny_app = "{\"data\":{\"type\":\"Webapp\",\"attributes\":{\"webapp_type\":\"rshiny\"," \
                    "\"title\":\"testsample\"," \
                    "\"file_name\":\"app.R\",\"commit\":\"\"," \
                    "\"job_datasets\":[],\"git\":{\"branch\":\"master\",\"commit\":\"latest\"}," \
                    "\"output_dir\":\"output\"," \
                    "\"strip_sources\":false}}} "

payload_dash_app = "{\"data\":{\"type\":\"Webapp\",\"attributes\":{\"webapp_type\":\"dash\",\"title\":\"testsample1\"," \
                   "\"file_name\":\"app.py\",\"commit\":\"\"," \
                   "\"job_datasets\":[],\"git\":{\"branch\":\"master\",\"commit\":\"latest\"}," \
                   "\"output_dir\":\"output\"," \
                   "\"strip_sources\":false}}} "
