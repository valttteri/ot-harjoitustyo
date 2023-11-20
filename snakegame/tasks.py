from invoke import task

@task
def start(ctx):
    ctx.run('python src/main.py')

@task
def test(ctx):
    ctx.run('coverage run --branch -m pytest src')

@task
def coverage_report(ctx):
    ctx.run('coverage report')
    ctx.run('coverage html')