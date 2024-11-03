# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='hardik@mysparrow.io',
    to_emails='hackergreen003@gmail.com',
    subject='Demo Email',
    html_content= """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Email Template</title>
    <style>
        /* General styles for emails */
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }

        table {
            border-spacing: 0;
            width: 100%;
        }

        td {
            padding: 10px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }

        .header {
            background-color: #0073e6;
            padding: 20px;
            text-align: center;
            color: white;
        }

        .content {
            padding: 20px;
            line-height: 1.6;
        }

        .footer {
            background-color: #0073e6;
            padding: 10px;
            text-align: center;
            color: white;
            font-size: 12px;
        }

        a {
            color: #0073e6;
            text-decoration: none;
        }

        a.button {
            background-color: #0073e6;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>
</head>

<body>
    <table class="container">
        <!-- Email Header -->
        <tr>
            <td class="header">
                <h1>Call from Sparrow</h1>
            </td>
        </tr>

        <!-- Email Body -->
        <tr>
            <td class="content">
                <h2>Hello,</h2>
                <p>Welcome to our service! We are thrilled to have you on board.</p>
                <p>If you have any questions, feel free to reach out to us at any time.</p>
                <p>To get started, click the button below:</p>
                <p><a href="#" class="button">Get Started</a></p>
                <p>Best regards,</p>
                <p>Your Company Team</p>
            </td>
        </tr>

        <!-- Email Footer -->
        <tr>
            <td class="footer">
                <p>&copy; 2024 Your Company. All rights reserved.</p>
                <p><a href="#">Unsubscribe</a> | <a href="#">Privacy Policy</a></p>
            </td>
        </tr>
    </table>
</body>

</html>
"""
    )
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)