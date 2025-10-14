# Email Notifications Setup Guide

This guide explains how to configure email notifications for the User Filtering GitHub Actions workflow.

## 📧 Required GitHub Secrets

To enable email notifications, you need to set up the following secrets in your GitHub repository:

### 1. Go to Repository Settings
1. Navigate to your GitHub repository
2. Click on **Settings** tab
3. Go to **Secrets and variables** → **Actions**
4. Click **New repository secret**

### 2. Add Required Secrets

#### `EMAIL_USERNAME`
- **Description**: Email address used to send notifications
- **Value**: Your email address (e.g., `your-email@gmail.com`)
- **Note**: For Gmail, this should be your Gmail address

#### `EMAIL_PASSWORD`
- **Description**: App password for the email account
- **Value**: Generated app password (NOT your regular email password)
- **For Gmail**: 
  1. Enable 2-Factor Authentication on your Google account
  2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
  3. Generate an app password for "Mail"
  4. Use this 16-character password

#### `NOTIFICATION_EMAIL`
- **Description**: Email address to receive notifications
- **Value**: Email address where you want to receive notifications
- **Note**: Can be the same as EMAIL_USERNAME or different

## 🔧 Supported Email Providers

### Gmail (Recommended)
```yaml
server_address: smtp.gmail.com
server_port: 587
```

### Outlook/Hotmail
```yaml
server_address: smtp-mail.outlook.com
server_port: 587
```

### Yahoo Mail
```yaml
server_address: smtp.mail.yahoo.com
server_port: 587
```

### Custom SMTP Server
Update the workflow file with your SMTP server details:
```yaml
server_address: your-smtp-server.com
server_port: 587  # or 465 for SSL
```

## 📨 Notification Types

### Success Notifications
- ✅ Sent when workflow completes successfully
- Includes filtered user count, age threshold, and artifact link
- Professional HTML format with detailed results table

### Failure Notifications
- ❌ Sent when workflow fails at any step
- Includes error details and troubleshooting steps
- Links to workflow logs for debugging

## 🧪 Testing Email Setup

1. **Test Configuration**: Push a small change to trigger the workflow
2. **Check Logs**: Verify the workflow runs without email errors
3. **Check Inbox**: Confirm you receive the notification email

## 🛠️ Troubleshooting

### Common Issues:

#### "Authentication Failed"
- Verify `EMAIL_USERNAME` is correct
- Ensure `EMAIL_PASSWORD` is an app password, not your regular password
- For Gmail, confirm 2FA is enabled and app password is generated

#### "Connection Timeout"
- Check SMTP server address and port
- Some networks block SMTP ports - try different network

#### "No Email Received"
- Check spam/junk folder
- Verify `NOTIFICATION_EMAIL` address is correct
- Check GitHub Actions logs for email sending errors

### Email Provider Specific:

#### Gmail
- Must use app passwords (requires 2FA)
- Regular passwords won't work
- App password format: 16 characters without spaces

#### Corporate Email
- May require different SMTP settings
- Contact IT department for SMTP server details
- May need VPN or specific network access

## 🔒 Security Best Practices

1. **Never commit credentials** to the repository
2. **Use app passwords** instead of regular passwords
3. **Rotate secrets** periodically
4. **Limit repository access** to trusted users
5. **Monitor email notifications** for unauthorized access

## 📋 Example Secret Values

```
EMAIL_USERNAME: myaccount@gmail.com
EMAIL_PASSWORD: abcd efgh ijkl mnop  (16-char app password)
NOTIFICATION_EMAIL: notifications@mycompany.com
```

## 🔄 Email Content

### Success Email Includes:
- Repository and branch information
- Age filter used
- Number of users found
- Timestamp and artifact name
- Direct link to download artifacts

### Failure Email Includes:
- Error context (repository, branch, commit)
- Troubleshooting checklist
- Direct link to workflow logs
- Run details for debugging