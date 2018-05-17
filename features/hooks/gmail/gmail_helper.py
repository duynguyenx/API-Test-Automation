import base64

from features.hooks.gmail.gmail_api import GmailAPI


class GmailHelper(GmailAPI):
    def __init__(self, client_secret_file_path, file_storage_path):
        GmailAPI.__init__(self, client_secret_file_path=client_secret_file_path, file_storage_path=file_storage_path)

    def get_unread_emails(self):

        return self.get_mail_list(query='is:unread')

    def get_current_user_email(self, unread_emails, user_id):

        for email in unread_emails:
            email_content = self.get_mail_content(msg_id=email['id'])

            for header in email_content['payload']['headers']:
                if header['name'] == 'To' and user_id in header['value']:
                    msg_str = base64.urlsafe_b64decode(email_content['payload']['body']['data'].encode('ASCII'))
                    current_email_id = email['id']
                    return msg_str, current_email_id
            return 0, 0

    def delete_email(self, email_id):

        if email_id:
            self.delete_email_id(msg_id=email_id)
