
import invoke

# Based on https://github.com/pyca/cryptography/blob/master/tasks.py


@invoke.task
def release(version):
    invoke.run("git tag -a pyuv-{0} -m \"pyuv {0} release\"".format(version))
    invoke.run("git push --tags")

@invoke.task
def upload(version):
    invoke.run("python setup.py sdist")
    invoke.run("twine upload -r pypi dist/pyuv-{0}*".format(version))

