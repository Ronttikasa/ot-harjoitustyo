from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)
    
@task # käynnistys jos python3-komento ei toimi
def start_win(ctx):    
    ctx.run("python src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
