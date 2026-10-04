# BUG-001 — Conflicting Appointment Is Created Despite Warning

## Summary

The system displays a scheduling conflict warning but still allows a second appointment to be created for the same patient and time slot.

## Preconditions

- Patient already has an appointment scheduled at 2:00 PM

## Steps to Reproduce

1. Open the appointment scheduling page
2. Select the patient
3. Select the already occupied 2:00 PM time slot
4. Click Schedule Appointment
5. Observe the conflict warning
6. Continue with the scheduling action

## Expected Result

The system should display the conflict warning and prevent the conflicting appointment from being created.

## Actual Result

The system displays the warning but still creates the second appointment.

## Severity

High

## Priority

High

## Status

Open
