import re


class ValidationError(Exception):
    def __init__(self, message, error_type):
        super().__init__(message)
        self.error_type = error_type


class User:
    def __init__(self):
        print(
            f"{' Welcome to registration form ':*^100}\n"
            f"{' In order to register on our website, please provide following information: ': ^100}"
        )
        self.name = input("What's your name? \n").lower().capitalize()
        self.surname = input("What's your surname? \n").lower().capitalize()

        while True:
            try:
                self.email = self.validate_email(input("Specify your email address: \n").lower())
                break
            except ValidationError as e:
                print(f'Invalid email: {e}')

        while True:
            try:
                self.password = self.validate_pwd(input("Password: \n"))
                break
            except ValidationError as e:
                print(f'Invalid password: {e}')

        print(f"{f'Dear {self.name} {self.surname}, you have been successfully registered!': ^100}")
        print(f"{f'Please confirm your email by the link sent to: {self.email}': ^100}")

    def validate_email(self, email):
        if re.match(r'^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email):
            return email
        else:
            raise ValidationError('Invalid email address', 'EmailValidationError')

    def validate_pwd(self, pwd):
        if len(pwd) < 8:
            raise ValidationError('Invalid password. Password must be at least 8 characters long.',
                                  'PasswordValidationError')
        if (re.search(r'[a-z]', pwd) and
                re.search(r'[A-Z]', pwd) and
                re.search(r'[0-9]', pwd) and
                re.search(r'[!"$;%:?*()_+-,.^]', pwd)):
            return pwd
        else:
            raise ValidationError(
                'Invalid password. Password must contain at least one lowercase letter, '
                'one uppercase letter, one digit, and one special character.','PasswordValidationError'
            )


user1 = User()





