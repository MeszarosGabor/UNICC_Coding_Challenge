# UNICC_Coding_Challenge

## Considerations (partially based on the problem statement as well as on email exchanges with the team)
- We develop a command line tool only. The tool takes no parameters (per problem statement) and operates with reasonably set constants.
- The current implementation NO LONGER assumes that the contancts JSON input can be stored in memory. We assume we can save the JSON file to disk from
which we can parse it without loading it all into memory (and eventually delete the temporary file).
- The current solution nevertheless assumes that the input JSON file is parseable. While the contact dictionaries may be remiss of certain values
(the application is prepared to handle that), the whole structure of the file should be a valid JSON. Error handling and cherry-picking of partial valid
items has been deemed out of scope of the current project. See "Additional Work Planned" for further details.
- According to the problem specification, `name` was considered a mandatory parameter of the notification. We adhere to this filtering logic but point out
that the name field is currently not used in any of the notification methods (sms, email, post).

## Setup
The application has been dockerized. Have Docker and docker compose installed. No additional setup is required.

## Run the Application
From the repo root, run:
```
docker compose run app
```
The execution will complete with several log lines of the individual exchanges, then a general statistics of the notifications sent will be logged, such as:
```
2024-06-28 11:10:52,563 - __main__ - INFO - Completed. Statistics:
2024-06-28 11:10:52,563 - __main__ - INFO - PayloadValidationResult.VALID_PAYLOAD: 186
2024-06-28 11:10:52,563 - __main__ - INFO - PayloadValidationResult.MISSING_CONTACT_OF_NOTIFICATION_TYPE: 64
```

## Run the Unit Tests
From the repo root, run:
```
docker compose run test
```
Sample output:
```
app/tests/test_bulk_notification_manager.py ....                                                                                                                          [ 20%]
app/tests/test_notification_manager.py ............                                                                                                                       [ 80%]
app/tests/test_transaction_fetcher.py ....                                                                                                                                [100%]

============================================================================== 20 passed in 0.09s ===============================================================================
```

## Additional Work Planned
- Support custom payload (this contradicts the problem statement's clear direction of "Also, the code should not take any parameters.")
That being said, there would be great value in supporting custom JSON payloads that we can share with the contacts.
- Customization (again, assuming we lift the above restriction) of the command line tool to specify single/multi-threaded execution.
- Error handling of the JSON loading and retrieval of partially valid data (open-ended, requires specification of what can be considered a valid chunk of a corrupted overall JSON structure).
- (long term, product-level decision) The current representation of the contact details is cumbersome. The author proposes the migration
of the input files into one of the following: JSONL, CSV, SQL table.

## Timer
The current solution was implemented, tested, and documented in 2 sessions amounting to ~4 hours of work in total.
