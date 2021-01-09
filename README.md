## The latest version of this prototype is now fully self-hosted and available at:

https://github.com/mm-io/hasura-django-starter

------

# Standard Prototype
## A Svelte, Django Rest Framework, and Firebase Prototype Starter

![Example App](./readme-example.gif?raw=true "Example App")

### Pre-Requisites:
- Create a Firebase application (https://firebase.google.com/)
     - Doesn't require Firestore, just a project and then enabling the username and Google sign-in methods here:
        - https://console.firebase.google.com/u/0/project/PROJECT-NAME/authentication/providers
- Install Docker (https://docs.docker.com/get-docker/)

### Features:
- Django Rest Framework API w/ JWT from Firebase (using: https://github.com/garyburgmann/drf-firebase-auth)
- Import / Export from Django Admin
- SQLite Database (For  simplicity) 
- Svelte Front-End (https://svelte.dev/)
- Basic CRUD Application Example
- Custom User Model & Sample User Management
- Storybook - for Component Driven Design (https://storybook.js.org/) - w/ Knobs & Notes Plugins

### How It Works:
![How It Works](./readme-token-diagram.png?raw=true "How It Works")

-----
## Quickstart:
- Clone / download this repo
- In terminal / command line change your directory to the project files
- Set up the frontend to use Firebase:
    - Grab the firebaseConfig which can be found at the bottom of:
        - https://console.firebase.google.com/u/0/project/PROJECT-NAME/settings/general/
    - Paste it into the space available in:
        - frontend/src/auth/firebase.js
- Set up the backend to use Firebase:
    - Download a service account key (.json) which can be found at the bottom of:
        - https://console.firebase.google.com/u/0/project/PROJECT-NAME/settings/serviceaccounts/adminsdk
    - Move it into the space available in:
        - backend/app/config/project.json (rename to project.json)
- Run the following command to start the containers:

```
docker-compose up
```

Need to restarted either the frontend or backend?

```
docker-compose up --force-recreate sp_frontend
```

or

```
docker-compose up --force-recreate sp_backend
```

Want to know more about Docker? I have a litter more information about it over here?

https://martinmark.com/getting-to-know-docker-running-your-first-container/

You'll be able to access the applications through:

### Application Frontend:
http://localhost:8080

### Storybook:
http://localhost:8081

### Django Admin:
http://localhost:8000/admin

### Django API:
http://localhost:8000/api

-----
## Project Structure:

### Backend:
- /backend/requirements.txt - Any packages to install using PIP
- /backend/app - Base project settings
    - /backend/app/settings.py - Project settings
    - /backend/app/urls.py - Routes user to API / admin URL routes
- /backend/backend - API
    - /backend/backend/models.py - Data models for database
    - /backend/backend/serializers.py - Serializer for sending data
    - /backend/backend/api.py - Views for data
    - /backend/backend/urls.py - URLs for routing requests (within http://localhost:8000/api/...)
    - /backend/backend/admin.py - Adding fields to the Django Admin

### Frontend:
*As you add your designs to /src they'll be compiled into /public and will be available at: http://localhost:8080*

- /frontend/src - Project Code
    - /frontend/src/App.svelte - Entry: You'll be able to define your routing here for your URLs => components
    - /frontend/src/package.json - Any packages to install using NPM
    - /frontend/src/pages - Folder contains all component pages
    - /frontend/src/components - Folder contains all shared components > just Sidebar and a Redirect component for now.
    - /frontend/src/shared.js - Shared functions (just an error handler for now)
    - /frontend/src/auth - Folder with the auth page and Firebase configurations
- /frontend/public - Post Compiled Frontend
    - /frontend/public/index.html - For an un-packaged CDN libraries you can add them manually to the header
    - /frontend/public/global.css - The global CSS for the project => for any unscoped components
- /frontend/stories - Storybook Stories
    - Each story has a .svelte file which is he actual component and a .js file to describe the story - ex:
        - button.svelte (is a scoped CSS component)
        - button.stories.js
        - sidebar.svelte (is a global CSS component)
        - sidebar.stories.js
-----
## Django: Creating a Superuser:
```
docker exec -it sp_backend python ./manage.py createsuperuser
```
You can use this account to login through http://localhost:8000/admin

-----
## Django: Generate New Secret Key:
It's recommended that if you do anything with this demo which is public that you update the secret key.

You can generate a new key with (https://humberto.io/blog/tldr-generate-django-secret-key/):

```
docker exec -it sp_backend python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

and then replace the key found in:
`/backend/app/settings.py`

-----
## Django: Updating the API:

### /backend/backend/models.py
- `user_model` - Custom user class which you can extend
- `BaseModel` - Custom base class > adds UUID to all other fields
- Two models > Ticket and Messages which are related (**good example for creating a new model**)

If you make changes to models, you can migrate the database with the following (or also recreate the container wih the recreate command above):

```
docker exec -it sp_backend python ./manage.py makemigrations && docker exec -it sp_backend python ./manage.py migrate
```

### /backend/backend/serializers.py
- `k_created_by` - adds the current signed in user's ID when adding through the API
- `k_username` - looks up the added user's email for display

### /backend/backend/api.py
- `IsAdministrator` - Custom permission which we can use later - using the custom IsAdministrator field which we added in models
- `filterset_fields` - Allow us to filter queries by the ID
- Permissions are added through `permission_classes`
- `my_profileViewSet` has a filter to only show the logged-in user's profile details

### /backend/backend/urls.py
- Where the user will be able to access the model through

### /backend/backend/admin.py
- Admin Forms and Admin Models > and then a registering at the bottom
- Using the `ImportExportMixin` will display an Import and Export button in the admin

-----
## Svelte: Using Legacy Libraries (& jQuery):

Above in **Product Structure** I mentioned that you can add extra libraries into the header via `/frontend/public/index.html`.

You'll still be able to use your older libraries which you may have been using to design your app - you just need to keep 2 things in mind:
1) the component lifecycle
2) `$` is a reserved character in svelte.

For the lifecycle, I recommend reading the following 4 pages to get an idea around how Svelte handles running scripts at different phases of the component lifecycle (https://svelte.dev/tutorial/onmount). You're most likely going to end up using onMount since it's the closest to what you may be used to loading static pages.

The the `$` character - you can get around this by using `window.$` (as was mentioned here: https://stackoverflow.com/a/58883964).

So for instance, intializing the datatables.net library (which is a great older datatable enhancement library) would look like:

```
window.$('#datatable').DataTable({ ...
```

instead of:

```
$('#datatable').DataTable({ ...
```
