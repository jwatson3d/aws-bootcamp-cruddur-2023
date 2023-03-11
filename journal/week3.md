# Week 3 — Decentralized Authentication

## Cognito

### Create Cognito User Pool

![user-pool](assets/cruddur-wk3-user-pool.png)

### AWS Amplify Install

![npm-list](assets/cruddur-wk3-npm-list.png)

### AWS Cognito User Pool

![user-pool](assets/cruddur-wk3-user-pool.png)

### AWS Cognito Invalid User

![invalid-user-pwd](assets/cruddur-wk3-invalid-user-pwd.png)

### AWS Cognito Access Token Error

![access-token](assets/cruddur-wk3-access-token.png)

### AWS Cognito Set User Password CLI

```shell
aws cognito-idp admin-set-user-password \
  --user-pool-id <your-user-pool-id> \
  --username <username> \
  --password <password> \
  --permanent
```

![set-user-pwd](assets/cruddur-wk3-set-user-pwd.png)

### AWS Cognito Login Success

![login-success](assets/cruddur-wk3-login-success.png)
