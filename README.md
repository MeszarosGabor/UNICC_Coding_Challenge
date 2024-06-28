# UNICC_Coding_Challenge

## Considerations (partially based on the problem statements as well as on email exchanges with the team)
- We develop a command line tool only. The tool takes no parameters (per problem statement) and operates with reasonably set constants.
- The current implementation assumes that the contancts JSON input can be stored in memory. This constraint will be lifted at a later commit. 

## SETUP
- Have Python 3.11+ installed.
- Set your pythonpath variable to the root of the repository (such as ```export PYTHONPATH=$PYTHONPATH:.``` from the root on Linux-based systems).
- Install the necessary requirements: ```pip install -r requirements.py```.

## RUN THE APPLICATION
From the repo root run 
```
python app/main.py
```
The execution will complete with several log lines of the individual exchanges, then a general statistics of the notifications sent will be logged, such as:
```
2024-06-28 11:10:52,563 - __main__ - INFO - Completed. Statistics:
2024-06-28 11:10:52,563 - __main__ - INFO - PayloadValidationResult.VALID_PAYLOAD: 186
2024-06-28 11:10:52,563 - __main__ - INFO - PayloadValidationResult.MISSING_CONTACT_OF_NOTIFICATION_TYPE: 64
```

## Additional work planned
- Support custom payload (this contradicts the problem statement clear direction of "Also, the code should not take any parameters.")
That being said, there would be great value in supporting custom JSON payloads that we can share with the contacts.
- Customization (again, assuming we lift the above restriction) of the command line tool to specify single/multi-threaded execution.
- Dockerization of the application.