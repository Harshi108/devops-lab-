# Exercise 5: Docker Security with AppArmor

## Objective
Explore Docker container security and AppArmor profile configuration.

## Files
- app.py: Flask application.
- Dockerfile: Builds the Flask image.
- my-apparmor-profile: Starter AppArmor profile.
- requirements.txt: Docker Python SDK dependency.
- apply_apparmor.py: Python SDK script with an AppArmor support check.
- test_restricted_actions.py: Restricted-action test script with a support check.

## Verification
- Built the flask-apparmor image.
- Started the Flask container on port 5001.
- Verified the Flask response using Invoke-RestMethod.
- Docker Desktop reported seccomp and cgroupns, but did not advertise AppArmor.

## Platform Limitation
Custom AppArmor profile enforcement was not verified on Windows Docker Desktop.
Run the profile validation and restricted-action tests on a Linux Docker host with AppArmor enabled.
The starter profile must be validated and loaded before enforcement can be claimed.

## Conclusion
Prepared the Docker security exercise files and verified the Flask container.
Custom AppArmor enforcement remains pending validation on a supported Linux host.
