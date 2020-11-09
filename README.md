> A batteries-included Django starter project. For a production-ready version see the book [Django for Professionals](https://djangoforprofessionals.com).

## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/), or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)

----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Pipenv](#pipenv)
  * [Docker](#docker)
* [Setup](#setup)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
DjangoX can be installed via Pip, Pipenv, or Docker depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
```

### Pip

```
$ source djangox/bin/activate
(djangox) $ pip install -r requirements.txt
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Docker

```
$ docker build .
$ docker-compose up -d
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
# Load the site at http://127.0.0.1:8000
```

For Docker, the `INTERNAL_IPS` configuration in `config/settings.py` must be updated to the following:

```python
# config/settings.py
# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
```

## Setup

```
# Run Migrations
(djangox) $ python manage.py migrate

# Create a Superuser
(djangox) $ python manage.py createsuperuser

# Confirm everything is working:
(djangox) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----

## 🤝 Contributing


## Example Workflow for Contributing

(If you don't already have a GitHub account, please create one. Your GitHub
username will be referred to later as 'YOUR_GITHUB_USERNAME'. Change it
accordingly in the steps below.)

1. Fork https://github.com/CengineLab/cenginelab using GitHub's interface to your own account.
Let's say that the forked repository is at
`https://github.com/YOUR_GITHUB_USERNAME/cenginelab` .
2. Clone the main cenginelab repository https://github.com/CengineLab/cenginelab to a local folder on
your computer, say named cenginelab/ (`git clone https://github.com/CengineLab/cenginelab cenginelab`)
3. `cd cenginelab`
4. `git remote add pullrequest https://github.com/YOUR_GITHUB_USERNAME/cenginelab`
NB: the remote named `pullrequest` should point to YOUR own forked repo, not the
main cenginelab repository! After this, your local cloned repository is prepared for
making pullrequests, and you can just do normal git operations such as:
`git pull` `git status` and so on.

5. When finished with a feature/bugfix/change, you can:
`git checkout -b your_new_fix_branch_name`
Replace `your_new_fix_branch_name` with a name that corresponds to your changes made.
6. `git push pullrequest`  # (NOTE: the `pullrequest` remote was setup on step 4)
7. On GitHub's web interface, go to: https://github.com/CengineLab/cenginelab/pulls

   Here the UI shows a dialog with a button to make a new pull request based on
   the new pushed branch.
   

8. After making your pullrequest (aka, PR), you can continue to work on the
branch `your_new_fix_branch_name` ... just do again `git push pullrequest` when you have more
commits.

9. If there are merge conflicts, or a branch lags too much behind cenginelab's master,
you can do the following:

   1. `git pull --rebase origin master` # solve conflicts and do
   `git rebase --continue`
   2. `git push pullrequest -f` # this will overwrite your current remote branch
   with the updated version of your changes.

The point of doing the above steps, is to never directly push to the main cenginelab repository, *only to your own fork*. Since your local `master` branch tracks the
main CengineLab repository's master, then `git checkout master`, as well as
`git pull --rebase origin master` will continue to work as expected and git can always do it cleanly.

Git is very flexible, so there are other ways to accomplish the same thing.
See the [GitHub flow](https://guides.github.com/introduction/git-handbook/#github), for more information.

## Using Github's hub CLI tool

You can download the `hub` tool from https://hub.github.com/ . Using
`hub`, you will not need to go through the (sometimes) slow website
to make PRs. Most remote operations can be done through the `hub` CLI
command.

NB: You still need to have a GitHub account.

### Preparation:
(steps 1..3 need to be done just *once*):

1. `hub clone CengineLab/cenginelab cenginelab`
2. `cd cenginelab`
3. `hub fork --remote-name pullrequest`

4. `git checkout -b my_cool_feature` # Step 4 is better done *once per each new feature/bugfix* that you make. remember `my_cool_name` refers to the name of a branch you create. Let the name be as close to what you are fixing as possible.

### Improve Cenginelab by making commits:

5. `git commit -am "accounts: Add user signup page"`

### Testing your commits locally:
You can test locally whether your changes have not broken something by
running: `python manage.py test`. 

### Publishing your commits to GitHub:

6. `git push pullrequest`

### Making a PR with `hub`:
(so that your changes can be merged to the main cenginelab repository)

7. `hub pull-request`

Optionally, you can track the status of your PR CI tests with:

8. `hub ci-status --verbose`


## ⭐️ Support

Give a ⭐️ if this project helped you!

## License

[The MIT License](LICENSE)


<!-- ## Docker Usage
```
# Build the Docker Image
$ docker-compose build

# Run Migrations
$ docker-compose run --rm web python manage.py migrate

# Create a Superuser
$ docker-compose run --rm web python manage.py createsuperuser

# Run Django on http://localhost:8000/
$ docker-compose up

# Run Django in background mode
$ docker-compose up -d

# Stop all running containers
$ docker-compose down

# Run Tests
$ docker-compose run --rm web pytest

# Re-build PIP requirements
$ docker-compose run --rm web pip-compile requirements/requirements.in
```-->

<!-- ## Next Steps

- Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
- Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
- Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/3.0/topics/email/#module-django.core.mail) to configure an SMTP backend
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

- [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
- [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
- `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html) -->


