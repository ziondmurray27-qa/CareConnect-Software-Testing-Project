# CareConnect Software Testing Project

CareConnect is a simulated healthcare application used to demonstrate software testing skills across manual testing, test case design, bug reporting, API testing, SQL validation, and basic Playwright automation.

## Features Tested

- Login and authentication
- Appointment scheduling
- Provider search
- Messaging
- Notifications
- Session timeout

## Testing Types Used

- Manual functional testing
- Positive and negative testing
- Boundary testing
- API testing
- SQL database validation
- Playwright automation
- Pytest
- Regression testing
- Basic CI/CD with GitHub Actions

## Example Defects Identified

### Appointment Conflict

The application displayed a scheduling conflict warning but still allowed a duplicate appointment to be created for the same patient and time slot.

### Message Character Limit

The application displayed a warning when a message exceeded the 500-character limit but still allowed the message to be sent.

### Data Consistency

Appointment information appeared correctly in the API response but was stored incorrectly in the database during validation.

## Tools and Technologies

- Postman
- SQL
- Playwright
- Pytest
- Git
- GitHub
- GitHub Actions
- Markdown

## What I Learned

This project helped me practice turning software requirements into test scenarios and test cases, comparing expected and actual results, documenting defects, and understanding how UI, API, and database testing connect.

I also practiced using assertions in automated tests and learned how manual and automated testing can work together as part of the same QA workflow.

## Project Status

This project is currently being developed as a QA portfolio project. Additional test documentation, API testing examples, SQL validation, automation tests, and CI/CD configuration will be added as the project progresses.

## Automation Note

CareConnect is a simulated application and does not have a live testing environment. The Playwright tests and GitHub Actions workflow in this repository demonstrate the structure and approach I would use for browser automation and CI/CD in a real QA project.
