# BUG-002 — Message Over Character Limit Is Still Sent

## Summary

The system displays a warning when a message exceeds the 500-character limit but still allows the message to be sent.

## Preconditions

- User is logged into CareConnect
- User has access to the messaging feature

## Steps to Reproduce

1. Open the messaging feature
2. Enter a message containing 501 characters
3. Observe the warning that the message exceeds the 500-character limit
4. Click Send

## Expected Result

The system should prevent the message from being sent because it exceeds the 500-character limit.

## Actual Result

The warning is displayed, but the full 501-character message is still sent successfully.

## Severity

Medium

## Priority

Medium

## Status

Open
