# Exercise 8: Jenkins Hello World Job

## Objective
Create a simple shell script, upload it to GitHub, and configure a Jenkins Freestyle job to execute it.

## Technologies
- Jenkins
- Git
- GitHub
- Bash

## Project Files
- `hello-world.sh` - Prints a Hello World message.
- `README.md` - Exercise documentation.

## Script
The script prints:

`Hello, Jenkins!`

## Jenkins Job Configuration
1. Open the Jenkins dashboard.
2. Select **New Item**.
3. Name the job `HelloWorld`.
4. Select **Freestyle project**.
5. Configure Git under Source Code Management using your repository URL.
6. Under Build Steps, choose **Execute shell**.
7. Enter `sh hello-world.sh`.
8. Save and select **Build Now**.

## Expected Output
`Hello, Jenkins!`

## Note
The Jenkins job must be configured and executed separately. Uploading these files to GitHub does not run the job automatically.