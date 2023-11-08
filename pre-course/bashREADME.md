In vscode terminal, it's cant run many operation such as wc or ls[Not Linux Command line]
- use Git Bash, WSL, or Google Cloud Shell instead!
- Bash มาจากคำว่า Bourne-again shell ซึ่งเป็น Unix shell ประเภทหนึ่ง

In Google Cloud Shell:

1. **Ending a Session:** Ending a session means that your current session in Google Cloud Shell will be terminated, and any data that is only stored in the temporary session environment will be lost. This includes files and data you created or modified during your current session. When you exit or close your Cloud Shell session, it's akin to logging out, and the session's data is not retained.

2. **Virtual Storage:** Google Cloud Shell uses *virtual storage*. It provides a temporary and ephemeral file system for your session. It's not local storage on your local computer or persistent cloud storage like Google Cloud Storage. The data is associated with your user account and is available as long as your session is active. When you end the session or if the session expires due to inactivity, the data is removed.

To ensure the safety and persistence of your data, it's a good practice to regularly back up your important files to more permanent storage solutions such as Google Cloud Storage, Google Drive, or other cloud storage options. This way, you can access your data from different sessions or devices and prevent data loss when your Cloud Shell session ends.