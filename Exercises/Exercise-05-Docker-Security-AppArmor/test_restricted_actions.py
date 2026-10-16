import docker

client = docker.from_env()

info = client.info()
security_options = info.get("SecurityOptions", [])

if not any("apparmor" in str(option).lower()
           for option in security_options):
    raise RuntimeError(
        "AppArmor is unavailable on this Docker daemon. "
        "Run the tests on a supported Linux Docker host."
    )

container = None

try:
    container = client.containers.run(
        "flask-apparmor:latest",
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="apparmor-restricted-test"
    )

    print("Container started:", container.short_id)

    for command in [
        ["cat", "/etc/passwd"],
        ["/bin/bash", "-c", "echo execution-test"]
    ]:
        result = container.exec_run(command)
        print("Command:", command)
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace"))

finally:
    if container is not None:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
