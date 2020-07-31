docker_build('gui-people-nandy-io', './gui')
docker_build('api-people-nandy-io', './api')

k8s_yaml(kustomize('.'))

k8s_resource('gui', port_forwards=['6580:80'])
k8s_resource('mysql', port_forwards=['6548:5678'])
k8s_resource('api', port_forwards=['16580:80', '16548:5678'])
