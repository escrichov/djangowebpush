Django Push Example
=============

1. Setup Project

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

2. Install ngrok

Go to https://ngrok.com/download

3. Run server and ngrok tunnel

```bash
python manage.py runserver
```

In other tab:
```bash
ngrok http 8000
```

3. Open ngrok hostname in browser. Allow notifications

4. Send notification with form

5. Send notifications following /send_push url