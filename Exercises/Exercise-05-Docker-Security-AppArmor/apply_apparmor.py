import docker
import json

client = docker.from_env()

try:
    info = client.info()
    security_options = info.get("SecurityOptions", [])
    print("Docker security options:", security_options)

    if not any("apparmor" in str(option).lower()
               for option in security_options):
        raise RuntimeError(
            "AppArmor is not advertised by this Docker daemon. "
            "Run this exercise on a Linux Docker host with AppArmor enabled."
        )

    image, build_logs = client.images.build(
        path=".",
        tag="flask-apparmor:latest"
    )
    print("Built image:", image.tags)

    container = client.containers.run(
        "flask-apparmor:latest",
        ports={"5000/tcp": 5002},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-sdk"
    )

    print("Container started:", container.short_id)

    details = client.api.inspect_container(container.id)
    print("Requested security options:",
          details["HostConfig"].get("SecurityOpt"))

    print("Note: verify the active profile on the Linux host too.")

    container.stop()
    container.remove()
    print("Container stopped and removed.")

except Exception as exc:
    print(type(exc).__name__ + ":", exc)
