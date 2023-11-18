from invoke import task

"""
Loading the image in objects/wall.py causes an import error when
running the start script. This can be fixed by changing the path to
'src/images/grass.png'
"""

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