# essbackend
an api to generate docs and details for a project

to begin install requirements in the requirements.txt file, create a superuser, generate a token using the api/token route. only authenticated users can create new users via api 

available routes include :

api/ ^projects/$ [name='esgproject-list'] 
api/ ^projects\.(?P<format>[a-z0-9]+)/?$ [name='esgproject-list']
api/ ^projects/(?P<pk>[^/.]+)/$ [name='esgproject-detail']
api/ ^projects/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='esgproject-detail']
api/ ^tasks/$ [name='usertask-list']
api/ ^tasks\.(?P<format>[a-z0-9]+)/?$ [name='usertask-list']
api/ ^tasks/(?P<pk>[^/.]+)/$ [name='usertask-detail']
api/ ^tasks/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='usertask-detail']
api/ ^$ [name='api-root']
api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/create_user/ [name='create-user']
api/generate_report/<str:format>/<int:project_id>/ [name='generate-report']
api/token/ [name='token_obtain_pair'] #to get jwt tokens for user creation
api/token/refresh/ [name='token_refresh']
