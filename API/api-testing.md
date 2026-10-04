# CareConnect API Testing

## Endpoint

`POST /api/appointments`

## Purpose

Verify that the appointment creation API returns the correct patient, provider, date, time, status, and appointment ID.

## Example Request

```json
{
  "patientId": 1024,
  "providerId": 501,
  "date": "2026-10-05",
  "time": "14:00"
}
```

## Expected Response

```json
{
  "appointmentId": 7832,
  "status": "scheduled",
  "patientId": 1024,
  "providerId": 501,
  "date": "2026-10-05",
  "time": "14:00"
}
```

## Validation Checks

- Patient ID matches the request
- Provider ID matches the request
- Appointment date matches the request
- Appointment time matches the request
- Status is `scheduled`
- Appointment ID is returned

## Example Failed Validation

If the request is sent for:

```json
{
  "patientId": 1024
}
```

but the API response returns:

```json
{
  "patientId": 9999
}
```

the test should fail because the returned patient data does not match the request.

## Status Validation

If a newly created appointment returns:

```json
{
  "status": "cancelled"
}
```

instead of:

```json
{
  "status": "scheduled"
}
```

the test should fail because the response does not match the expected appointment state.
