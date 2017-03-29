import os
import click

from .registry import service, package_language, repository_host


@click.group()
def main():
    pass

def ensure_config_run():
    if os.path.exists('config.py'):
        with open('config.py', 'r') as f:
            exec(f.read())


def ask_questions(name, handler):

    function = handler['function']
    arguments = handler['arguments']

    parameters = []
    for argument in arguments:
        # TODO: recongize default values from functions
        value = click.prompt(argument['description'], type=argument['type'], hide_input='password' in argument['name'])
        parameters.append(value)

    print('Running setup for {0}... '.format(name), end='')
    try:
        return function(*parameters)
    finally:
        click.echo(click.style('done', 'green'))


@click.command()
def quickstart():

    ensure_config_run()

    click.echo(click.style("Welcome to LetThereBe!", 'red'))
    print('')
    print('Please answer the following questions to set up your project (just press Enter to accept default values when available)')

    # Set up repo

    print('')
    click.echo(click.style("Step 1 - Setting up repository", 'magenta'))
    print('')

    available_repo_hosts = sorted(repository_host.members)

    if 'github' in available_repo_hosts:
        default_repo_host = 'github'
    else:
        default_repo_host = available_repo_hosts[0]

    repo_host = click.prompt('Which service would you like to set up your repository on?',
                             default=default_repo_host, type=click.Choice(available_repo_hosts))

    repo = ask_questions(repo_host, repository_host.members[repo_host])

    # Set up language

    print('')
    click.echo(click.style("Step 2 - Setting up the package layout", 'magenta'))
    print('')

    available_languages = sorted(package_language.members)

    if 'python' in available_languages:
        default_language = 'python'
    else:
        default_language = available_languages[0]

    language = click.prompt('Which language would you like to set up a project for?',
                            default=default_language, type=click.Choice(available_languages))

    local_path = ask_questions(language, package_language.members[language])

    # Add code to repository
    repo.add_directory_to_repo(local_path, '.', 'Initial commit with package layout')

    # Set up services

    print('')
    click.echo(click.style("Step 3 - Setting up services", 'magenta'))
    print('')

    available_services = sorted(service.members)

    services = click.prompt('Which services do you want to set up? (comma separated)', default=', '.join(available_services))

    for s in services.split(','):
        ask_questions(s.strip(), service.members[s.strip()])

    # Give final instructions_to_get_repo
    print('')
    click.echo(click.style("Epilogue", 'magenta'))
    print('')
    print(repo.instructions_to_get_repo())

main.add_command(quickstart)
