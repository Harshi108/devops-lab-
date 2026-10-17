# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Create a Jenkins CI/CD pipeline for a Python Flask application.

## Technologies
- Python
- Flask
- Jenkins
- Git and GitHub

## Project Files
- app.py: Flask web application.
- requirements.txt: Python dependencies.
- test_app.py: Unit test for the application.
- Jenkinsfile: Defines the multi-stage pipeline.
- README.md: Exercise documentation.

## Pipeline Stages
1. Build: Install Python dependencies.
2. Test: Run unit tests.
3. Deploy: Copy application files to a deployment directory.
4. Run Application: Start the deployed Flask application.
5. Test Application: Check the deployed application response.

## Expected Output
Hello, Jenkins Multi-Stage Pipeline!

## Jenkins Configuration
1. Create a new Jenkins Pipeline job.
2. Select Pipeline script from SCM.
3. Select Git and enter your GitHub repository URL.
4. Set the Script Path to:
   Exercises/Exercise-09-Jenkins-Multi-Stage-Pipeline/Jenkinsfile
5. Save the job and select Build Now when ready.

## Note
The Jenkins agent requires Python 3, pip, and the necessary dependencies.
The pipeline has not been executed as part of preparing these files.