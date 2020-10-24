# Notifies when Network Usage exceeds a specifies limit.
* Checks for network usage every 5 seconds.
* A notification is sent when the usage exceeds a specified limit provided by the user.

## Executing script
* `pip install -r requirements.txt`
* `python app.py <specified limit in MB>`
* for e.g `python app.py 100`

## Output
Executing `python app.py 4` gives:

**Init Notification**
![op_init](images/op_init.png)

**When usage exceeds specified limit**
![op_notif](images/op_notif.png)
