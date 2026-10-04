# CareConnect SQL Validation

## Purpose

Verify that appointment data stored in the database matches the data submitted through the application and API.

## Example Query

```sql
SELECT *
FROM appointments
WHERE appointment_id = 7832;
```

## Expected Database Record

```text
appointment_id: 7832
patient_id:     1024
provider_id:    501
date:           2026-10-05
time:           14:00
status:         scheduled
```

## Validation Checks

- Appointment ID matches the expected record
- Patient ID matches the API request
- Provider ID matches the API request
- Appointment date is correct
- Appointment time is correct
- Appointment status is correct

## Example Failed Validation

If the API creates an appointment for:

```text
time: 14:00
```

but the database stores:

```text
time: 15:00
```

the test should fail because the stored appointment data does not match the expected value.

## Cancellation Validation

After cancelling appointment `7832`, run:

```sql
SELECT status
FROM appointments
WHERE appointment_id = 7832;
```

The expected result should be:

```text
status: cancelled
```

If the database still returns:

```text
status: scheduled
```

the test should fail because the database was not updated to reflect the cancellation.
